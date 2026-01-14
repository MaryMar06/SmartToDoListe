import os
import re

print("📝 Smart To-Do Planer gestartet.")  # Programmname

# Versuch, das lokale Modell über llama-cpp zu laden
try:
    from llama_cpp import Llama

    model_path = "models/tiny-llama-q4/tinyllama-1.1b-chat-v1.0.Q4_K_S.gguf"

    if os.path.exists(model_path):
        print("💻 Modell: TinyLlama (lokal, GGUF über llama-cpp)")
        llm = Llama(model_path=model_path)

        output = llm("Hallo! Was kannst du?", max_tokens=50)
        print("🤖 TinyLlama Antwort:", output["choices"][0]["text"].strip())
    else:
        raise FileNotFoundError("GGUF-Modell nicht gefunden, HuggingFace wird verwendet")

except Exception as e:
    print("⚠️ Lokales Modell nicht gefunden oder Fehler:", e)
    print("💻 Modell: TinyLlama (HuggingFace)")

    from transformers import AutoTokenizer, AutoModelForCausalLM

    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    inputs = tokenizer("Hallo! Was kannst du?", return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)
    print("🤖 TinyLlama Antwort:", tokenizer.decode(outputs[0], skip_special_tokens=True))


def get_priority(category):
    """Priorität je nach Kategorie bestimmen."""
    if category == "Arbeit":
        return "hoch"
    elif category == "Zuhause":
        return "mittel"
    elif category == "Hobby":
        return "niedrig"
    else:
        return "niedrig"



while True:
    user_input = input("\nGib deine Aufgaben ein (jede Aufgabe mit ';' trennen, oder 'exit' zum Beenden):\n")
    if user_input.lower() == "exit":
        break

    tasks = [task.strip() for task in user_input.split(";") if task.strip()]
    structured_list = []

    for task in tasks:
        # Übliche Einleitungsfloskeln entfernen (Groß-/Kleinschreibung ignorieren)
        task = re.sub(
            r"^(heute muss ich |ich muss heute |ich soll |bitte erledige |aufgabe: )+",
            "",
            task,
            flags=re.IGNORECASE
        ).strip()

        # Kategorie der Aufgabe bestimmen
        if "Zimmer" in task or "Wäsche" in task or "Küche" in task:
            category = "Zuhause"
        elif "Buch" in task or "lesen" in task:
            category = "Hobby"
        elif "E-Mail" in task or "Arbeit" in task:
            category = "Arbeit"
        else:
            category = "Sonstiges"

        priority = get_priority(category)
        structured_list.append(f"- {task} (Priorität: {priority}, Kategorie: {category})")

    print("\n=== 🗂️ Strukturierte To-Do-Liste ===")
    for item in structured_list:
        print(item)

    print("\n✅ To-Do-Liste erfolgreich erstellt!")
    