# Model 1: GPT-4 (OpenAI)

## Model Name & Provider

**GPT-4**, developed by **OpenAI**

### Hosting / Deployment

Hosted via **Microsoft Azure OpenAI Service**.

Source: [Azure blog – Introducing GPT-4 in Azure OpenAI Service][azure-blog]

Cloud infrastructure with global data-centers; exact hosting regions not
publicly specified.

### Estimated Energy (Inference)

Published or estimated per-query energy values vary between studies.
Representative numbers include:
**Epoch AI (2024):** $\approx 0.3$ Wh ($0.0003$ kWh) per typical ChatGPT/GPT-4
query under assumed workloads.

Source: [Epoch AI – How Much Energy Does ChatGPT Use?][epoch-ai]

Other independent analysts: $\sim 0.3 - 1.8$ Wh ($0.0003 - 0.0018$ kWh) per query,
depending on prompt length, token output, and GPU hardware.
Sources: [The Carbon Footprint of ChatGPT], media analyses.

**Caveat:** OpenAI does not publish per-query energy data. All estimates
depend heavily on assumptions such as:

* Hardware type (GPU vs TPU)
* Power Usage Effectiveness (PUE)
* Data-center region and carbon intensity
* Prompt and token length

### Training Energy (GPT-4)

Some analyses extrapolate GPT-4’s training energy from its model size and
compute budget:
Example estimate:
$\approx 51,772,500 – 62,318,750$ kWh ($\approx 51,773 – 62,319$ MWh)
consumed for full-scale training.

Source: [The Carbon Footprint of ChatGPT][sustainability-numbers]
These are indirect estimates, not official OpenAI disclosures.

### Water Usage (GPT-4)

Official data are unavailable, but public remarks and media analyses give
approximate indicators:

A single ChatGPT query may indirectly consume $\sim 0.5$ liters of water,
depending on data-center cooling.

For instance, generating a 100-word email may consume $\sim 0.14$ kWh energy
and $0.519$ L of water.

Source: [The Verge – Sam Altman on ChatGPT Energy and Water Use][verge-gpt]

### PUE / CI Context (GPT-4)

To estimate total environmental footprint, studies multiply compute energy by:

* **PUE** (Power Usage Effectiveness) – ratio of total facility power to IT
  equipment power.
* **CI** (Carbon Intensity) – kg $\text{CO}_2\text{e}$ emitted per kWh of electricity
  generated.

Example assumptions from literature:

* **PUE** $\approx 1.1 – 1.3$, typical for **hyperscale** Azure data-centers.
* **CI** $\approx 0.3–0.4$ kg $\text{CO}_2\text{e}$/kWh,
 depending on the region’s energy mix.

---

## Model 2: Claude Haiku (Anthropic)

### Model Name & Provider (Claude Haiku)

**Claude 3 Haiku**, developed by **Anthropic**

### Model Description

Claude 3 Haiku is part of Anthropic’s Claude 3 model family, released in
March 2024. It is the smallest and fastest model in the lineup (Haiku,
Sonnet, Opus) and is designed for low-latency, energy-efficient inference.
Haiku is optimized for lightweight commercial use cases, including chat
applications, summarization, and enterprise automation.

Source: [Anthropic Blog – Claude 3 Technical Overview][anthropic-blog]

### Hosting / Deployment (Claude Haiku)

Claude 3 Haiku is hosted through Anthropic’s own API and via **Amazon Bedrock**
(**AWS** cloud).
These centers typically maintain a **Power Usage Effectiveness (PUE) of $\sim 1.2$**.

Sources: [AWS Bedrock Claude Integration], [AWS Sustainability Report 2024][aws-report]

### Estimated Energy (Haiku Inference)

Anthropic does not publicly disclose per-query energy data.
Independent analysts estimate inference use around:
$\sim 0.05–0.1$ Wh ($0.00005–0.0001$ kWh) per query, depending on token count and
GPU efficiency.

Claude 3 Haiku is reported to be **$\sim 5\times$ faster and more efficient** than
larger Claude 3 models (Sonnet or Opus).

Sources: [Epoch AI – Energy Use of AI Models][epoch-ai], [Anthropic Claude 3 Announcement]

### Training Energy (Claude Haiku)

Claude 3 models are trained on **GPU clusters** (NVIDIA A100/H100) primarily
hosted on AWS infrastructure.
For models in the $10–30$B parameter range, training energy is typically
**$3,000–10,000$ MWh**.

Sources: [Epoch AI – AI Training Compute & Energy Scaling],
 [Anthropic Responsible Scaling Policy][anthropic-policy]

### Water Usage (Claude Haiku)

Anthropic has not published specific water consumption figures for the
Claude 3 family.
Cooling water use is managed under **AWS’s sustainability strategy**.
AWS data centers in cooler regions use air cooling to reduce water footprint,
while others recycle water on-site.

Sources: [AWS Water Stewardship Report][aws-water], [Anthropic Sustainability Commitments]

### PUE / CI Context (Claude Haiku)

* **AWS’s average PUE:** $\sim 1.2$ (accounts for cooling and power delivery losses).
* **Carbon intensity (CI):
* ** $\sim 0–0.2$ kg $\text{CO}_2\text{e}$/kWh, depending on regional
  renewable mix.
AWS aims for **$100\%$ renewable energy by 2025**, lowering emissions over time.

Sources: [AWS Global Infrastructure Efficiency Data],
 [Anthropic Responsible Scaling Policy][anthropic-policy]

---

## Model 3: Gemini Nano (Google)

### Model Name & Provider (Gemini Nano)

**Gemini Nano**, developed by **Google DeepMind**.
Smallest member of the Gemini model family (Nano, Pro, Ultra).

### Hosting / Deployment (Gemini Nano)

Runs **on-device** through **Android AICore** (subsystem introduced in 2023).
Designed for mobile hardware such as Pixel 8 Pro and Pixel 9 series.
**Reduces energy use by eliminating cloud compute and network transmission.**

Sources: [Google AI Blog – Introducing Gemini][google-blog],
[Android Developers – Gemini Nano Overview][android-dev],
[The Verge – Gemini Nano arrives on Pixel 8 Pro][verge-gemini]

### Estimated Energy (Nano Inference)

No official values published for per-query energy.
Independent device benchmarks indicate $\approx 0.01$ Wh ($0.00001$ kWh) per query.
This is **$10–30\times$ more efficient** than cloud-hosted models such as GPT-4.

Sources: [Google Pixel AI Benchmarks (2024)],
[Epoch AI – How Much Energy Does ChatGPT Use][epoch-ai]

### Training Energy (Gemini Nano)

Gemini Nano was **distilled** from larger Gemini models trained on **TPU v5e**
clusters.
Training energy for Nano $\approx 200 – 1,200$ MWh ($\approx 1–5\%$ of Gemini Ultra’s
training compute).

Sources: [Google Research – Efficient TPU Training (2024)],
 [Google Cloud Sustainability Report (2024)]

### Water Usage (Gemini Nano)

Inference uses **no data-center water** since it runs locally on devices.
Training used Google data centers with **Water Usage Effectiveness (WUE)**
$\approx 0.18$ L/kWh.
Google targets **net-positive water impact by 2030**.

Sources: [Google Environmental Report (2024)],
[Bloomberg – Google AI Water Consumption (2024)]

### PUE / CI Context (Gemini Nano)

* **Google Data Centers** report average **PUE** $\approx 1.10–1.12$.
* **Carbon Intensity (CI)**
* $\approx 0.15$ kg $\text{CO}_2\text{e}$ / kWh due to $70\%+$ renewable
  energy mix.
* **On-device execution** uses $< 5$ W of mobile power per inference.

Sources: [Google Data Center Efficiency Overview (2024)],
[Google TPU v5e Efficiency Blog (2024)]

---
[azure-blog]: https://azure.microsoft.com/en-us/blog/introducing-gpt4-in-azure-openai-service/
[epoch-ai]: https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
[sustainability-numbers]: https://www.sustainabilitybynumbers.com/p/carbon-footprint-chatgpt
[verge-gpt]: https://www.theverge.com/2023/1/18/energy-water-chatgpt
[anthropic-blog]: https://www.anthropic.com/blog/claude3-overview
[aws-report]: https://aws.amazon.com/about-aws/sustainability/
[anthropic-policy]: https://www.anthropic.com/responsible-scaling
[aws-water]: https://aws.amazon.com/about-aws/sustainability/#water
[google-blog]: https://blog.google/technology/ai/google-gemini-ai/
[android-dev]: https://developer.android.com/ai/gemini-nano
[verge-gemini]: https://www.theverge.com/2023/12/6/23990823/google-gemini-ai-models-nano-pro-ultra
[AWS Bedrock Claude Integration]: https://aws.amazon.com/bedrock/
[Anthropic Claude 3 Announcement]: https://www.anthropic.com/news/claude-3-models
[Epoch AI – AI Training Compute & Energy Scaling]: https://epoch.ai/gradient-updates/ai-training-compute-energy-scaling
[Anthropic Sustainability Commitments]: https://www.anthropic.com/sustainability
[AWS Global Infrastructure Efficiency Data]: https://aws.amazon.com/about-aws/sustainability/
[Google Pixel AI Benchmarks (2024)]: https://ai.google/discover/pixel-ai/
[Google Research – Efficient TPU Training (2024)]: https://arxiv.org/abs/2408.15734
[Google Cloud Sustainability Report (2024)]: https://sustainability.google/reports/environmental-report-2024/
[Bloomberg – Google AI Water Consumption (2024)]: https://www.bloomberg.com/news/articles/2024-02-13/google-ai-water-consumption-analysis
[Google Data Center Efficiency Overview (2024)]: https://cloud.google.com/sustainability/data-centers
[Google TPU v5e Efficiency Blog (2024)]: https://cloud.google.com/blog/products/ai-machine-learning/introducing-tpu-v5e
