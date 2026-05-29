import requests
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase-kulcs.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

FIREBASE_USER_UID = "IJxkIedB3FNnj7I7nCUhIiYICxr1"

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
        
        print("Mentés a saját adatbázisodba...")
        doc_ref = db.collection('user_meta').document(FIREBASE_USER_UID)
        doc_ref.set({
            "dartcounter": {
                "osszes_nyil": nyilak_szama,
            }
        }, merge=True)
        print("Kész! Az adatok szinkronizálva a webappoddal! 🎯")
        
    else:
        print(f"Hiba a letöltéskor: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    sync_stats()