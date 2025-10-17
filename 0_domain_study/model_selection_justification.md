# Comparing Open-Source and Commercial LLMs on Reasoning and Summarization Tasks

## Summary

**Model Pairing:** GPT-4 vs. Mistral-3B (4 variants)  
**Tasks:** Reasoning + Summarization  
**Evaluation:** Accuracy, stepwise logic, summarization quality  
**Sample Size:** Start small, scale to 50+ for significance  

---

## Goal

To compare the accuracy and environmental impact of:  

- One commercial LLM (closed-source)  
- One open-source LLM in four configurations:  
  - Original  
  - Distilled  
  - RAG-enhanced (Retrieval-Augmented Generation)  
  - Distilled + RAG  

---

## Recommended Commercial Model

**Model:** GPT-4 (OpenAI)  

**Why:**  

- Industry benchmark for reasoning and summarization  
- Strong performance across tasks  
- Compatible with G-Eval evaluation  
- API access available (paid)  

**Alternative:** Claude 3 Opus (Anthropic): strong in reasoning,  
slightly weaker in summarization.  

---

## Recommended Open-Source Model

**Model:** Mistral-3B  

**Why:**  

- Lightweight and energy-efficient — smaller carbon footprint than 7B  
- Good performance for its size and architecture  
- Easy to distill and integrate with RAG  
- Active open-source community on Hugging Face  

**Alternative:** Mistral-7B (legacy, more accurate but heavier) or  
LLaMA-3-8B (requires stronger GPUs).  

---

## Evaluation Strategy

### 1. Reasoning Tasks

- ARC (AI2 Reasoning Challenge / grade-school science questions)  
- GSM8K (Math reasoning)  
- ProofWriter (Step-by-step inference)  
- LogiQA (Logical multiple choice)  

### 2. Summarization Tasks

- News articles  
- Academic abstracts  
- Narrative texts  

---

## Sample Size Recommendations

| Sampling Level | Purpose / Use Case | Reasoning | Summarization |
|----------------|--------------------|------------|----------------|
| Preliminary | Quick validation and failure detection | 50–100 | 50–100 |
| Reliable | Statistically meaningful trends | 200–500+ | 200–500+ |
| Academic | Comprehensive benchmark-level | 1,000–10,000+ | 1,000–10,000+ |

**Rationale:**  

- Preliminary: Initial signal of model behavior.  
- Reliable: Minimum for academic validity (500+ examples).  
- Academic: Derived from MMLU and MATH benchmarks (1,000+ examples).  

---

## Academic Justification of Sample Size

| Ref | Benchmark / Source | Justification |
|-----|--------------------|----------------|
| G1 | MMLU Benchmark | 57 subjects, thousands of Qs → 1,000+ needed |
| G2 | MATH Benchmark | 12,500 math problems → 1,000+ subset valid |
| G3 | ANLI / LLM Eval | 1,200 test examples → supports 200–500+ |
| G4 | ML Sample Size | 500+ gives strong validity in ML research |

---

## Why This Project Is Niche and Valuable

**Unique because:**  

- Compares *versions* of the same open-source model.  
- Evaluates *accuracy + environmental impact* (energy, CO₂).  

**Valuable because:**  

- Helps understand trade-offs between performance and footprint.  
- Designed for student teams with limited resources.  
- Provides replicable framework for *ethical + technical* evaluation.  
- Supports the global shift toward *eco-conscious AI*.  

**References:**  

- [DeepSeek vs GPT-4 vs LLaMA vs Mistral vs Cohere](https://www.aubergine.co/insights/deepseek-v3-vs-gpt-4-vs-llama-3-vs-mistral-7b-vs-cohere)  
- [Mistral vs GPT comparison](https://dev.to/abhinowww/mistral-vs-gpt-a-comprehensive-comparison-of-leading-ai-models-2lk2)  

---

## Note on Mistral Model Selection

- Mistral-7B is a *legacy model* (as of March 2025) but still benchmarked.  
- Mistral-3B offers better efficiency, lower GPU use, smaller footprint.  
- Our main open-source model: **Mistral-3B**  
- Mistral-7B appears as a baseline reference.  
- Mistral-Nemo: Mentioned as a next-generation model for discussion.  
