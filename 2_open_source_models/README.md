# **Open-Source Model Experiments**

This directory contains four standalone experiments exploring
**local, open-source language models** for Retrieval-Augmented Generation
(RAG), model evaluation, recursive editing, and sustainability tracking
(energy & CO₂ emissions).
Each subfolder includes its own notebook, documentation, outputs, and
model-specific setup.

---

## Directory Structure

```text
2_open_source_models/
│
├── distilled_models/
│   └── rag_and_distilled_model/
│
├── quantized_models/
│   └── mistral7b/
│
└── slm/
    ├── google_gemm/
    └── qwen/
```

Each subfolder contains a self-contained model with its own README,
notebook(s), generated outputs, and energy/emissions logs where applicable.

---

## Project Summaries

Below is a concise description of each model project to understand
the purpose of the overall folder at a glance.

---

### **1. Distilled Models – RAG + Instruction-Tuned Distilled LMs**

**Folder:** `distilled_models/rag_and_distilled_model/`
**Notebook:** `Apollo11_rag&distilled.ipynb`

This project uses a lightweight **LaMini-Flan-T5-248M** distilled model
combined with a **MiniLM** embedding model to run a fully local
Retrieval-Augmented Generation pipeline on the Apollo 11 dataset.
It demonstrates:

* Local embeddings and ChromaDB vector storage
* RAG-based question answering
* Evaluation across several prompt types
* Emissions tracking and generated output logs

Ideal for showing how **compact distilled models** can handle
RAG efficiently on CPU or modest GPU hardware.

---

### **2. Quantized Models – Mistral 7B RAG Pipeline**

**Folder:** `quantized_models/mistral7b/`

This project evaluates a **quantized Mistral-7B (GGUF)** model running
fully locally via `llama-cpp-python`.
It focuses on:

* Retrieval-Augmented Generation using LlamaIndex
* Local inference using a 4-bit quantized LLM
* Document processing, embedding (BGE-small), and top-k retrieval
* Practical observations on feasibility and performance on a laptop

A strong example of how quantization enables
**large-model capability at small-device cost**.

---

### **3. Small Language Model (SLM): Google Gemma 2-2B**

**Folder:** `slm/google_gemm/`

This experiment implements a structured RAG workflow with Google’s lightweight
**Gemma 2-2B** model and a fixed Apollo 11 source text.
Key features include:

* Standardized 21-prompt evaluation set
* RAG pipeline with chunked retrieval
* Draft to Critic to Refiner multi-step generation
* Real-time emissions logging with CodeCarbon
* Fully reproducible testing and reporting

This project demonstrates how even very small open-weight models can
perform multi-step reasoning when paired with thoughtful prompting and revision
cycles.

---

### **4. Small Language Model (SLM): Qwen 2.5B + Recursive Editing**

**Folder:** `slm/qwen/`

This notebook experiments with **Qwen 2.5B**, integrating:

* RAG retrieval
* A recursive editing loop (Draft to Critic to Refine)
* Context retrieval through Hugging Face embeddings
* Energy + CO₂ logging for each query

Outputs are saved in markdown form with all iterations and emissions data.

---

## Purpose of This Collection

This folder exists to:

* Compare how different **model sizes**, **architectures**, and
**inference strategies** behave on the **same tasks**.
* Demonstrate **fully local RAG pipelines** using only open-source components.
* Document **energy and carbon trade-offs** in local LLM usage.
* Provide reproducible examples that can be extended or rerun with other models.

Each subfolder is designed as a standalone experiment, but together they
form a cohesive study of open-source LLM efficiency and performance.

---

## Notes

* All code is intended to run locally.
* Each folder includes its own notebook and README with instructions.
* Energy/emissions reporting is included where relevant (via CodeCarbon).
* Datasets and prompts are standardized across projects for fairness and comparability.
