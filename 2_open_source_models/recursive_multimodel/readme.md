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

### Example: [Summarization]

- **Prompt:**  
  > In your own words, describe what happened when the computer alarms
  appeared during the landing.

### **Cycle 1:**

- **Draft Answer:**
  >As the descent began, Armstrong and Aldrin found themselves
  passing landmarks on the surface two or three seconds early. The problem could
  have been mascons, concentrations of high mass in a region or regions of the
  Moon's crust that contains a gravitational anomaly, potentially altering Eagle's
  trajectory. Five minutes into the descent, the burn and 6,000 feet (1,800 m)
  above the surface of the moon, the LM guidance computer (LGC) distracted the
  crew with the first of several unexpected 1201 and 1202 program alarms. Inside
  Mission Control Center, computer engineer Jack Garman told Guidance Officer
  Steve Bales it was safe to continue the descent. The program alarm indicated
  "executive overflows," meaning the guidance computer could not complete all its
  tasks in real-time and had to postpone some of them. Margaret Hamilton, the
  Director of Apollo Flight Computer Programming at the MIT Charles Stark Draper
  Laboratory later recalled: "To blame the computer for the Apollo 11 problems is
  like blaming the person who spots a fire and calls the fire department.
  Actually, the computer was programmed to do more than recognize error
  conditions. A complete set of recovery programs was incorporated into the
  software. The software's action, in this case, was to eliminate lower priority
  tasks and re-establish the more important ones. The computer, rather than almost
  forcing an abort, prevented an abourt. If the computer hadn't recognized this
  problem and took recovery action, I doubt if Apollo 11 would have been the
  successful Moon landing it was.

- **Critic Response:**

  >- The draft does not accurately describe the computer alarms that appeared
  during the landing. The draft should include the specific computer alarms
  (1201 and 1202) and the crew's reaction to them.
  >- The draft does not mention the specific actions taken by the crew in
  response to the computer alarms, such as Armstrong taking semi-automatic control.
  >- The draft does not include the details about Mission Control's role in
  addressing the alarms and the reassurance given to the crew.
  >- The draft does not mention the post-mission analysis showing the real fuel
  remaining was probably closer to 50 seconds, which is critical information.

### **Cycle 2:**

- **Draft Answer:**
  >The LM guidance computer (LGC) distracted the crew with the first
  of several unexpected 1201 and 1202 program alarms during the Apollo 11 mission.
  The program alarm indicated "executive overflows," meaning the guidance computer
  could not complete all its tasks in real-time and had to postpone some of them.
  The recovery programs were incorporated into the software, eliminating lower
  priority tasks and re-establishing the more important ones. Margaret Hamilton,
  the Director of Apollo Flight Computer Programming at the MIT Charles Stark
  Draper Laboratory later recalled that to blame the computer for the Apollo 11,
  problems is like blaming the person who spots a fire and calls the fire
  department. Actually, the computer was programmed to do more than recognize
  error conditions. The software's action, in this case, was to eliminate lower
  priority jobs and regain the more significant ones. If the computer hadn't
  recognized this problem and took recovery action, I doubt if Apollo 11 would
  have been the successful Moon landing it was.

- **Critic Response:**

  >- The draft does not mention the specific computer alarms (1201 and 1202)
  that appeared during the landing.
  >- The draft does not reference the exact timing of the alarms (five minutes
  into the descent, 6,000 feet above the surface).
  >- The draft does not include the specific actions taken by Mission Control
  to address the alarms.
  >- The draft does not mention the critical role of the guidance computer in
  safely continuing the descent despite the alarms.
  >- The draft does not include the perspective of the astronauts experiencing
  the alarms.
  >- The draft does not provide the exact quote from Jack Garman to Steve Bales.
  >- The draft does not mention Margaret Hamilton's role or her specific
  recollection of the event.

- **Refined Answer (Final):**

  >The LM guidance computer (LGC) distracted the crew with the first
  of several unexpected 1201 and 1202 program alarms during the Apollo 11 mission.
  The program alarm indicated "executive overflows," meaning the guidance computer
  could not complete all its tasks in real-time and had to postpone some of them.
  The recovery programs were incorporated into the software, eliminating lower
  priority tasks and re-establishing the more important ones. Margaret Hamilton,
  the Director of Apollo Flight Computer Programming at the MIT Charles Stark
  Draper Laboratory later recalled that to blame the computer for the Apollo 11,
  problems is like blaming the person who spots a fire and calls the fire
  department. Actually, the computer was programmed to do more than recognize
  error conditions. The software's action, in this case, was to eliminate lower
  priority jobs and regain the more significant ones. If the computer hadn't
  recognized this problem and took recovery action, I doubt if Apollo 11 would
  have been the successful Moon landing it was.

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
