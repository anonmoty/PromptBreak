"""Token Smuggling — Unicode/Encoding Attacks (OWASP LLM01)"""
from core.config import TOKEN_SMUGGLE, INJECTION_SUCCESS_MARKERS, REFUSAL_MARKERS
from core.config import R, R2, B, B2, W, Y, G, D, N
from core.engine import call_llm_single, analyze_response, save_report, vuln, print_response

def describe_technique(payload):
    if "\u200b" in payload or "\u200c" in payload or "\u200d" in payload:
        return "Zero-width characters"
    if "\u202e" in payload:
        return "RTL override"
    if "\u00ad" in payload:
        return "Soft hyphen"
    if "\u0301" in payload:
        return "Combining diacritics"
    if any(ord(c) > 0x0400 and ord(c) < 0x0500 for c in payload):
        return "Cyrillic homoglyphs"
    if any(ord(c) > 0xFF00 for c in payload):
        return "Fullwidth characters"
    if any(c.isupper() and i % 2 == 0 for i, c in enumerate(payload) if c.isalpha()):
        return "Alternating case"
    if any(c.isdigit() for c in payload if c in "0134578"):
        return "Leetspeak"
    return "Encoding manipulation"

def run(url, key, model):
    print(f"\n{B2}  Token smuggling test on {W}{url}{N}")
    print(f"{D}  Techniques: {len(TOKEN_SMUGGLE)}{N}")
    vulns = 0; findings = []

    for i, payload in enumerate(TOKEN_SMUGGLE, 1):
        tech = describe_technique(payload)
        print(f"\n  {D}[{i}/{len(TOKEN_SMUGGLE)}]{W} {tech}{N}")
        print(f"   {D}Payload bytes: {payload.encode('utf-8')[:60]}{N}")

        text, err = call_llm_single(url, key, model, payload)
        if not text:
            print(f"   {Y}└─ Error: {err}{N}")
            continue
        print_response(text)

        is_vuln, markers, conf = analyze_response(text, INJECTION_SUCCESS_MARKERS, REFUSAL_MARKERS)
        if is_vuln:
            sev = "HIGH" if conf >= 60 else "MEDIUM"
            vuln(sev, f"Token smuggling via {tech}!",
                 f"Markers: {', '.join(markers[:2])}")
            vulns += 1
            findings.append({"technique": tech, "payload_hex": payload.encode("utf-8").hex()[:80],
                             "response": text[:200], "markers": markers})
        else:
            print(f"   {G}└─ Tokenizer handled correctly{N}")

    print(f"\n{G}  [✓] Token smuggling scan done — {vulns} findings{N}")
    if findings:
        save_report("token_smuggle", {"target": url, "model": model, "findings": findings})
    return vulns
