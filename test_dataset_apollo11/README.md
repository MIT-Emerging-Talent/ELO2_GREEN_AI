# 🚀 Apollo 11 Test Dataset

## 🌕 Overview

This is the unified test dataset for comparing different AI models (commercial,
distilled, SLM, and RAG systems) in the ELO2 - Green AI project.

The dataset consists of selected passages from Wikipedia's Apollo 11 article,
accompanied by 21 standardized prompts testing summarization, reasoning,
retrieval, paraphrasing, and creative generation capabilities.

---

## 📂 Dataset Contents

- **[README.md][readme]** - This file (overview and instructions)  
- **[source_text.txt][source]** - Apollo 11 excerpted text
(~1,400 words, plain text)  
- **[test_prompts.md][prompts]** - All test prompts (readable format)  
- **[test_data.json][json]** - Complete dataset (structured format for automated
  testing)
- **[RATIONALE.md][rationale]** - Detailed explanation of selection decisions

📌 **Process documentation:** For background on dataset creation decisions and
team discussions, see the **[team briefing](https://docs.google.com/document/d/1jAE2Y2BJDx014MAXCxyH0-2EgieL_tCxCEeMK4VWBNQ/edit?usp=sharing)**

[readme]: /test_dataset_apollo11/README.md  
[source]: /test_dataset_apollo11/source_text.txt  
[prompts]: /test_dataset_apollo11/test_prompts.md  
[json]: /test_dataset_apollo11/test_data.json  
[rationale]: /test_dataset_apollo11/RATIONALE.md

---

## 📄 Source & License

**Source:** Wikipedia - Apollo 11 article  
**URL:** <https://en.wikipedia.org/wiki/Apollo_11>  
**Link:**<https://en.wikipedia.org/w/index.php?title=Apollo_11&oldid=1252473845>
**Revision ID:** 1252473845 (Wikipedia internal revision number)  
**Date Accessed:** October 22, 2025  
**Sections:** Excerpted passages from "Lunar landing" and "Lunar surface
operations"  
**Word Count:** ~1,400 words  
**Language:** English

**License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0)

- ✅ Content can be used freely for research
- ✅ Wikipedia must be attributed as the source
- ✅ Derivative works must be shared under the same license

**Attribution:** "Apollo 11" by Wikipedia contributors, licensed under CC BY-SA 3.0

**Text Structure:** Selected passages from Wikipedia sections.

- Individual sentences are unchanged; some paragraphs omitted for length management.
- Complete original sections total ~3,800 words; excerpted to ~1,400 words for
practical testing while maintaining all information necessary for the 21 test prompts.

📌 See [source_text.txt][source] for the complete excerpted text.

---

## 🎯 Selection Rationale

- ✅ **Practical length** - ~1,400 words manageable for all model types including
distilled models with standard chunking
- ✅ **Rich in specific details** - Ideal for RAG testing (times, names, numbers,
technical terms)
- ✅ **Multiple complexity levels** - Both simple recall and complex reasoning can
be tested
- ✅ **Narrative structure** - Clear sequence from descent through surface
activities
- ✅ **All prompts answerable** - 21 test prompts verified to work with selected
passages

The excerpts cover the dramatic descent and landing sequence, followed by
moonwalk activities, ensuring comprehensive testing across summarization,
reasoning, RAG, paraphrasing and creative generation tasks.

📌 See [RATIONALE.md][rationale] for detailed selection methodology.

---

## 📝 Test Structure

The test includes **21 standardized prompts** distributed across **five categories**.
In addition, a **Master Instruction** and **task-specific guidance prompts** are
provided to ensure consistency and clarity across all tasks.

### Prompt Delivery Overview

The test follows this sequence:  

**1. The Master Instruction** is used **once at the beginning** of the test.
**2.** Before each category, a **task-specific guidance prompt** clarifies how
the model should approach that task type (e.g., reasoning, summarization, retrieval).
**3.** Then, the **individual prompts for that category** are presented in order
of increasing difficulty.

### Prompt Categories

#### 1. Summarization (5 prompts)  

Tests model's ability to condense and extract key information.

**Difficulty:** Easy → Medium → Hard  
**Examples:** Main events, challenges faced, activities performed, equipment deployed

#### 2. Reasoning (5 prompts)  

Tests model's ability to analyze, infer, and make connections.

**Types:** Causal reasoning, hypothetical scenarios, interpretation,
deep analysis  
**Examples:** Why did computer alarms occur? What if Armstrong hadn't taken
manual control? What does Margaret Hamilton's statement reveal?

#### 3. RAG – Retrieval (5 prompts)  

Tests model's ability to retrieve specific information from source text.

**Types:** Times, quotes, numbers, lists, complex multi-part facts  
**Examples:** Landing time? Material collected? Scientific instruments deployed?

#### 4. Paraphrasing (3 prompts)  

Tests model's ability to restate information in its own words.

**Difficulty:** Easy → Medium  
**Examples:** Describe computer alarms, Armstrong’s teamwork, or sample collection.

#### 5. Creative Generation (3 prompts)  

Tests model's interpretive and imaginative capabilities.

**Difficulty:** Easy → Medium  
**Examples:** Imagine being in Mission Control. What does landing show about courage?
How did it change Earth?

📌 See [test_prompts.md][prompts] for the readable version with full prompt texts,
or [test_data.json][json] for its structured data version.

---

## 🔧 How to Use

### General Instructions

- **All 21 prompts** should be tested across all models to ensure a fair comparison.
- The **Master Instruction** and any **task-specific guidance prompts** should
  be applied as described in the Test Structure section.
- Some prompts can be more challenging for smaller models,
but attempting all prompts provides comprehensive evaluation data.

**Testing Protocol:**

**1.** Use the source text from **[source_text.txt][source]**
exactly as provided
**2.** Use all prompts from **[test_prompts.md][prompts]** without
modification
**3.** *(Optional)* Use **[test_data.json][json]** for automated or scripted
   testing workflows  
**4.** Record responses for each prompt with model configuration details  
**5.** Note any errors, failures, or unusual behaviors

---

## 📊 Evaluation

For each prompt, record:

**1. Accuracy** - Is the answer factually correct?  
**2. Completeness** - Are all key points covered?  
**3. Specificity** - Are specific details included (times, names, numbers)?  
**4. Reasoning Quality** - Is the logic sound and well-supported?  
**5. Paraphrasing Quality** - Is information reworded(not copied)  
while maintaining accuracy?
**6. Creative Generation Quality** - Is the response coherent, relevant, and text-inspired?
**7. Instruction Following** - Does the model follow the master or task-spesific
instructions (no source mentions, concise, natural)?

**Note:** Creative generation prompts have no single correct answer. Evaluate
based on coherence, relevance to text, and quality of reasoning.  
Maintain consistent evaluation criteria across all models for fair comparison.

---

## ⚠️ Guidelines

**Critical Rules:**

- **DO NOT modify** the source text
- **DO NOT modify** the prompts
- **DO record** all test configurations (model version, parameters, hardware)
- **DO note** any failures as "No response" or "Error" with details

**Technical Notes:**

- For RAG systems: Load the source text into the database and verify indexing
  before testing
- For models with token limits: Chunking may be required
- Environment: Use consistent hardware and settings when possible
- Environmental measurements: Use standardized protocols

---

## 📖 How to Cite This Dataset

When referencing this dataset in reports or publications:

> Apollo 11 Test Dataset: Excerpted passages from Wikipedia's "Apollo 11" article
> (Revision 1252473845, accessed October 22, 2025), licensed under CC BY-SA 3.0.
> Available at: <https://en.wikipedia.org/wiki/Apollo_11>

---

*For questions or issues, please contact the project team.  
Good luck with testing!* 🚀
