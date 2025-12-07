<!-- markdownlint-disable MD013 -->
# QwenModel: Qwen 2.5 + RAG + Recursive Editing

This project experiments with the open-sourced model **Qwen 2.5** (2.5B parameters) combined with **Retrieval-Augmented Generation (RAG)** and **recursive editing** to test its performance across different prompt categories from the Apollo 11 dataset.

## Project Structure

* **main.ipynb** – The core notebook where Qwen 2.5 is set up, RAG is integrated, and recursive editing is implemented.
* **output.md** – Contains the final prompts and responses generated through recursive editing, along with tracked energy and CO₂ emission metrics.

## Workflow Overview

### 1. Prompt Setup

The notebook defines three structured prompts for iterative refinement:

* **Draft Prompt** – Produces the initial answer.
* **Critic Prompt** – Analyzes weaknesses in the draft.
* **Refiner Prompt** – Improves the answer based on the critique.

This setup enables controlled recursive editing, especially useful for summarization, creative writing, and paraphrasing.

### 2. RAG Pipeline

* Connected to the Hugging Face API to generate **embeddings**.
* Built a **vector index** from the Apollo 11 dataset.
* Prepared a **retriever** to supply relevant context for Qwen.

### 3. Qwen Integration

A custom function handles:

* Retrieval of context
* Construction of Qwen API calls
* Application of recursive editing logic (3 iterations)

### 4. Energy Tracking

Each query is wrapped with **CodeCarbon** to record:

* CPU usage
* Energy consumption
* CO₂ emissions

All tracked metrics appear in `output.md`.

## Output

The final markdown file contains:

* The prompts used
* Recursive-editing improved final responses
* Per-question energy and emission statistics

## Purpose

This setup provides a compact testing environment to evaluate Qwen 2.5’s performance with RAG and recursive editing, enabling comparison with larger or alternative models.
