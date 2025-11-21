<!-- markdownlint-disable MD024 -->
<!-- Disabled MD024 (Multiple headings with the same content) rule
because repeated headings (Summary, Action Items) are intentionally used
across multiple sections for structural clarity.
-->
# Milestone 3 Meeting Minutes

## Meeting 14

**Date:** November 7, 2025 (Friday, 3:00 PM EST)  
**Attendees:** Amro, Aseel, Caesar, Safia, Banu

### Summary

- **Amro** presented the latest progress on his work with **Mistral 7B** integrated
  with **RAG**. The model showed improved accuracy and more contextually aligned
  responses. Although latency increased (64–>152), it was considered acceptable
  given the model’s size and the team’s limited compute.
- **Caesar** tested **CodeCarbon** and the **Emissions Tracker** and reported
  inconsistent results. Amro suggested trying an **offline version of
  CodeCarbon**.
- **Safia** continued experiments with **SLM (TinyLlama) + RAG** and will begin
  testing the **unified test prompts** next.
- Based on **Evan’s feedback**, the team decided to **evaluate outputs rather
  than models**. **Python evaluation libraries** produced weak results, so the
  team will use a **hybrid evaluation**: AI-based plus human-based.
- The previously discussed **Google Form** idea received positive feedback from
  Evan and will serve as a **human-based evaluation tool**.
- The **initial Google Form structure** was outlined:
  - Intro section with a short project description.
  - Following sections will show **model-generated texts** (open-source and
    commercial) in **random order**.
  - Participants will **guess the source** and rate clarity, relevance, and
    accuracy on a **1–5 scale**.
  - Per Evan’s suggestion, the **target audience** should be **diverse and
    multicultural**, so the form will be shared in the **cohort group**.

### Action Items

- The team aims to **meet again tomorrow**, depending on availability.
- The **recursive model approach** will be **re-evaluated**.
- **README files** will be prepared for all selected models in the repository.
- Work on the **Google Form** will begin, targeting a **November 15**
  publication date.

### Future Work

- Once published, the form will remain open for **two weeks** for response
  collection and analysis.
- In the **first week of December (final week of ELO2)**, the data will be
  analyzed manually and used to write the **research article**.

---

## Meeting 15

**Date:** November 9, 2025 (Sunday, 2:30 PM EST)  
**Attendees:** Amro, Aseel, Banu, Caesar, Reem, Safia

### Summary

- Due to scheduling conflicts, the meeting planned for Saturday was held today.
- A brief recap of Meeting 14 was provided.
- The team reviewed the general work plan and discussed the three models under
  testing.
- Caesar reported that the CodeCarbon issue was resolved using Amro’s prior
  suggestion. His distilled model initially failed on creative tasks.
- Amro recommended refining prompts. After adjusting guidance, temperature, and
  other parameters live during the meeting, Caesar’s model improved and produced
  two correct creative outputs out of three.
- Amro shared that Mistral 7B also improved in creative tasks after adopting the
  new guidance prompts.
- Reem presented her proposal to modify the recursive reasoning method into a
  **recursive editing** approach. The process involves:
  - One model generating a draft.
  - A feedback provider model reviewing it.
  - A refinement cycle combining draft and feedback.
  - Iteration until quality is high or a limit is reached.
  - Evaluation criteria vary by task.
- The current model lineup:
  - **Caesar:** LaMini (distilled open-source) + RAG
  - **Amro:** Mistral 7B + RAG
  - **Safia:** TinyLlama (SLM) + RAG
- The team agreed to apply the recursive editing framework to Safia’s model as
  the **fourth setup**.
- Human evaluation plans were discussed, focusing on participant-based accuracy
  and quality assessment. Final testing will be completed this week.

### Action Items

- Reem, Aseel, and Banu will implement **recursive editing** on the small model
  (TinyLlama + RAG + Recursive Editing).
- Caesar will apply recursive editing to the distilled model.
- Amro will test the method on Mistral.
- All members will prepare outputs and documentation before **Friday,
  November 14**.
- Friday’s meeting will review results and prepare the **Google Form**, which
  will be finalized on **Saturday, November 15**.

---

## Meeting 16

**Date:** November 14, 2025 (Thursday, 2:30 PM EST)  
**Attendees:** Amro, Aseel, Banu, Caesar, Reem, Safia

### Summary

- After asynchronous discussions, the team determined that **TinyLlama is not
  suitable** for recursive editing. The team switched to **Microsoft’s Phi-3**,
  but it was removed from Hugging Face. New SLMs were selected:
  **Reem → Microsoft Qwen**, **Aseel → Google Gemma**.
- **Caesar** reported **token limitation issues** during recursive editing.
- **Reem** shared updates on recursive cycle experiments and issues related to
  **context window tuning** and **token allocation**.
- **Amro** proposed using **specialized small models** for focused tasks
  (critique and refinement) instead of relying on large models. Retrieval and
  initial generation could be done by the user, while a small model refines the
  text.
- Technical discussions included context window tuning, max-token adjustments,
  and restoring capacity by splitting loops across notebook cells.
- The team reaffirmed that **GPUs outperform CPUs** significantly.
- The team began discussing the **Google Form methodology**, deciding to use
  **vague model descriptions** to avoid bias.

### Action Items

- Team will **meet again tomorrow at 2:30 PM EST** to finalize remaining work.
- **Safia and Banu** will develop the **Google Form** after the meeting and send
  it to Evan by Monday.
- **Reem and Aseel** will continue working on their models.
- All members must finalize **implementations and documentation**.

---

## Meeting 17

**Date:** November 15, 2025 (Wednesday, 2:30 PM EST)  
**Attendees:** Amro, Aseel, Caesar, Reem, Banu

### Summary

- **Aseel** confirmed she pushed her model and related work earlier today.
- **Reem** reported that she is finalizing outputs for upload.
- **Amro** improved his model documentation for clarity and organization.
- The team discussed the **structure of the Google Form**, focusing on whether
  to include only **open-source model outputs** or also **commercial outputs**.
  The group will seek **Evan’s guidance** before finalizing the structure.

### Action Items

- **Create the first Google Form draft tomorrow** and prepare to present it on
  Monday.
- **Publish the final form on Monday** after incorporating Evan’s feedback.
- **Finalize all model documentation** and begin reorganizing the repository.
