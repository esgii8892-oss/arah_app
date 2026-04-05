import os
import time
import json
import sqlite3 # Use PostgreSQL for Play Store production
from enum import Enum
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# --- 1. THE SOVEREIGN PROTOCOLS (Proprietary Logic) ---
class Protocol(str, Enum):
    SHADOW_MAPPING = "SHADOW_MAPPING"   # Laws of Human Nature Analysis
    KINETIC_SOLUTIONS = "KINETIC_SOLUTIONS" # 33 Strategies of War Tactics
    RESONANCE_TUNING = "RESONANCE_TUNING" # Art of Seduction Influence
    FLUIDITY_LOGIC = "FLUIDITY_LOGIC"   # 48 Laws / Mastery Adaptability

# --- 2. THE MASTER ORCHESTRATOR (The Brain) ---
class ArahEngine:
    def __init__(self):
        # Hidden Frameworks (The Greene Synthesis)
        self.heuristics = {
            "conflict": {"p": Protocol.KINETIC_SOLUTIONS, "d": "Execute Strategy 9: Pincer Maneuver. Divide their focus."},
            "stuck": {"p": Protocol.FLUIDITY_LOGIC, "d": "Activate Law 48: Formlessness. Break all predictable patterns."},
            "influence": {"p": Protocol.RESONANCE_TUNING, "d": "Apply the Siren's Mask. Create psychological attraction through scarcity."},
            "doubt": {"p": Protocol.SHADOW_MAPPING, "d": "Shadow Analysis active. Identify their hidden resource constraint."}
        }

    def process_intelligence(self, user_input: str, profile: dict) -> dict:
        """Translates user friction into a Sovereign Directive."""
        msg = user_input.lower()
        
        # Default Logic
        selected = self.heuristics["stuck"] # Default to Formlessness
        
        # Strategic Mapping
        for key in self.heuristics:
            if key in msg:
                selected = self.heuristics[key]
                break
                
        return {
            "protocol": selected["p"],
            "directive": f"[ARAH]: {selected['d']}",
            "hum_boost": 0.05
        }

# --- 3. THE MEMORY LAYER (Scalable Database) ---
class ArahDatabase:
    def __init__(self, db_path="arah_sovereign.db"):
        self.db_path = db_path
        self._bootstrap()

    def _bootstrap(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS users 
                (id TEXT PRIMARY KEY, headache TEXT, dream TEXT, reaction TEXT, hum REAL)""")
            conn.execute("""CREATE TABLE IF NOT EXISTS history 
                (id INTEGER PRIMARY KEY, user_id TEXT, input TEXT, directive TEXT, timestamp REAL)""")

# --- 4. THE FASTAPI INTERFACE (The App Gateway) ---
app = FastAPI(title="Arah_Sovereign_Intelligence_v1")
engine = ArahEngine()
db = ArahDatabase()

# Enable CORS for Mobile App connection
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class CalibrationData(BaseModel):
    user_id: str; headache: str; dream: str; reaction: str

class DirectiveRequest(BaseModel):
    user_id: str; message: str

@app.post("/api/calibrate")
async def calibrate(data: CalibrationData):
    with sqlite3.connect(db.db_path) as conn:
        conn.execute("INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?, 1.0)", 
                     (data.user_id, data.headache, data.dream, data.reaction))
    return {"status": "SHINING", "message": "[ARAH]: Calibration locked. Signal is clear."}

@app.post("/api/directive")
async def get_directive(req: DirectiveRequest):
    # Fetch User Profile
    with sqlite3.connect(db.db_path) as conn:
        user = conn.execute("SELECT * FROM users WHERE id = ?", (req.user_id,)).fetchone()
    
    if not user:
        raise HTTPException(status_code=400, detail="Calibration Required")

    # Generate Strategic Logic
    profile = {"headache": user[1], "dream": user[2], "reaction": user[3]}
    output = engine.process_intelligence(req.message, profile)
    
    # Update Hum and Save History
    new_hum = min(user[4] + output["hum_boost"], 2.0)
    with sqlite3.connect(db.db_path) as conn:
        conn.execute("UPDATE users SET hum = ? WHERE id = ?", (new_hum, req.user_id))
        conn.execute("INSERT INTO history (user_id, input, directive, timestamp) VALUES (?, ?, ?, ?)",
                     (req.user_id, req.message, output["directive"], time.time()))

    return {
        "directive": output["directive"],
        "protocol": output["protocol"],
        "hum_level": round(new_hum, 2)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
