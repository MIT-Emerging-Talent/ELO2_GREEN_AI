<!-- markdownlint-disable MD024 MD013 -->
<!-- Disabled MD024 (Multiple headings with the same content) rule
because repeated headings (Summary, Action Items) are
intentionally used across multiple sections for structural clarity.
Disabled MD013 (Line length) rule because mathematical formulas
and technical content require longer lines for readability. -->

# Milestone 2 Meeting Minutes

## **Meeting 9**

**Date:** October 16, 2025 (Thursday, 2:00 PM EST)

**Attendees:** Amro, Aseel, Caesar, Safia

### **Summary**

- The team decided to change the project approach due to limited access to environmental data (energy, carbon, and water consumption) for commercial AI models such as GPT, Claude, and Gemini.
- Since large-scale testing requires computational resources beyond the team’s capacity, the new plan focuses on evaluating open-source models using laptop hardware.
- Results will be compared with published environmental and performance data of commercial models to highlight how open-source AI can provide sustainable and accessible alternatives.

### **Action Items**

1. **Research and calculate environmental cost metrics:**
    - **Energy Consumption:**

        Etotal=(PGPU×UGPU+PCPU×UCPU+Pothers)×tEtotal=(PGPU×UGPU+PCPU×UCPU+Pothers)×t

    - **Facility Overhead:**

        Efacility=Etotal×PUEEfacility=Etotal×PUE

    - **Carbon Footprint:**

        Cemissions=Efacility×CICemissions=Efacility×CI

    - **Water Footprint:**

        Wconsumed=Efacility×WUEWconsumed=Efacility×WUE

2. Determine how much laptop hardware can handle (small, medium, large up to 3B).
3. Apply FLOPs-based linear scaling and empirical interpolation to improve result accuracy.
4. Add all presented work from previous meeting (model selection, evaluation methodology, environmental metrics) to the **domain study section** of the repository.

---

## **Meeting 10**

**Date:** October 19, 2025 (Saturday, 12:00 PM EST)

**Attendees:** Amro, Aseel, Caesar, Banu, Reem

### Summary

- The group discussed options for testing and running AI models.
- Ideas included running quantized models locally (with some accuracy loss) and using Google Colab for limited runs.
- Another idea was to use the Hugging Face API for accuracy and RAG testing, though this approach does not allow measuring environmental costs.
- The team also explored Recursive Reasoning Models as efficient and environmentally friendly alternatives, though task variety for testing remains limited.

### Action Items

1. Watch the video about recursive models and explore whether a small-scale recursive model can be built.
2. If possible, compare its accuracy and environmental impact with a distilled model (e.g., **DistilGPT**).
3. If not feasible, return to comparing **basic**, **RAG**, **distilled**, and **commercial models**.

---

## **Meeting 11**

**Date:** October 22, 2025 (Wednesday, 12:00 PM EST)

**Attendees:** Amro, Aseel, Caesar, Reem, Safia, Banu

### Summary

- Following office hour feedback from Evan, the team decided to focus on **small language models (SLMs)** due to their efficiency.
- The group agreed to compare open-source SLMs with distilled commercial models.
- It was decided to apply **RAG techniques** (via the **Ragas Python library**) to quantized, SLM, and recursive models to narrow the gap with commercial systems.
- Because of the project’s evolving direction, the final deliverable will shift from a **dashboard** to a **research paper or article**.
- The team also plans to create a **Google Form** later to assess public and expert awareness of the topic.

### Action Items

- **Reem:** Test DistilBERT on Hugging Face
- **Aseel:** Research commercial models
- **Amro:** Test the RAG method
- **Caesar:** Combine Distilled + RAG models
- **Safia:** Combine SLM + RAG models
- **Banu:** Develop a unified test prompt (e.g., a poem or short text)
- **All:** Prepare the GitHub repository

### **Future Tasks**

- Create and distribute an awareness form
- Develop a communication strategy
- Publish the research article

---

## **Meeting 12**

**Date:** October 27, 2025 (Monday, 1:00 PM EST)

**Attendees:** Amro, Aseel, Caesar, Reem, Safia, Banu

### Summary

- Team members presented updates on their assigned tasks from the previous meeting.
- **Reem** shared findings on **DistilBERT**, concluding that the model performed poorly for the project’s needs.
- **Caesar** presented a **DistilBERT + RAG demo**, confirming similar inefficiencies; both suggested that RAG could still be valuable if paired with a more capable distilled model.
- **Amro** demonstrated his **RAG implementation**, discussed constraints, and noted ongoing refinements.
- **Safia** showcased her **SLM + RAG demo** and shared documentation.
- **Aseel** and **Banu** updated on **commercial model research** and **test prompt development** respectively.
- The team discussed next research directions:
  - Experiment with **recursive models**
  - Search for a more efficient **distilled model**
  - Possibly abandon commercial model comparisons in favor of evaluating specific approaches or model-task pairings

### Action Items

1. All members continue their respective research and experiments.
2. Push all updates and outputs to the **GitHub repository** before the **ELO2 Midpoint Breakout Room Session** on **Wednesday, October 29**.
3. Identify a better distilled model for testing.
4. Evaluate test prompts on **SLM + RAG models**.
5. Hold a follow-up meeting on **Thursday** to review progress and next steps.

---

## **Meeting 13**

**Date:** October 31, 2025 (Friday, 12:00 PM EST)

**Attendees:** Amro, Aseel, Banu, Caesar

### Summary

- The originally planned follow-up meeting was postponed due to scheduling conflicts.
- **Amro** presented his **RAG demo** using **Banu’s test prompts** — the model answered most questions correctly but added unnecessary details and struggled with harder ones. Some hallucinations were observed.
- **Caesar** discovered a new, improved distilled model (**MBZUAI/LaMini-Flan-T5-248M**), applied **RAG**, and shared a demo. It performed well on most test prompts except the hard ones.
- The team outlined a **two-week roadmap** focused on **coding and technical tasks**, followed by **repository organization**.

### Action Items

- Prioritize coding tasks now; clean and organize the repository later.
- **Amro:** Continue refining RAG implementation.
- **Caesar:** Test the **CodeCarbon** library on the new model.
- **Banu:** Add a **generative paragraph task** to test prompts and create **three new prompts** for it (for use in the upcoming Google Form).
- **Aseel:** Prepare a draft for the **main README**.
- Team to explore **recursive models** in the coming days.
- Use **Slack** actively for communication and finalize the next meeting date later.
