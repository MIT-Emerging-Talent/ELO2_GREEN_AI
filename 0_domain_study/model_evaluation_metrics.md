# Model Testing Metrics

|Skill Type (Task)|What It Tests|Example Dataset|Metric to Measure Accuracy|
|-----------------|-------------|---------------|--------------------------|
|Reasoning / Logic|Mathematical reasoning|GSM8K|(correct answers / total)|
|Commonsense QA|Everyday reasoning and knowledge|PIQA, BoolQ|Accuracy|
|Summarization|condense information|CNN/DailyMail, XSum|ROUGE-L, BERTScore|
|Code Generation|Logical structure|HumanEval-lite, MBPP|Pass@k|

## Datasets

### GSM8K(Grade School Math 8K)

It is a dataset of 8.5K high quality linguistically diverse
grade school math word problems. The dataset was created to support the task
of question answering on basic mathematical problems that require multi-step
reasoning.

### BoolQ

It is a question answering dataset for yes/no questions containing
15942 examples. These questions are naturally occurring ---they are
generated in unprompted and unconstrained settings.

### PIQA

This dataset introduces the task of physical commonsense reasoning and a
corresponding benchmark dataset Physical Interaction: Question Answering
or PIQA.

### Extreme Summarization (XSum) Dataset

There are three features:
document: Input news article.
summary: One sentence summary of the article.
id: BBC ID of the article.

### The CNN / DailyMail Dataset

It is an English-language dataset containing just over
300k unique news articles as written by journalists at CNN and the Daily Mail.
he current version supports both extractive and abstractive summarization.
The HumanEval dataset released by OpenAI includes 164 programming problems
with a function sig- nature, docstring, body, and several unit tests.
They were handwritten to ensure not to be included in the training
set of code generation models.

### MBPP

The benchmark consists of around 1,000 crowd-sourced Python programming
problems, designed to be solvable by entry level programmers, covering
programming fundamentals, standard library functionality, and so on.
Each problem consists of a task description,code solution and 3 automated
test cases.

## Metrics

### Pass@1

The percentage of problems for which the model’s first generated solution
passes all tests.

### BERTScore

It measures how similar two pieces of text are in meaning, not just in word
overlap. It uses BERT embeddings (or similar transformer embeddings) to
compare the semantic content of the generated text and the reference text.

### ROUGE, or Recall-Oriented Understudy for Gisting Evaluation

It is a set of metrics and a software package used for evaluating automatic
summarization and machine translation software in natural language processing.
The metrics compare an automatically produced summary or translation against
a reference or a set of references (human-produced) summary or translation.
