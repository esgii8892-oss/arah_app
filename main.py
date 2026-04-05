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

TACTICS = [
    [
        "Law 15: Crush your enemy totally.", 
        "Sever their lines of communication or support.", 
        "Occupy the vacuum left behind before they can regroup."
    ],
    [
        "Law 21: Play a sucker to catch a sucker.", 
        "Lower their guard by appearing less intelligent or capable than you are.", 
        "Strike decisively once they overextend in their arrogance."
    ],
    [
        "Law 33: Discover each man's thumbscrew.", 
        "Observe their insecurities and emotional triggers quietly.", 
        "Apply subtle pressure to force them into an emotional, irrational mistake."
    ],
    [
        "Law 48: Formlessness.",
        "Refuse to take a predictable or rigid stance.",
        "Pivot rapidly as the situation changes to keep rivals guessing."
    ]
]

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
        
    selected_tactic = random.choice(TACTICS)
    
    return {
        "directive": f"[ARAH]: Reality mapped. Executing KINETIC_SOLUTIONS.",
        "protocol": "KINETIC_SOLUTIONS",
        "analysis": f"User Input detected: '{request.message}'. Formulating counter-maneuver.",
        "step_1": selected_tactic[0],
        "step_2": selected_tactic[1],
        "step_3": selected_tactic[2],
        "hum_level": round(random.uniform(1.0, 1.2), 2)
    }

@app.get("/")
def read_root():
    return {"message": "Arah OS is active and listening."}
