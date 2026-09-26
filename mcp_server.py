import json, sys
from client import MultimodalVisualHallucinationVerifierClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "multimodal-visual-hallucination-verifier", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "verify_visual_claims", "description": "Audits vision agent assertions against ground-truth OCR and bounding box metadata to prevent visual hallucination."}]}}
    elif method == "tools/call":
        client = MultimodalVisualHallucinationVerifierClient()
        res = client.verify_visual_claims()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = MultimodalVisualHallucinationVerifierClient()
        print(json.dumps(client.verify_visual_claims(), indent=2))
