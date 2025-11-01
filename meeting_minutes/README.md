<!-- markdownlint-disable MD013 -->

# 🗓️ Meeting Minutes – Environmental Impact of AI Models

This directory documents the weekly progress and decision-making process for the research project on **the environmental and performance trade-offs between large proprietary and small open-source AI models**.

Each meeting entry outlines team discussions, feedback, experimental progress, and assigned tasks across project milestones.

## 🧭 Milestone 1 – Scoping & Research Question Refinement

**Timeline:** September 27 – October 14, 2025

The first milestone focused on refining the research direction and defining a clear, measurable problem within **Green AI**. After exploring various AI-related topics, the team finalized the project title — **“Green AI Benchmarking of Foundation Models”** — and the research question:

> Can open-source LLMs match the accuracy of commercial models while reducing environmental impact?
>

Key progress included reviewing literature on energy, carbon, and water use in AI systems, selecting benchmark tasks (**reasoning** and **summarization**), and identifying evaluation metrics for **accuracy** and **environmental footprint**. The team also chose comparison models (**GPT-4** and **Mistral-7B**), created shared documentation, and distributed responsibilities among members.

By the end of Milestone 1, the project established its scope, research framework, and collaborative infrastructure, setting the stage for **Milestone 2**, focused on tool setup and metric calibration.

## ⚙️ Milestone 2 – Tool Setup & Experiment Planning

**Timeline:** October 15 – Ongoing

With the research framework and scope finalized in Milestone 1, **Milestone 2** focuses on preparing the experimental environment and defining how sustainability metrics will be measured. This phase involves setting up tools such as **CodeCarbon**, **CarbonTracker**, and **Eco2AI** to monitor energy and carbon usage, and exploring **Water Usage Effectiveness (WUE)** datasets from major cloud providers like AWS, Microsoft, and Google.

The team also plans to configure testing environments for small open-source models (e.g., **Mistral**, **LLaMA-2**) using **Hugging Face Transformers**, **PyTorch**, and GPU-enabled platforms such as **Colab**. Another core deliverable is the **experimental design document**, which will outline the metrics (energy, carbon, water, and accuracy), workflows, and methodology diagrams guiding the model evaluation process.

This milestone sets the foundation for **Milestone 3**, where real model experiments and energy tracking will begin.
