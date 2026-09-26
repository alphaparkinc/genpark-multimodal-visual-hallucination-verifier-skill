import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import MultimodalVisualHallucinationVerifierClient

def main():
    client = MultimodalVisualHallucinationVerifierClient()
    res = client.verify_visual_claims()
    print("=== Multimodal Visual Hallucination Verifier Output ===")
    print(f"Grounding Score: {res['visual_grounding_score']*100}% | Hallucination Detected: {res['hallucination_detected']}")
    print(f"Severity: {res['hallucination_severity']} | Action: {res['recommended_action']}")
    if res['discrepancy_details']:
        print("\nDiscrepancies Flagged:")
        for d in res['discrepancy_details']:
            print(f"  * [{d['attribute']}] Claimed: '{d['claimed']}' vs Actual: '{d['actual']}'")

if __name__ == '__main__':
    main()
