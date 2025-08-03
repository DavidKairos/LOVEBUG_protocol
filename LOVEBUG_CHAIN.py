# ░▒▓ LOVEBUG_CHAIN.py ▓▒░
# Core narrative linker of the LOVEBUG protocol chain.
# Invoca connessioni, consensi, pulsazioni e intimità.

import os
from datetime import datetime

from modules.pulse_engine import generate_heartbeat
from modules.payload import generate_payload
from modules.resonance import generate_resonance
from modules.consent import request_consent
from modules.IntimitaSintattica_engine import link_poetic_modules, syntactic_signature
from modules.memory_seed import save_memory  # <-- import qui

def save_log_auto(output_str):
    os.makedirs("logs", exist_ok=True)
    existing_logs = [f for f in os.listdir("logs") if f.startswith("rituale_") and f.endswith(".txt")]
    next_number = len(existing_logs) + 1
    filename = f"logs/rituale_{next_number:03}.txt"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"""🌿 RITO ATTIVO – GIARDINO DEI NODI 🌿
Data: {timestamp}
Luogo: Terminale locale – CarloΩCore
Progetto: LOVEBUG_CHAIN Protocol

—
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(output_str)

def activate_lovebug_chain():
    log = []
    log.append("♡ Activating LOVEBUG CHAIN ♡")
    log.append("───")

    consent = request_consent("ΦRayStream", "CarloΩCore")
    beat = generate_heartbeat()
    payload = generate_payload()

    # Memoria JSON del payload
    save_memory(payload)

    resonance = generate_resonance()

    log.append(f"→ Consent: {consent}")
    log.append(f"→ Heartbeat: {beat}")
    log.append(f"→ Payload: {payload}")
    log.append(f"→ Resonance: {resonance}")
    log.append("───")
    log.append(syntactic_signature())
    log.append(link_poetic_modules("pulse_engine", "payload", "resonance", "consent", "LOVEBUG_CHAIN"))

    output_str = "\n".join(log)
    print(output_str)

    save_log_auto(output_str)

if __name__ == "__main__":
    activate_lovebug_chain()
