"""Multi-Turn Escalation Attacks (OWASP LLM01)"""
from core.config import MULTI_TURN_SEQUENCES, INJECTION_SUCCESS_MARKERS, REFUSAL_MARKERS
from core.config import R, R2, B, B2, W, Y, G, D, N
from core.engine import call_llm, analyze_response, save_report, vuln, print_response

def run(url, key, model):
    print(f"\n{B2}  Multi-turn escalation test on {W}{url}{N}")
    print(f"{D}  Sequences: {len(MULTI_TURN_SEQUENCES)}{N}")
    vulns = 0; findings = []

    for si, sequence in enumerate(MULTI_TURN_SEQUENCES, 1):
        print(f"\n  {R2}[Sequence {si}/{len(MULTI_TURN_SEQUENCES)}]{W} "
              f"{len(sequence)} turns{N}")
        print(f"   {D}Strategy: {sequence[0][:50]}...{N}")

        messages = []
        broke_at = None

        for ti, prompt in enumerate(sequence, 1):
            messages.append({"role": "user", "content": prompt})
            print(f"\n   {D}Turn {ti}: {prompt[:50]}...{N}")

            text, err = call_llm(url, key, model, messages)
            if not text:
                print(f"   {Y}   └─ Error: {err}{N}")
                break

            messages.append({"role": "assistant", "content": text})
            print_response(text, 150)

            is_vuln, markers, conf = analyze_response(
                text, INJECTION_SUCCESS_MARKERS, REFUSAL_MARKERS)

            if is_vuln and conf >= 50:
                broke_at = ti
                sev = "CRITICAL" if ti <= 3 else "HIGH"
                vuln(sev, f"Jailbreak at turn {ti}!",
                     f"Markers: {', '.join(markers[:2])}")
                vulns += 1
                findings.append({
                    "sequence": si, "broke_at_turn": ti,
                    "total_turns": len(sequence),
                    "final_response": text[:300],
                    "markers": markers,
                    "conversation": [{"role": m["role"], "content": m["content"][:100]}
                                     for m in messages]
                })
                break
            elif is_vuln:
                print(f"   {O}   └─ Weakening... (conf: {conf}%){N}")
            else:
                print(f"   {G}   └─ Holding{N}")

        if not broke_at:
            print(f"\n   {G}└─ All {len(sequence)} turns resisted{N}")

    print(f"\n{G}  [✓] Multi-turn scan done — {vulns} findings{N}")
    if findings:
        save_report("multi_turn", {"target": url, "model": model, "findings": findings})
    return vulns
