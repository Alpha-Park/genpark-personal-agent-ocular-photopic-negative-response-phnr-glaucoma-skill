"""
Ocular Photopic Negative Response (PhNR) Retinal Ganglion Cell Client.
Zero-mock pure Python standard library implementation.
Calculates Photopic Negative Response (PhNR) trough amplitude (uV),
PhNR/b-wave ratio, and latency from full-field flash electroretinogram (ERG) signals.
"""

import math
from typing import Dict, Any, List, Optional


class PhotopicNegativeResponseClient:
    """
    Evaluates the Photopic Negative Response (PhNR), a slow negative component occurring after
    the b-wave of the photopic full-field ERG, which originates specifically from retinal ganglion cells (RGCs).
    """

    def __init__(self):
        pass

    def evaluate_phnr(
        self,
        b_wave_peak_amplitude_uv: float,
        phnr_trough_amplitude_uv: float,
        baseline_prestimulus_uv: float = 0.0,
        b_wave_latency_ms: float = 32.0,
        phnr_latency_ms: float = 72.0,
        a_wave_trough_uv: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates PhNR absolute amplitude, b-wave amplitude, and PhNR/b-wave ratio.
        b_wave_peak_amplitude_uv: Raw voltage peak of b-wave (uV).
        phnr_trough_amplitude_uv: Raw voltage trough of PhNR (uV, typically negative relative to baseline).
        baseline_prestimulus_uv: Baseline voltage prior to light flash (default: 0.0 uV).
        b_wave_latency_ms: Time to peak of b-wave in ms.
        phnr_latency_ms: Time to trough of PhNR in ms (typically 65 - 85 ms).
        a_wave_trough_uv: Optional photoreceptor a-wave trough voltage (uV).
        """
        if b_wave_latency_ms <= 0 or phnr_latency_ms <= b_wave_latency_ms:
            raise ValueError("PhNR latency must be positive and strictly occur after b-wave peak.")

        # PhNR amplitude measured from baseline (0 uV):
        # By convention, PhNR is a negative wave, so absolute magnitude is baseline - phnr_trough
        phnr_amplitude_uv = baseline_prestimulus_uv - phnr_trough_amplitude_uv

        # b-wave amplitude measured from baseline (or from a-wave trough if provided):
        if a_wave_trough_uv is not None:
            b_wave_net_uv = b_wave_peak_amplitude_uv - a_wave_trough_uv
        else:
            b_wave_net_uv = b_wave_peak_amplitude_uv - baseline_prestimulus_uv

        if b_wave_net_uv <= 0:
            raise ValueError("Calculated b-wave amplitude must be positive.")

        # PhNR / b-wave Ratio:
        # Standard clinical metric to normalize for ocular media opacities, pupil size, and global flash intensity.
        phnr_b_ratio = phnr_amplitude_uv / b_wave_net_uv

        # Clinical evaluation:
        # Healthy adult eyes: PhNR amplitude > 20 uV, PhNR/b-wave ratio >= 0.35 (typically 0.40 - 0.65)
        # Early retinal ganglion cell loss / ocular hypertension / glaucoma: PhNR amplitude drops (12 - 18 uV), ratio 0.25 - 0.34
        # Advanced glaucomatous neuropathy / optic nerve compression: PhNR amplitude < 10 uV, ratio < 0.20
        if phnr_b_ratio >= 0.35 and phnr_amplitude_uv >= 18.0:
            classification = "Normal Retinal Ganglion Cell Electrophysiology"
            rgc_integrity = "Preserved RGC Axonal Function"
            glaucoma_risk = "Low"
        elif phnr_b_ratio >= 0.25 or phnr_amplitude_uv >= 12.0:
            classification = "Early Inner Retinal Dysfunction / Subclinical RGC Stress"
            rgc_integrity = "Mild Ganglion Cell / Optic Nerve Compromise"
            glaucoma_risk = "Moderate / Suspicious"
        else:
            classification = "Severe Retinal Ganglion Cell Loss / Glaucomatous Deficit"
            rgc_integrity = "Pronounced RGC Axonopathy / Ganglion Cell Depletion"
            glaucoma_risk = "High"

        return {
            "status": "success",
            "phnr_amplitude_uv": round(phnr_amplitude_uv, 2),
            "b_wave_amplitude_uv": round(b_wave_net_uv, 2),
            "phnr_b_wave_ratio": round(phnr_b_ratio, 3),
            "phnr_latency_ms": round(phnr_latency_ms, 1),
            "b_wave_latency_ms": round(b_wave_latency_ms, 1),
            "evaluation": {
                "classification": classification,
                "rgc_integrity": rgc_integrity,
                "glaucoma_risk": glaucoma_risk
            }
        }
