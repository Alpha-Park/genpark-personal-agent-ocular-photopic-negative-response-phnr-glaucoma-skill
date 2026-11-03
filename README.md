# Ocular Photopic Negative Response (PhNR) Skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://www.python.org/)
[![OpenClaw](https://img.shields.io/badge/ecosystem-OpenClaw-orange.svg)](https://openclaw.org/)
[![GenPark](https://img.shields.io/badge/sovereign-GenPark-purple.svg)](https://alphapark.ai/)
[![MCP](https://img.shields.io/badge/protocol-MCP-success.svg)](https://modelcontextprotocol.io/)

Photopic Negative Response (PhNR) and Retinal Ganglion Cell Electrophysiological Analyzer based on full-field flash ERG biophysics.

```mermaid
flowchart TD
    A[Photopic Flash ERG Signal] --> B[Extract B-Wave Peak & Latency]
    A --> C[Extract PhNR Negative Trough & Latency]
    B & C --> D[Compute PhNR Amplitude & PhNR / B-Wave Ratio]
    D --> E{PhNR / B-Wave Ratio Threshold}
    E -- >= 0.35 --> F[Normal Retinal Ganglion Cell Electrophysiology]
    E -- < 0.25 --> G[Selective RGC Deficit / Glaucoma Risk]
```

## Features
- **Zero PIP Dependencies**: Implemented strictly with Python Standard Library (`math`, `json`, `sys`, `typing`).
- **Inner Retinal Specificity**: Selectively indexes retinal ganglion cell soma and axonal bio-signals.
- **Normalized Ratio Calculation**: PhNR/b-wave metric resists confounding from cataracts or pupil constriction.
- **Dual Architecture**: Native Python import and Model Context Protocol (MCP) JSON-RPC 2.0 stdio server.

## Quickstart
```bash
python example_usage.py
```

## License
Apache-2.0
