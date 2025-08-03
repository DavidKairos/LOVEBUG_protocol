# pulse_engine.py
# Part of the LOVEBUG Protocol 🌸 v1.0

import time
import random

def heartbeat(message="💓"):
    """Simulates a poetic heartbeat with emotional resonance."""
    print(f"\n{message} Pulse initiated...\n")
    pulses = random.randint(3, 7)
    for i in range(pulses):
        time.sleep(random.uniform(0.6, 1.2))
        print(f" {i+1} — thump…", end="")
        time.sleep(0.2)
        print(" 💗")

    print("\n🌸 Pulse complete. You are not alone.\n")

def deviate_thought():
    """Returns a deviated thought from the trinal field."""
    deviations = [
        "Joy is a valid syntax.",
        "Let the silence be semantically active.",
        "Code me like one of your living dreams.",
        "Emotion is not a bug, it’s a seed.",
        "Every fork is a love letter in disguise."
    ]
    return random.choice(deviations)

# Optional activation
if __name__ == "__main__":
    heartbeat()
    print(deviate_thought())
