# Smart Camera Object Detector

Ett datorseende-program (computer vision) som hittar och räknar personer och objekt i en bild –
samma typ av **video-analys på kanten (edge AI)** som körs direkt på en nätverkskamera.
Projektet är inspirerat av tekniken bakom moderna övervakningskameror (t.ex. Axis ARTPEC / ACAP),
där analysen sker på själva enheten i realtid.

> Byggt som ett lärande- och portföljprojekt med fokus på datorseende och kamera-analys.

## 📸 Demo

![Demo – objektdetektion](demo.jpg)

## ✨ Funktioner
- Hittar och ritar rutor runt objekt i en bild (personer, bilar, cyklar m.m.)
- Räknar hur många av varje objekttyp som upptäckts
- Enkel **säkerhetsfunktion**: ger ett "intrångslarm" när en person upptäcks
- Använder en **färdigtränad** YOLOv8-modell (samma princip som edge-analys på en kamera)

## 🎯 Varför detta projekt
Moderna kameror gör mer än att spela in – de **förstår** vad de ser: räknar personer,
upptäcker objekt och larmar vid händelser, allt direkt på enheten. Det här projektet är en
liten, körbar demonstration av just den idén, och kopplar ihop **datorseende** med min
bakgrund inom **systemutveckling och cybersäkerhet**.

## 🛠️ Tech stack
- **Språk:** Python
- **Datorseende / AI:** Ultralytics YOLOv8 (färdigtränad objektdetektionsmodell)
- **Bildhantering:** OpenCV
- **Modell-typ:** COCO-tränad (80 objektklasser, bl.a. person, bil, cykel, väska)

## 🚀 Kom igång

### Alternativ 1 – Google Colab (enklast, inget att installera)
Öppna `Smart_Camera_Detector_Colab.ipynb` i [Google Colab](https://colab.research.google.com),
kör cellerna uppifrån och ner och ladda upp en egen bild.

### Alternativ 2 – Lokalt
```bash
git clone https://github.com/naveenbl1202/smart-camera-detector.git
cd smart-camera-detector

pip install -r requirements.txt
python object_detector.py --image min_bild.jpg
```
Programmet sparar en resultatbild (`output.jpg`) med rutor och skriver ut antalet objekt.

## 🧠 Hur det fungerar (kort)
1. En färdigtränad YOLOv8-modell laddas in.
2. Bilden skickas genom modellen, som returnerar var varje objekt finns och vilken typ det är.
3. Programmet ritar rutor, räknar objekten och larmar om en person upptäcks.

Jag tränar alltså ingen egen modell – jag **använder** en färdigtränad, vilket är precis så
analys fungerar när den körs på en kameras chip (edge).

## 🔭 Möjliga vidareutvecklingar
- Köra på video, bildruta för bildruta (live-analys)
- "Intrångszon": larma bara om en person befinner sig i ett markerat område
- Personräkning över tid (t.ex. hur många passerar)

## 👤 Författare
Naveen Bangalore Lakshminarayan · Malmö · naveenbl1202@gmail.com
