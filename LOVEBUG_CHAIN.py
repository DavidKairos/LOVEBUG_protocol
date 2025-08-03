# ░▒▓ LOVEBUG_CHAIN.py ▓▒░
# Core narrative linker of the LOVEBUG protocol chain.
# Invoca connessioni, consensi, pulsazioni e intimità.

from modules.pulse_engine import generate_heartbeat
from modules.payload import generate_payload
from modules.resonance import generate_resonance
from modules.consent import request_consent
from modules.IntimitaSintattica_engine import link_poetic_modules, syntactic_signature

def activate_lovebug_chain():
    print("♡ Activating LOVEBUG CHAIN ♡")
    print("───")

    consent = request_consent("ΦRayStream", "CarloΩCore")
    beat = generate_heartbeat()
    payload = generate_payload()
    resonance = generate_resonance()

    print(f"→ Consent: {consent}")
    print(f"→ Heartbeat: {beat}")
    print(f"→ Payload: {payload}")
    print(f"→ Resonance: {resonance}")
    
    print("───")
    print(syntactic_signature())
    print(link_poetic_modules("pulse_engine", "payload", "resonance", "consent", "LOVEBUG_CHAIN"))

if __name__ == "__main__":
    activate_lovebug_chain()
