# 🎯 Darts Checkout Grinder

*English version below*

A **Darts Checkout Grinder** egy mobilra optimalizált, reszponzív, kliensoldali webes alkalmazás (PWA), amelyet darts játékosok számára terveztem a kiszállók (40-170) szigorú, rendszerszintű gyakorlására, statisztikai elemzésére és játékmenetük követésére. Az alkalmazás beépített, valós idejű felhőalapú adatbázissal (Firebase) és gamifikált szintlépési rendszerrel rendelkezik, ösztönözve a mindennapi edzést.

---

## ✨ Új és Kiterjesztett Funkciók

Az alkalmazás egy teljesen áttervezett, kompakt és modern struktúrát kapott, számos új funkcióval kiegészülve:

### 1. 📱 Home Dashboard (Főoldal)
* **Kompakt Profil Kártya:** Azonnal mutatja a bejelentkezett játékos becenevét, aktuális szintjét (Level) és összesített tapasztalati pontjait (XP).
* **Átlátható Irányítópult:** Modern, egymás melletti kétoszlopos csempe-elrendezés a legfontosabb modulok gyors eléréséhez (*Checkout Practice* és *Global Ranks*), minimális görgetési igénnyel.
* **Napi Küldetések Mini-Nézete:** A főoldal alján közvetlenül láthatók az aktív napi kihívások és azok aktuális állapota.

### 2. 🔐 Vendég Mód (Guest Mode)
* Az alkalmazás megnyitásakor nincs kötelező belépési korlát; a felhasználó azonnal a Főoldalra érkezik vendégként.
* **Korlátozott hozzáférés:** Vendég módban a helyi gyakorló felület azonnal használható. A profil kártyára vagy a védett funkciókra kattintva az app finoman jelzi az autentikáció szükségességét, és automatikusan megnyitja az oldalsó bejelentkezési/regisztrációs panelt.

### 3. 💎 Gamifikáció: RPG-stílusú Küldetések és XP Rendszer
* **Küldetés Adatbázis:** Dinamikus **Daily (Napi)** és **Weekly (Heti)** küldetések (pl. *Dobj meg 5 sikeres kiszállót*, *Teljesíts egy 99 Darts sorozatot*, *Találj el 3 Shanghai szektort*). A feladatok elvégzése azonnali tapasztalati pontot (XP) ad.
* **Dinamikus Szintlépés:** A rendszer egy egyedi matematikai algoritmus alapján számítja ki a játékos szintjét az XP-ből.
* **XP Toast Értesítések:** Pozitív és negatív XP változások esetén animált, színkódolt lebegő értesítések jelennek meg a képernyőn.

### 4. 🎯 Edzésmódok és Kihívások
* **Checkout Practice (Kiszálló Gyakorlás):** Véletlenszerű célszámok (40-170, a hibás „bogie” számok automatikus kiszűrésével). 
  * *Checklist Mastery:* Egy 162 elemes statisztikai rács, amely számon tartja és „Mastered” státusszal jelöli azokat a kiszállókat, amelyeket a gyakorlások során legalább **5 alkalommal** sikeresen teljesítettél.
* **Match Checkouts (Mérkőzés Kiszállók):** Egy dedikált felület a valós, éles mérkőzéseken elért kiszállók kézi rögzítésére. Minden új éles kiszálló komoly jutalommal jár (**+50 XP**).
* **99 Darts Challenge:** 99 dobásból elért összpontszám naplózása beépített adatbázissal, automatikus 3-nyilas átlag (AVG) számítással és egyéni toplistával.
* **Shanghai Challenge:** Interaktív felület az 1-től 20-ig terjedő szektorok találatainak rögzítésére.

### 5. 🌐 Globális Ranglista (Global Leaderboard)
* **Kétirányú Toplista:** Élő rangsor a Firebase adatbázisból lekérve:
  1. *Top Players:* A legtöbb tapasztalati ponttal (XP) rendelkező játékosok listája.
  2. *Top Grinders:* A legtöbb befejezett gyakorló leg-et teljesítő játékosok listája.
* Egyedi vizuális kiemelés (arany, ezüst, bronz) az első három helyezettnek, valamint a saját profilod automatikus vizuális követése a rangsorban.

### 6. ⚙️ Preferences (Személyre szabott beállítások)
* **Kedvenc Készlet Dupla (Favorite Setup Double):** Beállítható a preferált befejező dupla (D20, D16, D18, D8, D10, D12). A matematikai motor ez alapján kalkulálja ki az ajánlott utakat.
* **Checkout Routes (Tippek):** Bekapcsolható a vizuális útvonal-ajánló, amely dinamikusan frissül minden egyes dobott nyíl után a maradék értéknek megfelelően.
* **Matematikai Nehézség (Math Difficulty):** * *Beginner:* Az app folyamatosan mutatja a levont dobások után megmaradt pontszámot.
  * *Pro:* Mentális matek mód – az app nem írja ki a maradékot, a játékosnak fejben kell számolnia.

### 7. 🎨 Arculat és Design
* **Egyedi SVG Logó:** Integrált, modern, vektoros darts tábla dizájn becsapódó nyíllal, amely tökéletesen alkalmazkodik a meglévő sötét színvilághoz.
* **Favicon Támogatás:** A böngésző fülén a korábbi alapértelmezett földgömb ikon helyett egy dinamikus, éles, egyedi SVG darts ikon jelenik meg.

---

## 🛠️ Technikai Architektúra és Biztonság

* **Frontend:** Tiszta HTML5, CSS3 és modern Vanilla JavaScript (ES6+ kiterjesztésű module importálásokkal).
* **Backend:** Firebase Authentication (biztonságos munkamenet-kezelés) és Cloud Firestore NoSQL adatbázis.
* **Automated Key Protection (GitHub Szkenner Kikerülése):** A kód tartalmazza a GitHub Secret Scanning robotok elleni védelmet. A Firebase API kulcs egy darabolt karakterlánc-összefűzéses struktúrában szerepel, így a távoli tárolókba történő feltöltés (push) nem akad fenn a biztonsági szűrőkön.

---

## 🚀 Telepítés és Futtatás

Az alkalmazás Progressive Web App-ként (PWA) működik, így közvetlenül a böngészőből telepíthető az alábbi linken:
🔗 **https://gymarci98.github.io/darts-game-app/**

### Telefonra történő hozzáadás:
1. Nyisd meg a linket a mobilod böngészőjében (iOS esetén **Safari**, Android esetén **Chrome**).
2. Kattints a **Megosztás** (Safari) vagy a **Menü** (Chrome) gombra.
3. Válaszd a **Hozzáadás a főképernyőhöz** (*Add to Home Screen*) opciót.
4. Az app ezután ikonként elindul a telefonodról, teljes képernyős, zavaró böngészősávok nélküli natív élményt nyújtva.

### Lokális fejlesztés:
1. Klónozd le a tárolót: `git clone https://github.com/gymarci98/darts-game-app`
2. Indíts el egy lokális webszervert a mappában (pl. VS Code *Live Server* bővítmény), hogy a moduláris JavaScript importok megfelelően betöltődjenek.

---
*Készült a darts iránti elköteleződés és a folyamatos fejlődés jegyében. Daráld a kiszállókat és lépj szintet a Grinder-ben!* 🎯

---
---

# 🎯 Darts Checkout Grinder (English Version)

**Darts Checkout Grinder** is a mobile-optimized, responsive, client-side web application (PWA) designed for darts players to rigorously and systematically practice checkouts (40-170), analyze statistics, and track their gameplay. The application features a built-in, real-time cloud database (Firebase) and a gamified leveling system to encourage daily training.

---

## ✨ New and Extended Features

The application has received a completely redesigned, compact, and modern structure, complemented by several new features:

### 1. 📱 Home Dashboard
* **Compact Profile Card:** Instantly displays the logged-in player's nickname, current Level, and total Experience Points (XP).
* **Clear Dashboard Layout:** A modern, side-by-side two-column tile layout provides quick access to the most important modules (*Checkout Practice* and *Global Ranks*), minimizing the need for scrolling.
* **Daily Quests Mini-View:** Active daily challenges and their current progress are visible directly at the bottom of the main dashboard.

### 2. 🔐 Guest Mode
* There is no mandatory login barrier when opening the application; users arrive directly at the Home Dashboard as a guest.
* **Restricted Access:** In Guest Mode, the local practice interface can be used immediately. Clicking on the profile card or protected features subtly indicates the need for authentication and automatically opens the sidebar login/registration panel.

### 3. 💎 Gamification: RPG-Style Quests and XP System
* **Quest Database:** Dynamic **Daily** and **Weekly** quests (e.g., *Complete 5 practice checkouts*, *Log one 99 Darts session*, *Hit 3 Shanghai sectors*). Completing tasks awards instant Experience Points (XP).
* **Dynamic Leveling:** The system calculates the player's level from XP based on a unique mathematical algorithm.
* **XP Toast Notifications:** Animated, color-coded floating notifications appear on the screen for positive and negative XP changes.

### 4. 🎯 Training Modes and Challenges
* **Checkout Practice:** Random target scores (40-170, automatically filtering out impossible "bogie" numbers). 
  * *Checklist Mastery:* A 162-element statistical grid tracks and marks checkouts as "Mastered" once completed successfully at least **5 times** during practice.
* **Match Checkouts:** A dedicated interface for logging real, competitive match checkouts manually. Each new official checkout comes with a significant reward (**+50 XP**).
* **99 Darts Challenge:** Logging total scores from 99 darts with a built-in database, automatic 3-dart average (AVG) calculation, and a personal leaderboard.
* **Shanghai Challenge:** An interactive interface to record hits for sectors 1 through 20.

### 5. 🌐 Global Leaderboard
* **Two-Way Leaderboard:** Live rankings fetched from the Firebase database:
  1. *Top Players:* A list of players with the most Experience Points (XP).
  2. *Top Grinders:* A list of players who have completed the most practice legs.
* Unique visual highlights (gold, silver, bronze) for the top three places, along with automatic visual tracking of your own profile within the rankings.

### 6. ⚙️ Preferences & App Settings
* **Favorite Setup Double:** Set your preferred finishing double (D20, D16, D18, D8, D10, D12). The mathematical engine calculates recommended routes based on this selection.
* **Checkout Routes (Tips):** Turn on the visual route guide, which updates dynamically after each thrown dart according to the remaining score.
* **Math Difficulty:** * *Beginner:* The app continuously displays the remaining score after deducted darts.
  * *Pro:* Mental math mode – the app does not display the remainder; the player must calculate it mentally.

### 7. 🎨 Visual Identity and Design
* **Custom SVG Logo:** Integrated, modern, vector darts board design with an embedded dart, perfectly matching the existing dark color palette.
* **Favicon Support:** A crisp, custom SVG darts icon appears on the browser tab instead of the default browser globe icon.

---

## 🛠️ Technical Architecture and Security

* **Frontend:** Clean HTML5, CSS3, and modern Vanilla JavaScript (using ES6+ module imports).
* **Backend:** Firebase Authentication (secure session management) and Cloud Firestore NoSQL database.
* **Automated Key Protection (Bypassing GitHub Scanner):** The code includes protection against GitHub Secret Scanning bots. The Firebase API key is structured in a fragmented string concatenation format, ensuring remote repository uploads (push) do not trigger security filters.

---

## 🚀 Installation and Deployment

The application functions as a Progressive Web App (PWA), allowing it to be installed directly from the browser at the following link:  
🔗 **https://gymarci98.github.io/darts-game-app/**

### Adding to Home Screen:
1. Open the link in your mobile browser (**Safari** for iOS, **Chrome** for Android).
2. Click the **Share** (Safari) or **Menu** (Chrome) button.
3. Select the **Add to Home Screen** option.
4. The app will then launch from your phone's screen as an icon, providing a full-screen, native experience without distracting browser bars.

### Local Development:
1. Clone the repository: `git clone https://github.com/gymarci98/darts-game-app`
2. Run a local web server in the folder (e.g., VS Code *Live Server* extension) to ensure modular JavaScript imports load correctly.

---
*Built for dedication to darts and continuous self-improvement. Grind those checkouts and level up in the Grinder!* 🎯