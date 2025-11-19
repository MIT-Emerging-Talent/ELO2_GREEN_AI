# Commercial Models: The Crisis of AI Environmental Visibility

The environmental impact of Large Language Models (LLMs) has transitioned from
an esoteric concern to a critical research priority. While early studies focused
primarily on the energy cost of the massive **training phase** (e.g., GPT-4
training estimates: $\approx 51.8 \text{ – } 62.3 \text{ GWh}$) [Source: Sustainability
by Numbers], recent, rigorous analyses—such as the landmark benchmarking paper
*"How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM
Inference"* (Jegham et al., 2025)—have confirmed two major points:

* **Inference Dominance:** The energy consumed during **inference**
* (running the model
for every user query) is increasingly the dominant contributor to an LLM's total
lifecycle environmental footprint due to global scale [Source: Google Cloud Blog].
* **Divergent Reporting:** LLM energy reporting is highly unstable. As
demonstrated by the benchmarking paper, resource consumption can vary by over
**70 times** between the most and least efficient models for an equivalent task.
Furthermore, consumption figures depend not just on model size, but profoundly
on **deployment infrastructure** (PUE, regional carbon intensity) [Source: AWS
Sustainability Report] and **methodology** (batch size, token length, hardware
generation) [Source: Optimal Sparsity of MoE, arXiv]. This divergence leads to
figures where one study reports less consumption (e.g., Epoch AI's $0.3 \text{ Wh}$
per query) [Source: Epoch AI], while another (using different infrastructure
assumptions) reports significantly more.

---

## Our Research Intervention

This critical lack of standardized, reliable environmental data creates an
**eco-efficiency paradox**: we cannot definitively prove which models are
sustainable without standardized measurements, but the required performance
trade-offs often push users toward the most power-hungry frontier models (e.g.,
GPT-4's high capability, estimated at $0.3 \text{ – } 1.8 \text{ Wh}$ per query)
[Source: The Verge].

This project addresses this paradox with an **interventionist approach**.
Rather than
simply measuring existing systems, our research question directly investigates
whether we can *engineer* open-source models to definitively close the gap in the
efficiency balance:

> **Research Question:** **Can open-source language models, enhanced with
optimization techniques such as recursive editing and distillation, become
environmentally and functionally viable alternatives to commercial models?**

We hypothesize that by applying resource-saving techniques (e.g., **distillation**
to compress model size and **recursive editing** to refine output with minimal
re-computation), we can achieve an **eco-efficiency score** that consistently
demonstrates their viability as a sustainable alternative, driving adoption of
open-source models over proprietary, resource-intensive solutions.
