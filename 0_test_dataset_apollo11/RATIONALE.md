# Rationale for Text Selection

## Overview  

Excerpted passages (~1,400 words) from Wikipedia’s Apollo 11 “Lunar landing”
and “Lunar surface operations” sections were selected as the unified test
dataset for the ELO2 - Green AI project.

---

## Why Apollo 11?  

**Universal Knowledge:**

All major commercial models (GPT-4, Claude, Gemini) have Apollo 11 in their
training data, enabling fair comparison with and without RAG.

**Rich Factual Content:**

Dense with verifiable facts ideal for RAG testing— timestamps (20:17:40 UTC),
numbers (216 lbs fuel, 21.55 kg samples), names (Armstrong, Aldrin, Hamilton),
and technical terms (LGC, PLSS, EASEP).

**Accessibility:**

Wikipedia content is freely available, properly licensed (CC BY-SA 3.0), and stable
via permanent links.

**Appropriate Length:**

Complete sections total ~3,800 words; excerpted to ~1,400 words—substantial for
evaluation yet processable by smaller models on standard hardware. This length
aligns with standard benchmarks:

- Summarization tasks typically use 500-2,000 words,
- QA benchmarks 300-1,500 words,
- RAG evaluations 1,000-3,000 words (Rajpurkar et al., 2016; Hermann et al., 2015).

The excerpted length balances comprehensiveness with practical testability.

---

## Why These Excerpted Passages?  

![image](images/test-selection.png)

**Continuous Narrative:**

Selected passages flow from descent through surface activities, forming a natural
story arc ideal for summarization tasks requiring temporal understanding.  

**Balanced Complexity:**  

- Simple facts (times, names, quotes) suitable for smaller and distilled models
- Complex elements (technical problems, decision-making, procedures) challenging
  for all models

**Optimal for RAG:**

Dense with retrievable facts across categories—times, quantities, names, equipment,quotes.

**Reasoning Opportunities:**

Supports causal (Why?), hypothetical (What if?), interpretive (What does X reveal?),
and analytical reasoning.

**Verified Coverage:**

All 21 test prompts confirmed answerable with excerpted passages through
preliminary testing.

**Length Management:**

Complete sections (~3,800 words) would require extensive chunking for distilled models
with limited token capacity. Excerpted passages (~1,400 words) are more manageable
while maintaining comprehensive content for all test scenarios.

---

## Alignment with Project Goals  

**Fair Comparison:**  

- Commercial models tested on likely training data  
- RAG systems given the same information  
- All models evaluated on identical input
  
**Reproducibility:**

Permanent Wikipedia link, documented excerpt selections, license documentation.

**Why Not Other Approaches?**  

- Entire Wikipedia article (all sections)?
  Too long (~10,000+ words)—exceeds processing capacity of smaller models,
  impractical for manual verification.  
- Self-written summary?
  Custom summaries cannot be reproduced by others and raise objectivity concerns
  plus potential copyright issues.  
- Multiple unrelated passages?
  Disconnected excerpts (e.g., Apollo 11 + climate change) break narrative flow,
  prevent reasoning questions requiring connected context.  
- Technical manuals or engineering documents?
  NASA reports are too specialized, likely absent from training data, and limit
  question diversity to technical retrieval.  
- Complete sections without excerpting?
  While more comprehensive, ~3,800 words presents practical challenges for smaller
  models and extends testing time. Excerpting maintains essential information  
  while improving testability across architectures.

---

## Excerpt Selection Methodology  

**From “Lunar landing” section:**  

- Descent problems and trajectory issues  
- Computer alarms (1201, 1202) and Margaret Hamilton’s explanation  
- Manual landing sequence with fuel concerns  
- Landing confirmation moment  

**From “Lunar surface operations” section:**  

- EVA preparation and first step  
- Armstrong’s famous quote and its controversy  
- Surface activities and movement  
- Flag planting and Nixon communication  
- Scientific equipment deployment (EASEP)  
- Sample collection activities  
- Return to lunar module

**Omitted content:**  

- Extended technical explanations of radar systems  
- Detailed crew dialogue transcripts  
- Some procedural minutiae  

**Selection criteria:**  

- Information density for prompts  
- Narrative continuity  
- Factual richness for RAG tasks  
- Reasoning opportunities  

---

## Limitations  

**Excerpt nature:**

Using selected passages rather than complete sections reduces some contextual richness,
though all test prompts remain fully answerable.  

**Single domain:**

Results may not generalize beyond this topic.  

- *Acknowledgment:* This is a focused benchmark within defined scope.

---

## Conclusion  

The excerpted passages from *“Lunar landing”* and *“Lunar surface operations”*
sections provide:  

✅ Practical content for all model types  
✅ Reproducibility through permanent links and documented selections  
✅ Balance of factual density and narrative coherence  
✅ Support for diverse question types  
✅ Academic integrity through proper licensing and attribution  
✅ Alignment with Green AI benchmarking objectives  

This selection enables fair, transparent comparison of AI model accuracy and environmental
efficiency while maintaining practical testability on available hardware.

---

## References  

**Hermann, K. M., Kociský, T., Grefenstette, E., Espeholt, L., Kay, W., Suleyman,
M.,& Blunsom, P. (2015).**
*Teaching Machines to Read and Comprehend.*  
*Advances in Neural Information Processing Systems, 28.*  
[arXiv:1506.03340](https://arxiv.org/abs/1506.03340)  

**Rajpurkar, P., Zhang, J., Lopyrev, K., & Liang, P. (2016).**
*SQuAD: 100,000+ Questions for Machine Comprehension of Text.*  
*Proceedings of the 2016 Conference on Empirical Methods in Natural Language
Processing (EMNLP), pp. 2383–2392.*  
[ACL Anthology D16-1264](https://aclanthology.org/D16-1264/)  
