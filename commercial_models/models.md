# Model 1: GPT-4 (OpenAI)

## Model Name and Provider

**GPT-4**, developed by **OpenAI**.

### Hosting and Deployment

Hosted via **Microsoft Azure OpenAI Service**.

Source: [Azure blog – Introducing GPT-4 in Azure OpenAI Service][azure-blog].

Cloud infrastructure uses global data centers; regions are not public.

### Estimated Energy (Inference)

Published or estimated per-query energy values vary between studies.
Representative numbers include:

**Epoch AI (2024):** ≈ 0.3 Wh (0.0003 kWh) per ChatGPT/GPT-4 query.

Source: [Epoch AI – How Much Energy Does ChatGPT Use?][epoch-ai].

Other analysts estimate ≈ 0.3 – 1.8 Wh (0.0003 – 0.0018 kWh)
depending on prompt length, token output, and GPU hardware.

Sources: “The Carbon Footprint of ChatGPT,” media analyses.

**Caveat:** OpenAI does not publish per-query energy data.  
All estimates depend on assumptions such as:

* Hardware type (GPU vs TPU)
* Power Usage Effectiveness (PUE)
* Data center region and carbon intensity
* Prompt and token length

### Training Energy (GPT-4)

Some analyses extrapolate GPT-4’s training energy from model size and
compute budget:

≈ 51 – 62 GWh (51 772 500 – 62 318 750 kWh) for full-scale training.

Source: [The Carbon Footprint of ChatGPT][sustainability-numbers].

These are indirect estimates, not official OpenAI disclosures.

### Water Usage (GPT-4)

Official data are unavailable, but media analyses suggest:

A single ChatGPT query may indirectly consume ≈ 0.5 L of water,
depending on data-center cooling.

Generating a 100-word email may use ≈ 0.14 kWh energy and 0.52 L water.

Source: [The Verge – Sam Altman on ChatGPT Energy and Water Use][verge-gpt].

### PUE and CI Context (GPT-4)

Studies multiply compute energy by:

* **PUE** – Power Usage Effectiveness (total facility power / IT power)
* **CI** – Carbon Intensity (kg CO₂e / kWh electricity)

Example assumptions:

* **PUE:** ≈ 1.1 – 1.3 for Azure hyperscale centers  
* **CI:** ≈ 0.3 – 0.4 kg CO₂e / kWh (depending on region)

---

## Model 2: Claude Haiku (Anthropic)

### Model Name & Provider

**Claude 3 Haiku**, developed by **Anthropic**.

### Model Description

Part of Anthropic’s Claude 3 family (Haiku, Sonnet, Opus).  
Released March 2024. Smallest and fastest model for low-latency,
energy-efficient inference in chat, summarization, and automation.

Source: [Anthropic Blog – Claude 3 Technical Overview][anthropic-blog].

### Hosting & Deployment

Hosted via Anthropic API and **Amazon Bedrock (AWS)**.
These centers maintain **PUE ≈ 1.2**.

Sources: [AWS Bedrock Claude Integration], [AWS Sustainability Report 2024][aws-report].

### Estimated Energy

Anthropic does not publish per-query energy data.
Independent analysts estimate ≈ 0.05 – 0.1 Wh (0.00005 – 0.0001 kWh)
per query based on token count and GPU efficiency.

Claude 3 Haiku is ≈ 5× faster and more efficient than larger Claude 3 models.

Sources: [Epoch AI – Energy Use of AI Models][epoch-ai],
[Anthropic Claude 3 Announcement].

### Training Energy

Claude 3 models use NVIDIA A100/H100 GPUs on AWS.
Typical energy use ≈ 3 000 – 10 000 MWh for 10–30 B parameters.

Sources: [Epoch AI – AI Training Compute and Energy Scaling],
[Anthropic Responsible Scaling Policy][anthropic-policy].

### Water Usage

No specific data published.  
Cooling water managed under **AWS sustainability strategy**.  
Cooler regions use air cooling; others recycle water on-site.

Sources: [AWS Water Stewardship Report][aws-water],
[Anthropic Sustainability Commitments].

### PUE and CI Context

* **AWS PUE:** ≈ 1.2  
* **Carbon Intensity:** ≈ 0 – 0.2 kg CO₂e / kWh (depending on renewables)  
AWS targets 100 % renewable energy by 2025.

Sources: [AWS Global Infrastructure Efficiency Data],
[Anthropic Responsible Scaling Policy][anthropic-policy].

---

## Model 3: Gemini Nano (Google)

### Provider

**Gemini Nano**, developed by **Google DeepMind**.  
Smallest member of Gemini family (Nano, Pro, Ultra).

### Hosting

Runs on-device via **Android AICore** (subsystem introduced 2023).  
Designed for mobile hardware like Pixel 8 Pro and Pixel 9.  
Reduces energy use by eliminating cloud compute and network load.

Sources: [Google AI Blog – Introducing Gemini][google-blog],
[Android Developers – Gemini Nano Overview][android-dev],
[The Verge – Gemini Nano on Pixel 8 Pro][verge-gemini].

### Estimated Energy(Inference)

No official values.  
Device benchmarks show ≈ 0.01 Wh (0.00001 kWh) per query —
10 – 30× more efficient than GPT-4.

Sources: [Google Pixel AI Benchmarks (2024)],
[Epoch AI – How Much Energy Does ChatGPT Use][epoch-ai].

### Training Energy of gemini

Gemini Nano is distilled from larger Gemini models trained on **TPU v5e**.  
Training energy ≈ 200 – 1 200 MWh (1 – 5 % of Gemini Ultra).

Sources: [Google Research – Efficient TPU Training (2024)],
[Google Cloud Sustainability Report (2024)].

### Water Usage (nano)

Inference uses no data-center water.  
Training used Google data centers with **WUE ≈ 0.18 L/kWh**.  
Google targets net-positive water impact by 2030.

Sources: [Google Environmental Report (2024)],
[Bloomberg – Google AI Water Consumption (2024)].

### PUE & CI Context

* **PUE:** ≈ 1.10 – 1.12 (Google Data Centers)
* **CI:** ≈ 0.15 kg CO₂e / kWh (70 % renewable mix)
* **On-device:** < 5 W per inference

Sources: [Google Data Center Efficiency Overview (2024)],
[Google TPU v5e Efficiency Blog (2024)].

---

[azure-blog]:
https://azure.microsoft.com/en-us/blog/introducing-gpt4-in-azure-openai-service/
[epoch-ai]:
https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
[sustainability-numbers]:
https://www.sustainabilitybynumbers.com/p/carbon-footprint-chatgpt
[verge-gpt]:
https://www.theverge.com/2023/1/18/energy-water-chatgpt
[anthropic-blog]:
https://www.anthropic.com/blog/claude3-overview
[aws-report]:
https://aws.amazon.com/about-aws/sustainability/
[anthropic-policy]:
https://www.anthropic.com/responsible-scaling
[aws-water]:
https://aws.amazon.com/about-aws/sustainability/#water
[google-blog]:
https://blog.google/technology/ai/google-gemini-ai/
[android-dev]:
https://developer.android.com/ai/gemini-nano
[verge-gemini]:
https://www.theverge.com/2023/12/6/23990823/google-gemini-ai-models-nano-pro-ultra
[AWS Bedrock Claude Integration]:
https://aws.amazon.com/bedrock/
[Anthropic Claude 3 Announcement]:
https://www.anthropic.com/news/claude-3-models
[Epoch AI – AI Training Compute and Energy Scaling]:
https://epoch.ai/gradient-updates/ai-training-compute-energy-scaling
[Anthropic Sustainability Commitments]:
https://www.anthropic.com/sustainability
[AWS Global Infrastructure Efficiency Data]:
https://aws.amazon.com/about-aws/sustainability/
[Google Pixel AI Benchmarks (2024)]:
https://ai.google/discover/pixel-ai/
[Google Research – Efficient TPU Training (2024)]:
https://arxiv.org/abs/2408.15734
[Google Cloud Sustainability Report (2024)]:
https://sustainability.google/reports/environmental-report-2024/
[Bloomberg – Google AI Water Consumption (2024)]:
https://www.bloomberg.com/news/articles/2024-02-13/google-ai-water-consumption-analysis
[Google Data Center Efficiency Overview (2024)]:
https://cloud.google.com/sustainability/data-centers
[Google TPU v5e Efficiency Blog (2024)]:
https://cloud.google.com/blog/products/ai-machine-learning/introducing-tpu-v5e
