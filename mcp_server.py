"""
MCP Server for Ocular Photopic Negative Response (PhNR) Skill.
Conforms to Model Context Protocol (MCP) JSON-RPC 2.0 stdio specification.
"""

import sys
import json
from client import PhotopicNegativeResponseClient


def handle_request(line: str) -> None:
    try:
        req = json.loads(line)
    except Exception:
        return

    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "genpark-personal-agent-ocular-photopic-negative-response-phnr-glaucoma-skill",
                    "version": "1.0.0"
                }
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/list":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_phnr",
                        "description": "Calculate ERG Photopic Negative Response (PhNR) amplitude, PhNR/b-wave ratio, and retinal ganglion cell health.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "b_wave_peak_amplitude_uv": {"type": "number", "description": "Peak voltage of b-wave (uV)."},
                                "phnr_trough_amplitude_uv": {"type": "number", "description": "Trough voltage of PhNR (uV)."},
                                "baseline_prestimulus_uv": {"type": "number", "description": "Pre-stimulus baseline voltage (default: 0.0 uV)."},
                                "b_wave_latency_ms": {"type": "number", "description": "b-wave peak latency (default: 32.0 ms)."},
                                "phnr_latency_ms": {"type": "number", "description": "PhNR trough latency (default: 72.0 ms)."},
                                "a_wave_trough_uv": {"type": "number", "description": "Optional a-wave trough voltage (uV)."}
                            },
                            "required": ["b_wave_peak_amplitude_uv", "phnr_trough_amplitude_uv"]
                        }
                    }
                ]
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_phnr":
            client = PhotopicNegativeResponseClient()
            try:
                res = client.evaluate_phnr(
                    b_wave_peak_amplitude_uv=float(args["b_wave_peak_amplitude_uv"]),
                    phnr_trough_amplitude_uv=float(args["phnr_trough_amplitude_uv"]),
                    baseline_prestimulus_uv=float(args.get("baseline_prestimulus_uv", 0.0)),
                    b_wave_latency_ms=float(args.get("b_wave_latency_ms", 32.0)),
                    phnr_latency_ms=float(args.get("phnr_latency_ms", 72.0)),
                    a_wave_trough_uv=float(args["a_wave_trough_uv"]) if "a_wave_trough_uv" in args and args["a_wave_trough_uv"] is not None else None
                )
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
                    }
                }
            except Exception as e:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32000, "message": str(e)}
                }
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
    else:
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method {method} not found"}
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()


def main():
    for line in sys.stdin:
        if line.strip():
            handle_request(line)


if __name__ == "__main__":
    main()
