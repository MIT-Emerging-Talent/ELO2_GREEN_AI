import json

from datasets import Dataset
from langchain_community.llms import LlamaCpp  # Use LangChain's LlamaCpp for evaluation
from llama_index.embeddings.huggingface import (
    HuggingFaceEmbedding,
)  # Need this for embeddings
from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import answer_relevancy, faithfulness

# --- 1. Configuration ---
MODEL_PATH = "D:/Mistral7B/mistral-7b-instruct-v0.2.Q4_K_M.gguf"  # Same model used for generation
INPUT_FILE = "D:/Mistral7B/rag_results.json"  # The file saved by the previous script

# --- 2. Load the Saved Results ---
print(f"Loading results from {INPUT_FILE}...")
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

# Convert the list of dictionaries into a Hugging Face Dataset
# Ragas requires columns named 'question', 'answer', 'contexts'
eval_dataset = Dataset.from_list([loaded_data[0]])  # Only evaluate the first item
print(f"Loaded {len(eval_dataset)} results.")

# --- 3. Initialize Evaluator Model and Embeddings ---
print("Initializing evaluator models...")
# ... (gpu_layers = 0 setting) ...

eval_llm = LlamaCpp(
    model_path=MODEL_PATH,
    # ... other parameters ...
    n_ctx=1024,  # Keep reduced context
    # ...
)
ragas_llm = LangchainLLMWrapper(eval_llm)

# --- ADD THIS TEST BLOCK ---
print("\n--- Testing eval_llm directly ---")
try:
    test_prompt = (
        "Explain the importance of testing in software development in one sentence."
    )
    print(f"Sending test prompt: {test_prompt}")
    response = eval_llm.invoke(test_prompt)
    print(f"Test response received: {response}")
    print("--- eval_llm test successful ---\n")
except Exception as e:
    print("--- eval_llm test FAILED ---")
    print(f"Error during direct invocation: {e}")
    import traceback

    traceback.print_exc()
    # Decide if you want to exit here or continue to ragas evaluation
    # exit() # Uncomment to stop if the direct test fails
# --- END OF TEST BLOCK ---

# Ragas metrics might also need embeddings
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# --- 4. Run Ragas Evaluation ---
print("\n--- Running Ragas Accuracy Evaluation ---")

try:
    print("Starting Ragas evaluate()...")  # <-- ADDED
    result = evaluate(
        eval_dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
        ],
        llm=ragas_llm,
        embeddings=embed_model,
        # raise_exceptions=False # Optional: Try adding this if it keeps crashing
    )
    print("Ragas evaluate() finished.")  # <-- ADDED

    print("\n--- Ragas Accuracy Results ---")
    print(result)  # <-- KEEP THIS

    # Save results to a file for later analysis
    print("Preparing to save results to JSON...")  # <-- ADDED
    with open("ragas_evaluation_results.json", "w") as f:
        # Convert numpy values to Python native types for JSON serialization
        import numpy as np

        # Check if result is not None and is a dictionary before processing
        if result and isinstance(result, dict):
            result_dict = {
                k: float(v)
                if isinstance(v, (np.number, float)) and not np.isnan(v)
                else None
                for k, v in result.items()
            }
            print(
                f"Result dictionary prepared: {result_dict}"
            )  # <-- ADDED (optional, can be verbose)
            json.dump(result_dict, f, indent=4)
            print("Results saved to ragas_evaluation_results.json")  # <-- ADDED
        else:
            print(
                "Evaluation result was None or not a dictionary, skipping save."
            )  # <-- ADDED

except Exception as e:
    print("\n--- Evaluation Error ---")
    print(f"Error during evaluation or saving: {e}")  # <-- MODIFIED
    import traceback

    traceback.print_exc()

# Make sure to explicitly delete the model to avoid memory issues
if "eval_llm" in locals():
    print("Deleting LLM objects...")  # <-- ADDED
    del ragas_llm
    del eval_llm
    print("LLM objects deleted.")  # <-- ADDED

print("\n--- Evaluation Script Finished ---")
