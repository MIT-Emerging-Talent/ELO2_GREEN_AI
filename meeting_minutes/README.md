<!-- markdownlint-disable MD013 -->
<!-- Disabled MD013 (Line length) for better readability -->

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

**Timeline:** October 15 – November 6, 2025

With the research framework and scope finalized in Milestone 1, **Milestone 2** focuses on preparing the experimental environment and defining how sustainability metrics will be measured. This phase involves setting up tools such as **CodeCarbon**, **CarbonTracker**, and **Eco2AI** to monitor energy and carbon usage, and exploring **Water Usage Effectiveness (WUE)** datasets from major cloud providers like AWS, Microsoft, and Google.

The team also plans to configure testing environments for small open-source models (e.g., **Mistral**, **LLaMA-2**) using **Hugging Face Transformers**, **PyTorch**, and GPU-enabled platforms such as **Colab**. Another core deliverable is the **experimental design document**, which will outline the metrics (energy, carbon, water, and accuracy), workflows, and methodology diagrams guiding the model evaluation process.

By the end of Milestone 2, the team completed the technical setup, finalized the measurement pipeline, and validated that all tracking tools operate consistently across model types—ensuring a smooth transition into Milestone 3, where full experiments will be executed.

## 📊 Milestone 3 – Model Benchmarking & Data Collection

**Timeline:** November 7 – November 18, 2025

Milestone 3 marks the beginning of the full experimental phase. Using the measurement pipeline and tooling established in Milestone 2, the team runs benchmark tasks on both proprietary and open-source models to collect data on **accuracy** and **environmental impact**. This includes tracking **energy consumption and carbon emissions** for each testing model under consistent test conditions.

During this phase, the team also validates accuracy results on selected reasoning and summarization tasks, investigates irregular outputs, and updates evaluation scripts when needed. Additional observations such as **inference time, token throughput**, and **hardware utilization** are recorded to support later analysis.

By the end of Milestone 3, the project has produced a complete experimental dataset covering sustainability metrics and accuracy scores for all evaluated models, providing a strong foundation for **Milestone 4**, which focuses on human evaluation and qualitative assessment.

## 🧪 Milestone 4 – Human Evaluation & Survey Analysis

**Timeline:** November 19 – ongoing

Milestone 4 centers on incorporating **human judgment** into the benchmarking process. The team prepares a Google Form survey designed to compare model outputs side-by-side. Participants evaluate **clarity, coherence, informativeness, factuality,** and **overall preference**.

Once responses are collected, the team analyzes the results by aggregating scores, assessing agreement among reviewers, and comparing human preferences with automated accuracy metrics from earlier milestones. This helps identify where quantitative and qualitative assessments align or diverge.

By the end of Milestone 4, the project integrates the human evaluation results into the broader dataset, enabling a more nuanced understanding of model performance and preparing the groundwork for **Milestone 5**.
