import os
import time
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from codecarbon import OfflineEmissionsTracker
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset
from langchain_community.llms import LlamaCpp
from ragas.llms import LangchainLLMWrapper

# --- 1. Configuration ---

# Set the path to your downloaded GGUF model
MODEL_PATH = "D:/Mistral7B/mistral-7b-instruct-v0.2.Q4_K_M.gguf" # <-- IMPORTANT: Update this path if needed

# Set the path to your data (PDFs, .txt, etc.)
DATA_PATH = "D:/Mistral7B/data" # <-- IMPORTANT: Update this path if needed

# Set your country's ISO code for CodeCarbon
# Find your code: https://en.wikipedia.org/wiki/List_of_ISO_3166-1_alpha-3_codes
# Using "EGY" for Egypt as an example
YOUR_COUNTRY_ISO_CODE = "EGY" 

# Define your "Golden Set" of test questions
TEST_QUESTIONS = [
    "What is the main topic of the document?",
    #"Summarize the key findings in three bullet points.",
    # ... add 10-15 more of your own questions ...
    #"What is [a specific term] according to the text?",
    #"What conclusion does the author reach?",
]

# --- 2. Initialize Models ---

print("Initializing models...")

# Load the local LLM (Mistral 7B)
llm = LlamaCPP(
    model_path=MODEL_PATH,
    temperature=0.1,
    max_new_tokens=512,
    context_window=3900,
    generate_kwargs={},
    model_kwargs={"n_gpu_layers": 1}, # Set > 0 if you have GPU offloading
    verbose=True,
)

# Load the local Embedding Model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Set up LlamaIndex global settings
Settings.llm = llm
Settings.embed_model = embed_model

# --- 3. Load & Index Documents ---

print("Loading documents...")
documents = SimpleDirectoryReader(DATA_PATH).load_data()
print(f"Loaded {len(documents)} document(s).")

print("Indexing documents... (this may take a moment)")
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
print("Indexing complete.")

# --- 4. Run Evaluation (Accuracy & Environmental Cost) ---

# Initialize a list to hold our evaluation data
eval_data = {
    "question": [],
    "answer": [],
    "contexts": [],
}

# Initialize the CO2 Emissions Tracker
print(f"\nInitializing CodeCarbon tracker for country: {YOUR_COUNTRY_ISO_CODE}")
tracker = OfflineEmissionsTracker(country_iso_code=YOUR_COUNTRY_ISO_CODE)
tracker.start()

print("\n--- Starting Evaluation Loop ---")

try:
    for query in TEST_QUESTIONS:
        print(f"\nQuerying: {query}")
        
        # --- Start tracking for this specific query ---
        tracker.start_task("RAG Query") 
        start_time = time.time()
        
        # Run the query
        response = query_engine.query(query)
        
        # --- Stop tracking for this query ---
        end_time = time.time()
        # stop_task() returns an EmissionsData OBJECT
        emissions_data = tracker.stop_task() 
        
        # Collect results for ragas
        answer = str(response)
        contexts = [node.get_content() for node in response.source_nodes]
        
        eval_data["question"].append(query)
        eval_data["answer"].append(answer)
        eval_data["contexts"].append(contexts)
        
        # --- Print Results for this Query ---
        print(f"Answer: {answer}")
        print("-" * 30)
        print(f"Latency: {end_time - start_time:.2f} seconds")
        
        # --- CORRECTED LINES ---
        # Access attributes using dot notation
        print(f"Emissions: {emissions_data.emissions * 1000:.6f} gCO2eq")
        print(f"Energy: {emissions_data.energy_consumed * 1000:.6f} Wh")
        # --- END OF CORRECTION ---
        
        print("=" * 50)

finally:
    # --- CORRECTED LINES ---
    # stop() returns a FLOAT (total_emissions_kg)
    total_emissions_kg = tracker.stop()
    print("\n--- Total Emissions Summary (Saved to emissions.csv) ---")
    # Access total energy from the tracker object itself
    print(f"Total Energy Consumed: {tracker.final_emissions_data.energy_consumed * 1000:.4f} Wh")
    print(f"Total CO2 Emitted: {total_emissions_kg * 1000:.4f} gCO2eq")
    # --- END OF CORRECTION ---


# --- 5. Run Ragas Accuracy Evaluation ---

print("\n--- Running Ragas Accuracy Evaluation ---")

# Convert your collected data into a Hugging Face Dataset object
eval_dataset = Dataset.from_dict(eval_data)

# --- Set up the Ragas evaluator to use YOUR local model ---
# We must wrap our local model for Ragas to use it as a judge.
# The easiest way is to use the Langchain wrapper.

# 1. Import the required LangChain and Ragas wrapper classes
#    You may need to run: pip install langchain-community


# 2. Create a new LangChain LlamaCpp object *just for evaluation*
#    This points to the same model file.
eval_llm = LlamaCpp(
    model_path=MODEL_PATH,
    n_gpu_layers=1,      # Match your settings from Section 2
    n_batch=512,         # Match your settings
    n_ctx=3900,          # Match your settings
    temperature=0,       # Evaluators should be deterministic
    verbose=False,
)
# 3. Wrap the LangChain object for Ragas
ragas_llm = LangchainLLMWrapper(eval_llm)

# 4. Run the evaluation, passing the wrapped LLM and embeddings directly
result = evaluate(
    eval_dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
    ],
    llm=ragas_llm,          # <-- Pass the evaluator LLM here
    embeddings=embed_model, # <-- Pass the embeddings here
)

print("\n--- Ragas Accuracy Results ---")
print(result)

# The result will be a dictionary like:
# {'faithfulness': 0.85, 'answer_relevancy': 0.92}

print("\n--- Project Evaluation Complete ---")