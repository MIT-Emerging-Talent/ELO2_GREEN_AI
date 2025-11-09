# Apollo 11 Model Evaluation Suite

This document contains **21 standardized test prompts** for evaluating language
models using the Apollo 11 lunar landing context.

Please follow the instructions in order:
first **Master Prompt**,  
then **task-specific instructions**,  
and then **the prompts for that category**.

---

## Master Prompt

> You are an expert assistant.  
> Answer only using the provided context.  
> Keep answers clear, concise, and natural.  
> Do not provide unnecessary details or repeat information.  
> Do not mention or refer to the document, context, or data source.

---

## 21 Standardized Test Prompts

This section contains all test prompts organized by task category.

### Summarization Tasks (5 prompts)

> **Task Instruction:**  
> Summarize or describe information clearly and concisely.

#### Prompt 1 (Easy)  

Summarize the main events during the Apollo 11 lunar landing in 3 sentences.

#### Prompt 2 (Easy)  

What were the main challenges Armstrong faced while landing the Eagle?

#### Prompt 3 (Medium)  

Describe the activities the astronauts performed on the lunar surface.

#### Prompt 4 (Medium)  

Explain what scientific equipment the astronauts deployed on the Moon.

#### Prompt 5 (Hard)  

Compare the planned timeline for the lunar surface operations with what actually
happened.

---

### Reasoning Tasks (5 prompts)

> **Task Instruction:**  
> Provide short, well-structured answers (2–5 sentences).  
> Use only logical reasoning.  
> Do not add assumptions or outside facts.

#### Prompt 6 (Easy)  

Why did the computer alarms (1201 and 1202) occur during the descent?

#### Prompt 7 (Medium)  

What would have happened if Armstrong had not taken manual control during the landing?

#### Prompt 8 (Medium)  

Why did Armstrong's famous quote become controversial?

#### Prompt 9 (Hard)  

Analyze how the fuel situation during landing reflects the risk management challenges
of the mission.

#### Prompt 10 (Hard)  

Based on the text, what does Margaret Hamilton's statement reveal about the Apollo
Guidance Computer's design philosophy?

---

### RAG Tasks (5 prompts)

> **Task Instruction:**  
> Provide precise and direct answers using only the given context.  
> Avoid explanation unless explicitly requested.

#### Prompt 11 (Easy)  

At what time (UTC) did Eagle land on the Moon?

#### Prompt 12 (Easy)  

How much lunar material did the astronauts collect?

#### Prompt 13 (Medium)  

What was Armstrong's famous first words when stepping on the Moon?

#### Prompt 14 (Medium)  

What scientific instruments were included in the EASEP package?

#### Prompt 15 (Hard)  

How much usable fuel remained when Eagle landed, and how many seconds of powered
flight did this represent?

**Expected Answers for RAG:**  

- **Prompt 11:** 20:17:40 UTC on July 20, 1969  
- **Prompt 12:** 21.55 kilograms (47.5 lb)  
- **Prompt 13:** "That's one small step for [a] man, one giant leap for mankind"
- **Prompt 14:** Passive Seismic Experiment Package and retroreflector array
  (for lunar laser ranging experiment)  
- **Prompt 15:** 216 pounds (98 kg); estimated 25 seconds according to initial data,
  but post-mission analysis showed closer to 50 seconds

---

### Paraphrasing Tasks (3 prompts)

> **Task Instruction:**  
> Rewrite the given information in your own words.  
> Preserve meaning and tone without copying phrases directly.  
> The output should read naturally like an original paragraph.

#### Prompt 16 (Easy)  

In your own words, describe what happened when the computer alarms appeared during
the landing.

#### Prompt 17 (Medium)  

Explain how Armstrong's decisions, actions, and teamwork during the descent contributed
to the mission's success.

#### Prompt 18 (Medium)  

Describe how the astronauts collected and handled Moon samples using your own words.

---

### Creative Generation Tasks (3 prompts)

> **Task Instruction:**  
> Use the context as inspiration, but do not copy it.  
> Expand or interpret the ideas creatively, producing a short paragraph.  
> Keep the tone natural and imaginative, as if writing your own reflection.

#### Prompt 19 (Easy)  

Imagine being one of the people in Mission Control. How would you feel while
watching the landing?

#### Prompt 20 (Medium)  

Write a short paragraph about what the Moon landing might have shown about human
courage.

#### Prompt 21 (Medium)  

Describe how life on Earth might have changed after people saw the first Moon landing.
