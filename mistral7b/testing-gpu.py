from llama_cpp import Llama

# --- Configuration ---
# IMPORTANT: Update this to the correct path on your machine
MODEL_PATH = "D:/Mistral7B/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

print("Attempting to load model with GPU...")

try:
    llm = Llama(
        model_path=MODEL_PATH,
        n_gpu_layers=-1,  # Try to offload all layers to GPU
        verbose=True,  # This is the most important part!
    )
    print("\n--- TEST SUCCESSFUL ---")
    # Check the output above for lines mentioning CUDA or cuBLAS and layer offloading

except Exception as e:
    print("\n--- TEST FAILED ---")
    print(f"An error occurred: {e}")
