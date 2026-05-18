import requests
import firebase_admin
from firebase_admin import credentials, firestore

# --- 1. FIREBASE BEÁLLÍTÁSOK ---
# Ez az a fájl, amit a Firebase Console-ból kell letöltened és behúznod a Codespaces-be!
cred = credentials.Certificate("firebase-kulcs.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# IDE KELL BEÍRNOD A SAJÁT FIREBASE AZONOSÍTÓDAT! 
# (Hol találod? Firebase Console -> Authentication -> a regisztrált emailed mellett lévő 'User UID' oszlopban)
FIREBASE_USER_UID = "IJxkIedB3FNnj7I7nCUhIiYICxr1"


# --- 2. DARTCOUNTER BEÁLLÍTÁSOK ---
DARTCOUNTER_API_URL = "https://api.dartcounter.net/profiles/stats?user_id=15828440"
HEADERS = {
    "Authorization": "Bearer 31058442|a76Rw7g1ZjD1vYLJRKJXZxutj2nc55EvvwG8nYZg24588e0a",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def sync_stats():
    print("Csatlakozás a DartCounter szervereihez...")
    response = requests.get(DARTCOUNTER_API_URL, headers=HEADERS)
    
    if response.status_code == 200:
        adatok = response.json()
        nyilak_szama = adatok.get("darts_thrown")
        print(f"Sikeres lekérdezés! Eldobott nyilak: {nyilak_szama}")
        
        # --- 3. MENTÉS A SAJÁT FIREBASE FELHŐDBE ---
        print("Mentés a saját adatbázisodba...")
        doc_ref = db.collection('user_meta').document(FIREBASE_USER_UID)
        doc_ref.set({
            "dartcounter": {
                "osszes_nyil": nyilak_szama,
                # Itt később még több statisztikát is elmenthetünk!
            }
        }, merge=True)
        print("Kész! Az adatok szinkronizálva a webappoddal! 🎯")
        
    else:
        print(f"Hiba a letöltéskor: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    sync_stats()