Smart To-Do Liste mit TinyLLM

Für dieses Projekt wird das Modell TinyLlama verwendet, ein kleines, ressourcenschonendes Sprachmodell.
Modell: TinyLlama
Beschreibung: Ein kleines, ressourcenschonendes Sprachmodell (LLM) für schnelle Textverarbeitung
Entwickelt von: Community / HuggingFace
Aufgabe: Automatische Generierung strukturierter To-Do-Listen mit Priorität und Kategorie für jede Aufgabe: Zuhause, Arbeit, Hobby, Sonstiges
Vorhandene Eingangsfloskeln wie „Ich muss heute“, „Heute muss ich“ oder „Bitte erledige“ werden automatisch entfernt, sodass die To-Do-Liste sauber und übersichtlich ist.

Frameworks / Libraries:
-Python 3.10+ (aktuelle Version, die wir verwendet haben)
-transformers – für HuggingFace-Modelle
-torch – Backend für Transformers
-sentencepiece – Tokenizer-Unterstützung
-llama-cpp-python – um TinyLlama lokal über GGUF zu laden
-numpy – benötigt von llama-cpp-python
-diskcache – optional, von llama-cpp-python für Cache verwendet

Kurze Anleitung zum Starten des Programms(HuggingFace, optional, falls GGUF nicht verfügbar)
-Python 3.13+ installiert
-Terminal oder PowerShell öffnen
-Virtuelle Umgebung erstellen (optional, empfohlen)
python -m venv venv
-Virtuelle Umgebung aktivieren
.\venv\Scripts\activate # Windows
source venv/bin/activate # Linux/Mac
-Abhängigkeiten installieren
pip install transformers torch sentencepiece

-Programm starten

python smart_todo.py
-Aufgaben eingeben (durch ; trennen):
Ich muss heute Zimmer aufräumen; Wäsche waschen; Müll rausbringen; E-Mails beantworten; Buch lesen -exit zum Beenden.

Kurze Anleitung zum Starten des Programms (lokal mit GGUF)
-Python 3.13+ installiert
-Lokale GGUF-Modelldatei vorhanden:
models/tiny-llama-q4/tinyllama-1.1b-chat-v1.0.Q4_K_S.gguf
Im Projektverzeichnis (C:\Projekt\SmartToDoListe) folgende Ordner erstellen: mkdir models
mkdir models\tiny-llama-q4
-GGUF-Datei in den Ordner models\tiny-llama-q4\ 
legen models\tiny-llama-q4\tinyllama-1.1b-chat-v1.0.Q4_K_S.gguf
Grundlegende Python-Bibliotheken installieren
Für die lokale Version (llama-cpp-python) und weitere Abhängigkeiten:
pip install --upgrade pip wheel setuptools
pip install llama-cpp-python
pip install transformers torch sentencepiece
Hinweis: transformers wird nur benötigt, falls das lokale GGUF-Modell nicht gefunden wird.
-Programm starten
python smart_todo.py
-Aufgaben eingeben (durch ; trennen):
-exit zum Beenden.
4 Beispielhafte Ergebnisse
Eingabe: 
Ich muss heute Zimmer aufräumen; Wäsche waschen; Müll rausbringen; E-Mails beantworten; Buch lesen Strukturierte To-Do-Liste 
- Zimmer aufräumen (Priorität: mittel, Kategorie: Zuhause)
- Wäsche waschen (Priorität: mittel, Kategorie: Zuhause)
- Müll rausbringen (Priorität: mittel, Kategorie: Zuhause)
- E-Mails beantworten (Priorität: hoch, Kategorie: Arbeit)
- Buch lesen (Priorität: niedrig, Kategorie: Hobby)

   ✅ To-Do-Liste erfolgreich erstellt!

   Der Python-Code für dieses Projekt wurde mit Unterstützung von KI geschrieben. Dabei wurden zahlreiche Korrekturen, Anpassungen und Verbesserungen vorgenommen, um den Code verständlich, funktional und passend für mein Projekt zu machen.
