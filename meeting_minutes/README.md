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

With the research framework and scope finalized in Milestone 1, **Milestone 2** focused on preparing the experimental environment and defining how sustainability metrics were be measured. This phase involved setting up tools such as **CodeCarbon**, **CarbonTracker**, and **Eco2AI** to monitor energy and carbon usage, and exploring **Water Usage Effectiveness (WUE)** datasets from major cloud providers like AWS, Microsoft, and Google.

The team also planned to configure testing environments for small open-source models (e.g., **Mistral**, **LLaMA-2**) using **Hugging Face Transformers**, **PyTorch**, and GPU-enabled platforms such as **Colab**. Another core deliverable was the **experimental design document**, which was outlining the metrics (energy, carbon, water, and accuracy), workflows, and methodology diagrams guiding the model evaluation process.

By the end of Milestone 2, the team completed the technical setup, finalized the measurement pipeline, and validated that all tracking tools operate consistently across model types—ensuring a smooth transition into Milestone 3, where full experiments will be executed.

## 📊 Milestone 3 – Model Benchmarking & Data Collection

**Timeline:** November 7 – November 18, 2025

Milestone 3 marked the beginning of the full experimental phase. Using the measurement pipeline and tooling established in Milestone 2, the team ran benchmark tasks on both proprietary and open-source models to collect data on **accuracy** and **environmental impact**. This included tracking **energy consumption and carbon emissions** for each testing model under consistent test conditions.

During this phase, the team also validated accuracy results on selected reasoning and summarization tasks, investigated irregular outputs, and updated evaluation scripts when needed. Additional observations such as **inference time, token throughput**, and **hardware utilization** were recorded to support later analysis.

By the end of Milestone 3, the project has produced a complete experimental dataset covering sustainability metrics and accuracy scores for all evaluated models, providing a strong foundation for **Milestone 4**, which focuses on human evaluation and qualitative assessment.

## 🧪 Milestone 4 – Human Evaluation & Survey Analysis

**Timeline:** November 19 – December 3, 2025

Milestone 4 centered on incorporating **human judgment** into the benchmarking process and concluded successfully. The team prepared and published a Google Form survey to compare model outputs side-by-side, and participants evaluated **clarity, coherence, informativeness, factuality,** and **overall preference**.

To improve participation and focus, the survey scope was refined to eight questions across four categories—**Reasoning, Summarization, Creative Writing,** and **Paraphrasing**—and the **Retrieval/RAG** category was excluded due to its emphasis on factual lookup rather than generative quality.

Once responses were collected, the team analyzed the results by aggregating scores, assessing agreement among reviewers, and comparing human preferences. Initial insights, including distributional patterns and respondent demographics, were reviewed via Google Forms visualizations, and notable alignments and divergences between human judgments and quantitative metrics were documented to guide interpretation in the final analysis.

By the end of Milestone 4, the project integrated the human evaluation results into the broader dataset, consolidated the confirmed question set and model pairings, and prepared materials for downstream reporting. This provided a more nuanced understanding of model performance, completing the human evaluation phase and setting up the transition into **Milestone 5**.

## 📣 Milestone 5 – Communication of Results & Final Presentation

**Timeline:** December 4 – ongoing

Milestone 5 focuses on packaging and communicating the project’s findings while completing the final presentation and releasing the full set of artifacts. The team is synthesizing human evaluation results to produce a coherent analysis narrative, drafting and editing the presentation and article for publication, and finalizing an infographic and visual summary that will be embedded in both the article and the presentation.

In parallel, the repository is being cleaned and organized to publish the code, data, and analysis notebooks with clear usage notes and data access instructions. Everything will be finalized on December 7.
