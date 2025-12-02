# Hybrid RAG with Critic–Refiner Workflow (Qwen2.5 + LAmini)

## 1. 🎯Goal

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline enhanced
 with a **dual-stage Critic–Refiner architecture**.

The main objective was to create a **highly accurate, context-grounded, and reliable
 question-answering system**, combining:

- **Qwen2.5-7B-Instruct** (cloud-based Critic)  
- **LAmini (local GGUF model)** (Refiner)  
- **LlamaIndex** (retrieval engine)  

The system rigorously evaluates draft answers using a critic model, detects
factual errors or missing context, and then rewrites them using a local refiner
 model.  
This produces answers that are **trustworthy**, **grounded**, and **fully derived
 from source documents**.

---

## 2. 🤖 About the Models Used

### 2.1 Qwen2.5-7B-Instruct (Critic Model)

Qwen2.5-7B is a powerful instruction-tuned LLM developed by Alibaba Cloud.  
It was chosen as the **Critic** for these reasons:

- **High factual reliability:** Qwen models consistently score high in truthfulness
- and instruction-following benchmarks.
- **Ideal for evaluation:** As a cloud-based model on Hugging Face Inference API,
- it is fast, stable, and accurate.
- **Excellent reasoning capabilities:** Perfect for evaluating alignment between
- retrieved context and generated draft answers.

### 2.2 LAmini (Local Refiner Model)

LAmini is a compact, efficient, open-source model designed for rewriting and
stylistic refinement.  
It was selected as the **Refiner** because:

- **Small and fast:** Runs comfortably on consumer hardware in `.gguf` format.
- **Excellent at rewriting:** Ideal for polishing or correcting drafts based on
- reviewer feedback.
- **Local privacy:** No online requests; all refinement happens locally.
- **Lightweight:** Fits the project's goal of low-cost, local execution.

### 2.3 Why a Critic–Refiner System?

This architecture ensures:

- The **Critic** checks for correctness, consistency, and missing facts.  
- The **Refiner** rewrites only the necessary corrections.  
- The workflow minimizes hallucinations and guarantees source-grounded answers.

This structure is heavily inspired by **self-correcting LLM systems** and
 **Human-in-the-Loop editorial workflows**, but automated.

---

## 3. 🛠️ Methodology: Retrieval-Augmented Generation (RAG)

To answer questions based on documents not included in the LLM’s training data,
 RAG augments the model’s knowledge using retrieval.

The pipeline works as follows:

1. **Retrieval:**  
   User question → Convert to embedding → Search vector index → Retrieve relevant
   text chunks.

2. **Draft Generation:**  
   The retrieved context + question are used to generate a **draft answer**.

3. **Critic Evaluation (Qwen2.5):**  
   The critic compares the draft answer against the retrieved context and returns:
   - `[OK]` — Draft is accurate  
   - `[REVISE]` — Draft contains errors/missing info  
     - plus a bulleted list of required corrections.

4. **Refinement (LAmini):**  
   LAmini rewrites the draft based **only on the critic’s feedback**, producing
   the final polished answer.

This ensures accuracy and consistency with the source documents.

### Implementation Details

- **Framework:** `LlamaIndex`
- **Local Model Loader:** `llama-cpp-python`
- **Embedding Model:** `HuggingFaceEmbedding` (e.g., BAAI/bge-small)
- **Critic Model:** `Qwen/Qwen2.5-7B-Instruct` via HuggingFace Inference API
- **Refiner Model:** `LAmini-Chat` in `.gguf` format
- **Energy Tracking:** CodeCarbon (`OfflineEmissionsTracker`)

---

## 4. 📑 Prompt Engineering: The Editorial Workflow

### 4.1 Critic Prompt

The Critic acts like a strict editor.

It must:

- Judge the draft answer
- Compare it with the source context
- Output `[OK]` or `[REVISE]`
- Provide bullet-point feedback only when necessary

Example behavior:
[REVISE]

The draft added information not found in the source context.

Missing key fact about X.

### 4.2 Refiner Prompt (LAmini)

The Refiner receives:

- Draft answer  
- Editor (Critic) feedback  

It rewrites the answer accordingly, following strict rules:

- Only fix issues the Critic highlighted
- No new information allowed
- Must produce a complete final answer

This avoids adding hallucinations and ensures correctness.

---

## 5. 📊 Sample Workflow (Prompts & Responses)

You can include your own examples below.

### Example 1: [Your Question Here]

- **Prompt:**  
    > **Paste your question here**

- **Draft Answer:**  
    > **Paste model output here**

- **Critic Response:**  
    > **Paste critic evaluation here**

- **Refined Answer (Final):**  
    > **Paste LAmini rewrite here**

- **My Analysis:**  
    > [Your notes]

---

### Example 2: [Your Question Here]

(Same structure)

---

### Example 3: [Your Question Here]

(Same structure)

---

## 6. 🌱 Environmental Tracking

We used **CodeCarbon** to measure local compute emissions and energy usage.

This enables:

- Transparency regarding energy cost
- Comparison with API-based approaches
- Understanding environmental impact on local hardware

---

## 7. 📚 References (Reputable Sources)

All documentation used:

- Hugging Face Inference API  
  <https://huggingface.co/docs/api-inference>  

- LlamaIndex Documentation  
  <https://docs.llamaindex.ai>  

- LAmini Models  
  <https://huggingface.co/LinkSoul/LAmini-Chat>  

- Qwen2.5 Models  
  <https://huggingface.co/Qwen>  

- LlamaCPP / GGUF Models  
  <https://github.com/ggerganov/llama.cpp>  

- CodeCarbon  
  <https://mlco2.github.io/codecarbon/>  

---

## 8. ✅ Summary

This project demonstrates a powerful hybrid RAG architecture that blends cloud
 reasoning and local refinement.  
Using a Critic–Refiner pipeline dramatically increases accuracy, reduces
 hallucinations, and ensures answers remain faithful to the source documents.

LAmini provides fast, private, offline rewriting, while Qwen2.5 guarantees
 high-quality factual evaluation.

Together, they form a reliable, cost-efficient, and production-ready RAG system.
