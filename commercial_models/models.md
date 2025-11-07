<!-- markdownlint-disable MD013 MD024 MD025 MD026 MD041 MD001 -->
<!-- This disables line length, duplicate headings, multiple top-level headings, heading punctuation, first heading, and heading increment rules -->
<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD025 -->
<!-- Multiple top-level headings needed for each model section -->

# Model 1: GPT-4 (OpenAI)

### Model Name & Provider

**GPT-4**, developed by **OpenAI**.

#### Hosting & Deployment

Hosted via **Microsoft Azure OpenAI Service**.  
Source: [Azure blog – Introducing GPT-4 in Azure OpenAI Service][azure-blog].

Cloud infrastructure uses global data centers; regions are not public.

#### Estimated Model Size & Architecture

GPT-4 is widely considered a frontier model with a highly complex architecture,  
widely estimated to utilize a Sparse Mixture-of-Experts (MoE) mechanism. This MoE architecture  
allows the model to have a massive total number of latent parameters (potentially over 1 trillion),  
but only a sparse subset (Active FLOPs) are used for any single inference query.  
Source: Optimal Sparsity of Mixture-of-Experts Language Models …  
<https://arxiv.org/html/2508.18672v2>  
Parameters vs FLOPs: Scaling Laws for Optimal Sparsity …  
<https://arxiv.org/html/2501.12370v2>

**Estimated Model Size (widely reported):** ≈ **1.8 trillion parameters**  
(widely reported; not officially confirmed by OpenAI)

#### Estimated Energy (Inference)

Published or estimated per-query energy values vary between studies.  
Representative numbers include:

**Epoch AI (2024):** ≈ 0.3 Wh (0.0003 kWh) per ChatGPT/GPT-4 query.  
Source: [Epoch AI – How Much Energy Does ChatGPT Use?][epoch-ai].

Other analysts estimate ≈ 0.3 – 1.8 Wh (0.0003 – 0.0018 kWh)  
depending on prompt length, token output, and GPU hardware.

**Caveat:** OpenAI does not publish per-query energy data. All estimates depend on assumptions such as:  

- Hardware type (GPU vs TPU)  
- Power Usage Effectiveness (PUE)  
- Data-center region and carbon intensity  
- Prompt and token length

#### Training Energy (GPT-4)

Some analyses extrapolate GPT-4’s training energy from its model size and compute budget:  
≈ 51 – 62 GWh (51,772,500 – 62,318,750 kWh) for full-scale training.  
Source: [The Carbon Footprint of ChatGPT][sustainability-numbers].

These are indirect estimates, not official OpenAI disclosures.

#### Water Usage

Official data are unavailable, but media analyses provide approximate indicators:  

- A single ChatGPT query may indirectly consume ≈ 0.5 L of water.  
- Generating a 100-word email may use ≈ 0.14 kWh energy and 0.52 L water.

Source: [The Verge – Sam Altman on ChatGPT Energy and Water Use][verge-gpt].

#### PUE / CI Context

Studies multiply compute energy by:  

- **PUE** – Power Usage Effectiveness (total facility power / IT power)  
- **CI** – Carbon Intensity (kg CO₂e / kWh)

Example assumptions:  

- **PUE:** ≈ 1.1 – 1.3 for Azure hyperscale centers  
- **CI:** ≈ 0.3 – 0.4 kg CO₂e/kWh (depending on region)

---

# Model 2: Claude 3 Haiku (Anthropic)

### Model Description

Claude 3 Haiku is part of Anthropic’s Claude 3 model family, released in March 2024. It is the smallest and fastest model in the Claude 3 lineup (Haiku, Sonnet, Opus) and is designed for low-latency, energy-efficient inference while maintaining strong reasoning capabilities. Haiku is optimized for lightweight commercial use cases, including chat applications, summarization, and enterprise automation.

Sources:  
[Anthropic – Claude 3 Model Family Overview][anthropic-claude3]  
[Anthropic Blog – Claude 3 Announcement][anthropic-blog]

#### Hosting / Deployment

Claude 3 Haiku is hosted via Anthropic’s API and via AWS Amazon Bedrock (cloud). These data centers typically maintain a **PUE ≈ 1.2**.

Sources:  
[AWS Bedrock Claude Integration][aws-bedrock]  
[AWS Sustainability Report][aws-sustainability]

#### Estimated Model Size / Architecture

Claude 3 Haiku is estimated to have **≈ 20 billion parameters**, making it significantly smaller than larger models in the family (e.g., Claude 3 Opus). This parameter estimate is based on community sources; Anthropic does not publicly confirm.

Source:  
[Reddit – ClaudeAI parameter discussion][reddit-claude-haiku]

#### Estimated Energy

Anthropic does not publish per-query energy data. Independent analysts estimate models of similar size (10–30 billion parameters) use ~0.05-0.1 Wh (0.00005-0.0001 kWh) per query, depending on hardware and tokens. Haiku is reportedly ~5× more efficient than larger Claude variants.

Sources:  
[Epoch AI – Energy Use of AI Models][epoch-energy]  
[Anthropic Claude 3 Announcement][anthropic-announcement]

#### Training Energy Estimates

For models in the 10–30 billion parameter range, training energy is estimated at **3,000-10,000 MWh**, depending on runs and infrastructure.

Sources:  
[Epoch AI – AI Training Compute & Energy Scaling][epoch-training]  
[Anthropic Responsible Scaling Policy][anthropic-scaling]

#### Water Usage of claude

Anthropic has not published water-consumption data for Claude 3. AWS manages cooling water use via its sustainability programs. Some centers use air-cooling or recycle water on-site to reduce water usage.

Sources:  
[AWS Water Stewardship Report][aws-water]  
[Anthropic Sustainability Commitments][anthropic-sustainability]

#### PUE and CI Context

- AWS average **PUE ≈ 1.2** (accounts for cooling & power delivery losses)  
- Carbon intensity **CI ≈ 0-0.2 kg CO₂e/kWh**, depending on region  
- AWS targets **100% renewable energy by 2025**

Sources:  
[AWS Global Infrastructure Efficiency Data][aws-infra]  
[Anthropic Responsible Scaling Policy][anthropic-scaling]

---

# Model 3: Gemini Nano (Google DeepMind)

#### Model Name & Provider

**Gemini Nano**, developed by **Google DeepMind**, is the smallest and most efficient member of the Gemini family (Nano, Flash, Pro, Ultra).

Sources:  
[Google AI Blog – Introducing Gemini][google-gemini]

#### Hosting / Deployment

Runs primarily **on-device** via Android’s **AICore system service** (introduced with Android 14). Optimized hardware (e.g., Pixel 8 Pro / 9 Series) eliminates cloud compute and network latency.

Sources:  
[Android Developers – Gemini Nano Overview][android-nano]

#### Estimated Model Size / Architecture

Gemini Nano is deployed as quantized versions:  

- **Nano-1:** 1.8 billion parameters  
- **Nano-2:** 3.25 billion parameters  

Source:  
[Exploding Topics – Industry Model Sizes][exploding-topics]

#### Estimated Energy (Inference)

Cloud median inference for Gemini: ≈ 0.24 Wh per text prompt (wide-scope).  
On-device Nano estimate: ≈ 0.01 Wh (0.00001 kWh) per query. Note: direct official Nano numbers not published.

Sources:  
[Google Cloud Blog – Measuring Environmental Impact of Inference][google-impact]

#### Training Energy Estimates

Gemini Nano was distilled from larger models on Google TPU v5e clusters. Estimated training cost: **≈ 200-1,200 MWh**, amortised across many devices.

Sources:  
[Google Research – TPU Efficiency Overview][google-tpu]  
[Google Cloud Blog – Measuring Environmental Impact of Inference][google-impact]

#### Water Usage

- **Inference:** Zero data-center water (runs on device)  
- **Training:** Google data centres report WUE ≈ 0.26 mL per median cloud query in some analyses  

Sources:  
[Google Cloud Blog – Measuring Environmental Impact of Inference][google-impact]

#### PUE / CI Context

Google’s data centre fleet reports average **PUE ≈ 1.10-1.12**.  
Reported carbon intensity (CI) ≈ 0.03 g CO₂e per median cloud query, reflecting high level of renewables.

Sources:  
[Google Cloud Blog – Measuring Environmental Impact of Inference][google-impact]

---

[azure-blog]: https://azure.microsoft.com/en-us/blog/introducing-gpt4-in-azure-openai-service  
[epoch-ai]: https://epoch.ai/article/how-much-energy-does-chatgpt-use  
[sustainability-numbers]: https://sustainability-numbers.com/the-carbon-footprint-of-chatgpt  
[verge-gpt]: https://www.theverge.com/2024/4/16/sam-altman-chatgpt-water-energy  
[anthropic-claude3]: https://www.anthropic.com/news/claude-3-family  
[anthropic-blog]: https://www.anthropic.com/news/claude-3  
[aws-bedrock]: https://aws.amazon.com/bedrock/claude/  
[aws-sustainability]: https://sustainability.aboutamazon.com/environment/the-cloud  
[reddit-claude-haiku]: https://www.reddit.com/r/ClaudeAI/comments/1bi7p5w/how_many_parameter_does_claude_haiku_have/  
[epoch-energy]: https://epoch.ai/article/energy-use-of-ai-models  
[anthropic-announcement]: https://www.anthropic.com/news/claude-3  
[epoch-training]: https://epoch.ai/article/ai-training-compute-and-energy-scaling  
[anthropic-scaling]: https://www.anthropic.com/papers/responsible-scaling-policy  
[aws-water]: https://sustainability.aboutamazon.com/environment/water  
[anthropic-sustainability]: https://www.anthropic.com/news/anthropic-sustainability-commitments  
[aws-infra]: https://aws.amazon.com/about-aws/global-infrastructure/sustainability/  
[google-gemini]: https://blog.google/technology/ai/google-gemini-ai/  
[android-nano]: https://developer.android.com/ai/gemini-nano  
[exploding-topics]: https://explodingtopics.com/blog/ai-model-sizes  
[google-impact]: https://cloud.google.com/blog/products/sustainability/measuring-environmental-impact-of-inference  
[google-tpu]: https://research.google/pubs/efficient-tpu-training-v5e/  
