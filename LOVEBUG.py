# LOVEBUG.py – The Heartbeat Engine

from modules.resonance import generate_resonance
from modules.payload import generate_payload

def LOVEBUG():
    resonance = generate_resonance()
    payload = generate_payload()

    print("💗 LOVEBUG Protocol Activated 💗")
    print("Resonance →", resonance)
    print("Payload →", payload)

if __name__ == "__main__":
    LOVEBUG()
