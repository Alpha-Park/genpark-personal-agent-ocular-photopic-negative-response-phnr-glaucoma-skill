---
name: genpark-personal-agent-ocular-photopic-negative-response-phnr-glaucoma-skill
description: Electroretinography (ERG) Photopic Negative Response (PhNR) analyzer. Calculates PhNR trough amplitude, PhNR/b-wave ratio, and latency to evaluate inner retinal ganglion cell integrity and glaucoma vulnerability.
version: 1.0.0
author: GenPark Ecosystem
license: Apache-2.0
tags:
  - personal-agent
  - ophthalmology
  - erg
  - phnr
  - glaucoma
  - retinal-ganglion-cells
  - openclaw
  - genpark
  - mcp
---

# Ocular Photopic Negative Response (PhNR) Skill

## Overview
This skill computes the Photopic Negative Response (PhNR) from photopic flash electroretinograms (ERGs):
- **Retinal Origin**: While the a-wave originates from cone photoreceptors and the b-wave from ON-bipolar cells, the PhNR is a negative potential that specifically reflects spiking activity of retinal ganglion cells (RGCs) and their glia.
- **PhNR / b-wave Ratio**: Normalizes the PhNR against the pre-ganglionic b-wave, controlling for optical media opacities, pupil size variation, and flash luminance differences.
- **Early Glaucomatous Screening**: A selective drop in PhNR amplitude and ratio precedes detectable standard automated perimetry visual field defects and nerve fiber layer thinning.

## Mathematical Formulation
1. **PhNR Amplitude**:
   $$\text{PhNR} = V_{\text{baseline}} - V_{\text{trough}}$$
2. **b-wave Amplitude**:
   $$V_b = V_{\text{peak}} - V_{\text{baseline}}$$
3. **Normalized PhNR / b-wave Ratio**:
   $$\text{Ratio} = \frac{\text{PhNR}}{V_b}$$

## Usage
```python
from client import PhotopicNegativeResponseClient

client = PhotopicNegativeResponseClient()
res = client.evaluate_phnr(
    b_wave_peak_amplitude_uv=65.0,
    phnr_trough_amplitude_uv=-28.0
)
print(res["evaluation"]["rgc_integrity"])
```
