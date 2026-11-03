"""
Example usage of Ocular Photopic Negative Response (PhNR) Skill.
Demonstrates healthy preserved retinal ganglion cell function vs early glaucomatous neuropathy.
"""

import json
from client import PhotopicNegativeResponseClient


def main():
    print("=== Testing Ocular Photopic Negative Response (PhNR) Skill ===")
    client = PhotopicNegativeResponseClient()

    # 1. Healthy normal eye (b-wave peak = 65 uV, PhNR trough = -30 uV, baseline = 0 uV -> PhNR amp = 30 uV, ratio = 30/65 = 0.462)
    res_normal = client.evaluate_phnr(
        b_wave_peak_amplitude_uv=65.0,
        phnr_trough_amplitude_uv=-30.0,
        baseline_prestimulus_uv=0.0,
        b_wave_latency_ms=31.0,
        phnr_latency_ms=70.0
    )
    print("\n[Case 1: Normal Healthy Retinal Ganglion Cell Response]")
    print(json.dumps(res_normal, indent=2))

    # 2. Early glaucomatous optic nerve compromise (selective drop in PhNR: b-wave remains 60 uV, but PhNR is blunted to -10 uV -> ratio = 0.167)
    res_glaucoma = client.evaluate_phnr(
        b_wave_peak_amplitude_uv=60.0,
        phnr_trough_amplitude_uv=-10.0,
        baseline_prestimulus_uv=0.0,
        b_wave_latency_ms=32.0,
        phnr_latency_ms=75.0
    )
    print("\n[Case 2: Early Glaucomatous RGC Axonopathy]")
    print(json.dumps(res_glaucoma, indent=2))

    # Assertions
    assert res_normal["phnr_b_wave_ratio"] >= 0.35
    assert res_glaucoma["phnr_b_wave_ratio"] < 0.25
    assert res_normal["evaluation"]["glaucoma_risk"] == "Low"
    assert res_glaucoma["evaluation"]["glaucoma_risk"] == "High"
    print("\n[SUCCESS] Photopic Negative Response tests passed!")


if __name__ == "__main__":
    main()
