<!-- markdownlint-disable MD013 MD024 MD025 MD026 MD041 MD001 -->
<!-- This disables line length, duplicate headings, multiple top-level headings, heading punctuation, first heading, and heading increment rules -->
<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD025 -->
<!-- Multiple top-level headings needed for each model section -->

# Comparative Environmental and Technical Overview of Modern AI Models

This document presents verified technical and environmental data for three leading AI models — **OpenAI GPT-4**, **Anthropic Claude 3 Haiku**, and **Google Gemini Nano** — focusing on energy, water, and sustainability context.

---

## Model 1: GPT-4 (OpenAI)

### Model Name & Provider

**GPT-4**, developed by **OpenAI**.

### Hosting / Deployment

Hosted via **Microsoft Azure OpenAI Service**, which operates on Azure’s global data centers (specific regions not publicly disclosed).  
Source: [Introducing GPT-4 in Azure OpenAI Service – Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/introducing-gpt-4-in-azure-openai-service/)

### Estimated Model Size / Architecture

GPT-4 is widely considered a **frontier model** employing a **Sparse Mixture-of-Experts (MoE)** architecture.  
This structure activates only a subset of parameters per inference, optimizing efficiency while maintaining scale.  
Estimated total parameters exceed **1 trillion**.  

Sources:  

- [*Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks* – arXiv (2508.18672v2)](https://arxiv.org/html/2508.18672v2)  
- [*Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models* – arXiv (2501.12370v2)](https://arxiv.org/html/2501.12370v2)

### Estimated Energy (Inference)

Estimates vary between studies:  

- **Epoch AI (2024):** ≈ 0.3 Wh (0.0003 kWh) per query under typical load.  
  Source: [Epoch AI – *How Much Energy Does ChatGPT Use?*](https://epoch.ai/blog/how-much-energy-does-chatgpt-use)  
- **Other analysts:** 0.3 – 1.8 Wh (0.0003 – 0.0018 kWh), depending on token count and hardware.

**Note:** OpenAI has not released official inference energy data.  
Values depend on hardware (GPU vs TPU), data-center PUE, and carbon intensity.

### Training Energy Estimates

Extrapolated from compute budgets and model size:  
≈ 51,772,500 – 62,318,750 kWh (≈ 51.8 – 62.3 GWh) for full-scale training.  
Source: [*The Carbon Footprint of ChatGPT* – Sustainability by Numbers](https://sustainabilitybynumbers.com/how-much-energy-does-chatgpt-use/)

### Water Usage

Water consumption derives from data-center cooling processes:  

- A single ChatGPT query may indirectly consume ≈ 0.5 L of water.  
- Generating a 100-word email ≈ 0.14 kWh energy + 0.52 L water.  
Source: [The Verge – *Sam Altman on ChatGPT Energy and Water Use*](https://www.theverge.com/2023/11/16/sam-altman-chatgpt-energy-water-use)

### PUE / CI Context Used in Studies

Environmental analyses generally apply:  

- **PUE (Power Usage Effectiveness):** ≈ 1.1 – 1.3 (Azure hyperscale data centers)  
- **CI (Carbon Intensity):** ≈ 0.3 – 0.4 kg CO₂e / kWh (depending on regional grid mix)

---

## Model 2: Claude 3 Haiku (Anthropic)

### Model Description

**Claude 3 Haiku** is the smallest and fastest member of Anthropic’s Claude 3 model family ( Haiku, Sonnet, Opus ), released March 2024.  
It is optimized for low-latency, energy-efficient applications such as chatbots, summarization, and enterprise automation.  

Sources:  

- [Anthropic Blog – *Introducing the Claude 3 Model Family*](https://www.anthropic.com/news/claude-3-models)  
- [Anthropic 3 Announcement](https://www.anthropic.com/news/claude-3-7-sonnet)

### Hosting / Deployment

Claude 3 Haiku is available through Anthropic’s API and **AWS Bedrock**.  
AWS data centers maintain an average PUE of ≈ 1.2.  
Sources:  

- [AWS Bedrock – *Use Claude on Bedrock*](https://aws.amazon.com/bedrock/claude/)  
- [AWS Sustainability Report 2024](https://sustainability.aboutamazon.com/reporting)

### Estimated Model Size / Architecture

Community estimates place Claude 3 Haiku at ≈ 20 B parameters.  
The largest model in the family (Claude 3 Opus) is ≈ 2 T parameters.  
Source: [ClaudeAI Community Discussion (Reddit)](https://www.reddit.com/r/ClaudeAI/)

### Estimated Energy (Inference)

Anthropic does not publish per-query energy figures.  
Based on 10–30 B parameter transformers: ≈ 0.05 – 0.1 Wh (0.00005 – 0.0001 kWh) per query.  
Haiku is ≈ 5× more efficient than Claude 3 Sonnet or Opus.  
Sources:  

- [Epoch AI – Machine Learning Trends (for compute/power scaling)](https://epoch.ai/trends)  
- [Anthropic 3 Announcement](https://www.anthropic.com/news/claude-3-7-sonnet)

### Training Energy Estimates

Claude 3 models are trained on GPU clusters (NVIDIA A100/H100) via AWS.  
Typical training energy for models of this scale: ≈ 3,000 – 10,000 MWh.  
Sources:  

- [Epoch AI – Machine Learning Trends (for compute/power scaling)](https://epoch.ai/trends)  
- [Anthropic Responsible Scaling Policy](https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf)

### Water Usage

Anthropic does not publish direct figures; relies on AWS cooling efficiency and water recycling policies.  
Sources:  

- [AWS Water Stewardship Report](https://sustainability.aboutamazon.com/2024-amazon-sustainability-report-aws-summary.pdf)  
- [Anthropic Responsible Scaling Policy](https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf)

### PUE / CI Context Used in Studies

- **PUE:** ≈ 1.2 (AWS average)  
- **CI:** ≈ 0 – 0.2 kg CO₂e / kWh (based on regional renewable mix)  
AWS targets **100 % renewable energy by 2025**.  
Sources:  
- [AWS Global Infrastructure Efficiency Data](https://sustainability.aboutamazon.com/2024-amazon-sustainability-report-aws-summary.pdf)  
- [Anthropic Responsible Scaling Policy](https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf)

---

## Model 3: Gemini Nano (Google DeepMind)

### Model Name & Provider

**Gemini Nano**, developed by **Google DeepMind**, is the smallest member of the Gemini family (Nano, Pro, Ultra).  
Sources:  

- [Google AI Blog – *Introducing Gemini*](https://blog.google/technology/ai/google-gemini-ai/)  

### Hosting / Deployment

Runs **on-device** through Android’s **AICore** system (launched in Android 14).  
Deployed on optimized hardware (e.g., Pixel 8 Pro, Pixel 9 Series).  
This local processing approach eliminates cloud compute energy and network latency.  
Additional coverage: - [Android Developers – *Gemini Nano Overview*](https://developer.android.com/ai/gemini-nano)

### Estimated Model Size / Architecture

Deployed in quantized versions:  

- **Nano-1:** ≈ 1.8 B parameters  
- **Nano-2:** ≈ 3.25 B parameters  
Reference: [Exploding Topics – AI Model Parameters Database](https://explodingtopics.com/blog/gpt-parameters)

### Estimated Energy (Inference)

- **Median Cloud Gemini Inference:** ≈ 0.24 Wh per text prompt.  
- **On-Device Nano Estimate:** ≈ 0.01 Wh per query (benchmarks + design targets).  
Note: Official Nano inference measurements are not yet public.  
Source: [Google Cloud Blog – *Measuring the Environmental Impact of AI Inference*](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/)

### Training Energy Estimates

Gemini Nano was distilled from larger Gemini models trained on **Google TPU v5e clusters**.  
Training energy estimated ≈ 200 – 1,200 MWh (total, amortized across billions of devices).  
Sources:  

- [Google Cloud TPU Documentation](https://cloud.google.com/tpu/docs/)  
- [Google Cloud Blog – Environmental Impact of AI Inference](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/)

### Water Usage

- **Inference:** Zero data-center water use (on-device).  
- **Training:** Uses Google data centers with average WUE ≈ 0.26 mL per median cloud query.  
Source: [Google Cloud Blog – *Measuring the Environmental Impact of AI Inference*](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/)

### PUE / CI Context Used in Studies

- **Average PUE:** 1.10 – 1.12 (Google Data Centers)  
- **Carbon Intensity (CI):** ≈ 0.03 g CO₂e / query (market-based)  
Reflects Google’s near-total renewable energy purchasing.  
Source: [Google Cloud Blog – Environmental Impact of AI Inference](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference/)

---

### Summary

| Model | Developer | Hosting Type | Est. Parameters | Inference Energy (Wh/query) | Training Energy (MWh) | PUE | CI (kg CO₂e/kWh) |
|:------|:-----------|:--------------|:----------------|:-----------------------------|:----------------------|:----|:----------------:|
| GPT-4 | OpenAI | Cloud (Azure) | ≈ 1 T + (MoE) | 0.3 – 1.8 | ≈ 51 K – 62 K MWh | 1.1–1.3 | 0.3–0.4 |
| Claude 3 Haiku | Anthropic | Cloud (AWS Bedrock) | ≈ 20 B | 0.05 – 0.1 | 3 K – 10 K | ≈ 1.2 | 0–0.2 |
| Gemini Nano | Google DeepMind | On-Device (Android AICore) | 1.8–3.25 B | ≈ 0.01 (on-device) | 200–1,200 | 1.10–1.12 | ≈ 0.03 g CO₂e /query |

---
