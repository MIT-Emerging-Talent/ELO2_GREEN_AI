# 🌱 ELO2 – GREEN AI  

***Comparing Commercial and Open-Source Language Models for***
***Sustainable AI***

This repository presents the **ELO2 – GREEN AI Project**, developed
within the **MIT Emerging Talent – AI & ML Program (2025)**. The work
investigates the technical performance, sustainability traits, and
human-perceived quality of **open-source small language models (SLMs)**
compared to commercial systems.

---

## 🔍 Project Overview

### Research Question

**To what extent can open-source LLMs provide competitive output quality
while operating at significantly lower environmental cost?**

### Motivation

Large commercial LLMs deliver strong performance but demand substantial
compute and energy. This project examines whether **small, accessible,
and environmentally efficient open-source models**—especially when
enhanced with retrieval and refinement pipelines—can offer practical
alternatives for everyday tasks.

---

## 🧪 Methods

### 1. Model Families

The study evaluates several open-source model groups:

- **Quantized Model:** Mistral-7B (GGUF)
- **Distilled Model:** LaMini-Flan-T5-248M
- **Small Models:** Qwen, Gemma
- **Enhanced Pipelines (applied to all model families):**
  - **RAG (Retrieval-Augmented Generation)**
  - **Recursive Editing**
    - includes AI-based critique and iterative refinement

These configurations serve as the optimized open-source setups used in
the comparison against commercial models.

---

### 2. Tasks & Dataset

Evaluation tasks include:

- summarization
- factual reasoning
- paraphasing
- short creative writing
- instruction following
- question answering

A targeted excerpt from the **Apollo-11 mission transcripts** served as
the central reference text for all evaluation tasks. All prompts were constructed
directly from this shared material. Using a single, consistent source ensured
that every model was tested under identical informational conditions, allowing
clear and fair comparison of output quality and relevance.

---

### 3. RAG Pipeline

Retrieval-Augmented Generation (RAG) was applied to multiple model
families. The pipeline includes:

- document indexing  
- dense similarity retrieval  
- context injection through prompt augmentation  
- answer synthesis using guidance prompts  

RAG improved factual grounding in nearly all models.

---

### 4. Recursive Editing Framework

A lightweight iterative refinement procedure was implemented:

1. **Draft Generation:**  
   The primary model produces an initial output.

2. **AI-Based Critique:**  
   A secondary SLM evaluates clarity, accuracy, faithfulness and relevance.

3. **Refinement Step:**  
   A revision prompt integrates critique and generates an improved text.

4. **Stopping Condition:**  
   The cycle ends after a fixed number of iterations or when critique
   stabilizes.

This approach allowed weaker SLMs to yield higher-quality results
without relying on large models.

---

### 5. Environmental Measurement

Environmental footprint data was captured with **CodeCarbon**, recording:

- CPU/GPU energy usage
- carbon emissions
- PUE-adjusted overhead

These measurements enabled comparison with published metrics for
commercial LLMs.

---

### 6. Human Evaluation (Single-Blind)

A structured Google Form experiment collected:

- **source identification** (commercial vs. open-source)  
- **quality ratings** on accuracy, faithfulness, relevance, and clarity  
  (1–5 scale)

Outputs were randomized and anonymized to avoid bias. This provided a
perception-based counterpart to technical evaluation.

---

## 📊 Key Findings

- FINDING1.....
- FINDING2.....
- FINDING3.....
- FINDING4.....

More detailed results are included in the research article.

---

## 👥 Contributors

- [Amro Mohamed](https://github.com/Elshikh-Amro)
- [Aseel Omer](https://github.com/AseelOmer)
- [Banu Ozyilmaz](https://github.com/doctorbanu)
- [Caesar Ghazi](https://github.com/CaesarGhazi)
- [Reem Osama](https://github.com/reunicorn1)
- [Safia Gibril Nouman](https://github.com/Safi222)

---

## 🙏 Acknowledgments

Special thanks to the **MIT Emerging Talent Program** for their
guidance and feedback throughout the project.
