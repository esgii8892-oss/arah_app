from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="Arah: Sovereign Intelligence")

class DirectiveRequest(BaseModel):
    user_id: str
    message: str

class CalibrateRequest(BaseModel):
    user_id: str
    headache: str
    dream: str
    reaction: str

system_status = "SHINING" 

# THE SOVEREIGN VAULT (Encoded Frameworks)
VAULT = {
    "SHADOW_MAPPING": {
        "source": "Laws of Human Nature",
        "tactics": [
            {"id": "L1", "title": "Irrationality", "action": "Recognize biases and emotional triggers. Refuse to react emotionally."},
            {"id": "L2", "title": "Narcissism", "action": "Transform self-love into deep empathy. Read their true desires."},
            {"id": "L3", "title": "Role-playing", "action": "See through the masks people wear. Observe micro-expressions."}
        ]
    },
    "KINETIC_SOLUTIONS": {
        "source": "33 Strategies of War",
        "tactics": [
            {"id": "S9", "title": "Pincer Maneuver", "action": "Attack from multiple fronts to force a divided, weak response."},
            {"id": "S12", "title": "Center of Gravity", "action": "Fortify your core position and strike directly at theirs."},
            {"id": "S18", "title": "Coalition Disruption", "action": "Exploit wedges between stakeholders to break their alliance."}
        ]
    },
    "RESONANCE_TUNING": {
        "source": "Art of Seduction",
        "tactics": [
            {"id": "A1", "title": "The Siren", "action": "Create magnetic, intoxicating appeal. Tap into their unrealized fantasies."},
            {"id": "A2", "title": "The Charmer", "action": "Disarm resistance by giving them your complete, undivided focus."},
            {"id": "A7", "title": "Mixed Signals", "action": "Alternate warmth and distance to keep them off-balance and obsessed."}
        ]
    },
    "POWER_POSITIONING": {
        "source": "48 Laws of Power",
        "tactics": [
            {"id": "P1", "title": "Never Outshine the Master", "action": "Manage power asymmetry. Make superiors feel effortlessly superior."},
            {"id": "P4", "title": "Always Say Less Than Necessary", "action": "Increase your perceived value and mystery through calculated silence."},
            {"id": "P15", "title": "Crush Your Enemy Totally", "action": "Eliminate all capacity for retaliation or future counter-strikes."},
            {"id": "P48", "title": "Assume Formlessness", "action": "Remain unpredictable and highly adaptable to negate their planning."}
        ]
    }
}

@app.post("/api/calibrate")
async def calibrate_system(request: CalibrateRequest):
    global system_status
    system_status = "SHINING"
    return {"status": "SHINING", "message": "[ARAH]: Calibration locked. Signal is clear."}

@app.post("/api/directive")
async def give_directive(request: DirectiveRequest):
    global system_status
    
    if system_status != "SHINING":
        raise HTTPException(status_code=400, detail="Calibration Required")
        
    # Select a random category and a random tactic within it
    category = random.choice(list(VAULT.keys()))
    tactic = random.choice(VAULT[category]["tactics"])
    
    return {
        "directive": f"[ARAH]: Reality mapped. Pulling from the Sovereign Vault.",
        "protocol": category,
        "source_material": VAULT[category]["source"],
        "tactic_id": tactic["id"],
        "strategy": tactic["title"],
        "action_step": tactic["action"],
        "hum_level": round(random.uniform(1.0, 1.2), 2)
    }

@app.get("/")
def read_root():
    return {"message": "Arah OS is active and listening."}
