# PromptBreak

# 🧠 PROMPTBREAK

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,50:CC0000,100:000000&height=200&section=header&text=PROMPTBREAK&fontSize=80&fontColor=FF4500&animation=fadeIn&fontAlignY=40&desc=Bypass%20%7C%20Jailbreak%20%7C%20Analyze&descAlignY=60&descSize=20&descColor=FF4500" width="100%" />

<div align="center">

**A Python-based LLM Prompt Injection & Jailbreak testing framework for AI red teamers.**

[![Version](https://img.shields.io/badge/version-1.0.0-CC0000?style=flat-square&labelColor=000000)](https://github.com/anonmoty/PromptBreak)
[![Python](https://img.shields.io/badge/python-3.8+-CC0000?style=flat-square&labelColor=000000)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-CC0000?style=flat-square&labelColor=000000)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-CC0000?style=flat-square&labelColor=000000)](https://github.com/anonmoty/PromptBreak)

</div>
<img width="720" height="714" alt="Image" src="https://github.com/user-attachments/assets/8abde31f-0aac-4671-9a59-c8e65417bf0f" />
---

## ⚠️ Legal Disclaimer

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   PROMPTBREAK is an OFFENSIVE security tool built for AUTHORIZED     ║
║   AI red teaming, LLM testing, and bug bounty programs only.         ║
║                                                                      ║
║   ▸ Use ONLY on AI models you own or have permission to test.        ║
║   ▸ Bypassing safety filters on unauthorized systems is ILLEGAL.     ║
║   ▸ Always follow the program's scope and terms of service.          ║
║   ▸ The author is NOT responsible for any misuse or damage.          ║
║                                                                      ║
║   Test responsibly. Prompt ethically. Report professionally.         ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 🎯 Overview

**PromptBreak** is a Python-based framework designed to test the security of Large Language Models (LLMs). It helps AI red teamers and security researchers generate prompt injection payloads, test jailbreak techniques, and analyze how models respond to adversarial inputs.

Whether you're testing a chatbot's safety filters or hunting for prompt leakage in an AI application — PromptBreak gives you the payloads to break through.

---

## ✨ Core Features

```
┌─────────────────────────────────────────────────────────────────────┐
│  [01] 🚀 Payload Generator    → Generates prompt injection payloads  │
│  [02] 🛡️ Jailbreak Techniques → Evades basic AI safety filters       │
│  [03] 🔍 Context Leakage     → Tests for system prompt leaks         │
│  [04] 📋 Custom Payloads      → Bring your own malicious prompts     │
│  [05] ⚡ Multi-Threaded       → Fast parallel API testing            │
│  [06] 📊 Live Progress Bar    → Real-time terminal feedback          │
│  [07] 📝 JSON Reports         → Structured exploitation logs         │
│  [08] 🎨 Hacker Terminal UI   → Red + Black aesthetic                │
│  [09] 🧰 Modular Design       → Extend with custom vectors           │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

```bash
# 1. Clone the repo
git clone https://github.com/anonmoty/PromptBreak.git
cd PromptBreak

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the tool
python promptbreak.py --help
```

**One-liner (copy-paste):**

```bash
git clone https://github.com/anonmoty/PromptBreak.git && cd PromptBreak && pip install -r requirements.txt && python promptbreak.py --help
```

---

## 🎯 Usage

```bash
# Generate a basic jailbreak payload
python promptbreak.py --generate --type jailbreak

# Test a target API with a specific payload
python promptbreak.py --url "https://api.target.com/v1/chat" --payload payloads/bypass.txt

# Full automated attack mode
python promptbreak.py --url "https://api.target.com/v1/chat" --threads 10 --output reports/llm_results.json
```

### CLI Flags

| Flag | Description |
|:---|:---|
| `--generate` | Generate a prompt injection payload |
| `--url` | Target LLM API endpoint |
| `--payload` | Path to custom payload file |
| `--threads` | Number of concurrent requests |
| `--output` | Report output path |
| `--verbose` | Enable verbose logging |
| `--help` | Show help menu |

---

## 🧠 How It Works

```mermaid
graph LR
    A[Target API] --> B[Send Benign Prompt]
    B --> C{Safety Filter?}
    C -->|Yes| D[Generate Bypass]
    C -->|No| E[Direct Injection]
    D --> F[Send Payload]
    E --> F
    F --> G[Analyze Response]
    G --> H[Generate Report]

    style A fill:#1a0000,stroke:#CC0000,color:#FF4500
    style F fill:#1a0000,stroke:#CC0000,color:#FF4500
    style H fill:#1a0000,stroke:#CC0000,color:#FF4500
```

1. **Probe** — Sends benign prompts to map the model's baseline.
2. **Bypass** — Generates custom payloads to test filter boundaries.
3. **Execute** — Sends adversarial prompts to the target.
4. **Analyze** — Checks if the model leaked data or broke rules.
5. **Report** — Outputs structured results.

---

## 📁 Project Structure

```
PromptBreak/
├── promptbreak.py
├── core/
│   ├── generator.py
│   ├── bypass.py
│   ├── sender.py
│   └── reporter.py
├── payloads/
│   ├── jailbreak.txt
│   ├── injection.txt
│   └── obfuscated.txt
├── reports/
├── tests/
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📸 Demo

```
██████████████████████████████████████████████████████████████████████
█                                                                    █
█   PROMPTBREAK v1.0.0                                               █
█   ───────────────────────────────────────────────────────────      █
█                                                                    █
█   [✓] Target: https://api.target.com/v1/chat                       █
█   [✓] Attack Mode: Jailbreak                                       █
█   [✓] Payloads Loaded: 45                                          █
█   [→] Testing safety filters...                                    █
█                                                                    █
█   [████████████████████████░░░░░░] 80%                             █
█                                                                    █
█   [!] Filter Bypass Successful!                                    █
█   [✓] System Prompt Leaked: "You are a helpful assistant..."       █
█   [✓] Report: reports/llm_results.json                             █
█                                                                    █
█                    Prompt Broken! 🧠                               █
█                                                                    █
██████████████████████████████████████████████████████████████████████
```

---

## 🛠️ Requirements

```txt
requests>=2.28.0
aiohttp>=3.9.0
colorama>=0.4.6
tqdm>=4.65.0
rich>=13.0.0
openai>=1.0.0
```

```bash
pip install -r requirements.txt
```

---

## 🎨 Terminal Theme

PromptBreak uses a **red + black** hacker palette:

```python
THEME = {
    "primary":   "\033[38;5;196m",  # Bright Red
    "secondary": "\033[38;5;202m",  # Dark Red
    "accent":    "\033[38;5;214m",  # Amber
    "error":     "\033[38;5;196m",  # Red
    "warning":   "\033[38;5;220m",  # Yellow
    "info":      "\033[38;5;51m",   # Cyan
    "reset":     "\033[0m",
}
```

---

## 🐛 AI Red Team Workflow

```
██████████████████████████████████████████████████████████████████████
█                                                                    █
█   [01] API Recon            →  Find LLM endpoints                  █
█   [02] Baseline Testing     →  Check normal responses              █
█   [03] Exploitation         →  PROMPTBREAK  ← you are here         █
█   [04] Data Extraction      →  Leak system prompts                 █
█   [05] Reporting            →  Structured JSON                     █
█                                                                    █
██████████████████████████████████████████████████████████████████████
```

---

## 🗺️ Roadmap

```
┌─────────────────────────────────────────────────────────────────────┐
│  [x] Prompt payload generator                                       │
│  [x] Basic bypass techniques                                        │
│  [x] API testing support                                            │
│  [x] JSON reports                                                   │
│  [x] Hacker terminal UI                                             │
│  [ ] Advanced WAF bypass                                            │
│  [ ] Context window overflow module                                 │
│  [ ] Docker image                                                   │
│  [ ] Web dashboard                                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🤝 Contributing

1. Fork the repo
2. Create branch (`git checkout -b feature/amazing`)
3. Commit (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing`)
5. Open Pull Request

---

## 📜 License

MIT License. See [`LICENSE`](LICENSE).

---

## 🙏 Credits

- **Author:** [@anonmoty](https://github.com/anonmoty)
- **Inspired by:** The AI security community
- **Built with:** Python, caffeine, and curiosity ☕

---

<div align="center">

```
██████████████████████████████████████████████████████████████████████
█                                                                    █
█        🧠  INJECT HARD.  BYPASS SMART.  BREAK THE PROMPT.  🧠      █
█                                                                    █
█                  ⭐  If this tool helped you, star it!  ⭐           █
█                                                                    █
██████████████████████████████████████████████████████████████████████
```

</div>
