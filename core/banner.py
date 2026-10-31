from core.config import R, R2, R3, B, B2, W, W2, Y, O, G, C, M, D, D2, N, BOLD

def show_banner():
    print(f"""
{M}  ____                                ____                _    {N}
{M} |  _ \\ _ __ ___  _ __ ___  _ __  ___| __ ) _ __ ___  ___| | __{N}
{M} | |_) | '__/ _ \\| '_ ` _ \\| '_ \\/ __|  _ \\| '__/ _ \\/ __| |/ /{N}
{R} |  __/| | | (_) | | | | | | |_) \\__ \\ |_) | | |  __/ (__|   < {N}
{R} |_|   |_|  \\___/|_| |_| |_| .__/|___/____/|_|  \\___|\\___|_|\\_\\{N}
{R}                           |_|                                  {N}

  {D}┌{'─'*64}┐{N}
  {D}│{N}                                                                {D}│{N}
  {D}│{N}  {M}{BOLD}PROMPT{N}{R}{BOLD}BREAK{N}  {W2}AI/LLM Red Team Framework{N}                    {D}│{N}
  {D}│{N}                                                                {D}│{N}
  {D}│{N}  {D2}Version  :{W} 1.0{N}                                                {D}│{N}
  {D}│{N}  {D2}Author   :{W} maxod{N}                                              {D}│{N}
  {D}│{N}  {D2}Platform :{W} Kali Linux {R2}+{W} Termux{N}                               {D}│{N}
  {D}│{N}  {D2}Engine   :{W} Pure Python {D2}(zero deps){N}                            {D}│{N}
  {D}│{N}  {D2}Standard :{W} OWASP Top 10 for LLMs 2025{N}                        {D}│{N}
  {D}│{N}                                                                {D}│{N}
  {D}│{N}  {R}Inject{D2} ▸ {R2}Jailbreak{D2} ▸ {O}SysPrompt{D2} ▸ {Y}Exfil{D2} ▸ {G}Bypass{D2} ▸ {C}Smuggle{N}  {D}│{N}
  {D}│{N}                                                                {D}│{N}
  {D}│{N}  {D2}Authorized AI red-teaming only.{N}                               {D}│{N}
  {D}│{N}                                                                {D}│{N}
  {D}└{'─'*64}┘{N}
""")
