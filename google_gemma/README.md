# Project: “Green AI Automated RAG Testing with Gemma”

## Overview

We built an interactive retrieval-augmented generation (RAG) pipeline using the
open-weight model *Gemma 2-2b* by Google and applied it to a standardized text
and prompt set derived from the Apollo 11 lunar landing.

**The goal:**

* evaluate summarisation, reasoning, retrieval, paraphrasing, and creative tasks
in a controlled, reproducible way — logging both answer quality and local
sustainability metrics (energy/carbon emissions) via CodeCarbon.

## Model

**Model ID:** `google/gemma-2-2b-it` (Hugging Face)

**Key attributes:**

* Open-weight decoder-only model trained by Google
* Supports text-generation and conversational usage
* Suitable for research, summarisation, reasoning, and retrieval tasks
* Lightweight enough for deployment on modest compute resources

Model link: [https://huggingface.co/google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)

## What We Did

1. Created a source document (`source.txt`) using ~1,400 words of selected
   Wikipedia excerpts on Apollo 11.
2. Defined a set of 21 standardised prompts spanning five categories:
   summarisation, reasoning, RAG (fact retrieval), paraphrasing, and creative
   generation.
3. Built a document retrieval component using sentence-transformers to chunk
   the document and select top-k relevant chunks per query.
4. Developed an interactive notebook workflow that:

   * Accepts a question at runtime
   * Runs RAG → Draft → Critic → Refiner cycles using Gemma
   * Tracks local CPU/GPU energy usage and CO₂ emissions with CodeCarbon
   * Logs each question, answer, timestamp, and emissions to a single
     append-only log file
5. Logged runtime latency and emissions per query for performance and
   sustainability insights.

## How to Use

1. Clone the repository:

   ```bash
   git clone <YOUR_REPO_URL>
   cd your_repo_folder
   ```

2. Place your `source.txt` into `./data/`.

3. Add your Hugging Face API key in the config cell.

4. Run the notebook setup cells, then use the interactive prompt cell to ask
   questions.

## Why This Matters

* **Reproducibility** — fixed source text and prompt set allow consistent
  evaluation across models.
* **Efficiency vs. Accuracy** — emissions are logged alongside outputs to
  explore trade-offs between model performance and energy cost.
* **Accessibility** — uses an open model and standard Python tools, making
  research on small language models feasible even on laptops.
