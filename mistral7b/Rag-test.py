from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.llama_cpp import LlamaCPP

# --- Configuration ---
# Point to your downloaded model file
MODEL_PATH = "D:/Mistral7B/mistral-7b-instruct-v0.2.Q4_K_M.gguf"  # <-- IMPORTANT: update this path

# --- 1. Load the LLM (our quantized Mistral model) ---
# This uses llama-cpp-python to run the GGUF model on your CPU
llm = LlamaCPP(
    model_path=MODEL_PATH,
    # Model parameters - you can adjust these
    temperature=0.1,
    max_new_tokens=512,
    context_window=3900,  # The model's context window size
    generate_kwargs={},
    model_kwargs={
        "n_gpu_layers": -1
    },  # Set to > 0 if you have a GPU and want to offload layers
    verbose=True,
)

# --- 2. Configure the Embedding Model ---
# This model creates numerical representations of your text for retrieval.
# It runs locally on your machine.
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# --- 3. Set up Global Settings ---
# This tells LlamaIndex to use our chosen models.
Settings.llm = llm
Settings.embed_model = embed_model

# --- 4. Load Your Data ---
# This will load all files from the 'data' directory.
print("Loading documents...")
documents = SimpleDirectoryReader("D:/Mistral7B/data").load_data()
print(f"Loaded {len(documents)} document(s).")

# --- 5. Create the Index and Query Engine ---
# The VectorStoreIndex will process your documents and build a searchable index.
# The query engine connects the retriever (finds relevant text) with the LLM (generates answers).
print("Indexing documents... (this may take a moment)")
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(streaming=True)

# --- 6. Start Querying ---
print("\n--- Query Engine Ready ---")
while True:
    query = input("Ask a question about your documents: ")
    if query.lower() == "exit":
        break

    response_stream = query_engine.query(query)

    print("\nAssistant: ", end="")
    # Stream the response to the console
    response_stream.print_response_stream()
    print("\n" + "-" * 50)
