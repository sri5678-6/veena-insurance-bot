import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from gtts import gTTS
import speech_recognition as sr
import time
import threading
import io
import pygame
import json
from difflib import get_close_matches
from veena_script import veena_script  # Ensure this file exists with proper script flow

# --- Load customer data ---
with open("customer_data.json", "r", encoding="utf-8") as f:
    customers = json.load(f)

if customers and isinstance(customers, list):
    customer = customers[0]
    policy_holder = customer.get("policy_holder", "Customer")
    policy_number = customer.get("policy_number", "N/A")
    product_name = customer.get("product_name", "Insurance Plan")
    policy_start_date = customer.get("policy_start_date", "N/A")
    total_premium_paid = customer.get("total_premium_paid", "N/A")
    premium_due_date = customer.get("premium_due_date", "N/A")
    outstanding_amount = customer.get("outstanding_amount", "N/A")
    sum_assured = customer.get("sum_assured", "N/A")
    fund_value = customer.get("fund_value", "N/A")
else:
    policy_holder = "Customer"
    policy_number = "N/A"
    product_name = "Insurance Plan"
    policy_start_date = "N/A"
    total_premium_paid = "N/A"
    premium_due_date = "N/A"
    outstanding_amount = "N/A"
    sum_assured = "N/A"
    fund_value = "N/A"

# --- Language setup ---
LANGUAGES = {
    "english": "en",
    "hindi": "hi",
    "marathi": "mr",
    "gujarati": "gu"
}

selected_language = 'en'
lang_key = 'english'

# --- Global flags ---
is_speaking = False
user_input_queue = []

# --- Audio and mic setup ---
pygame.mixer.init()
recognizer = sr.Recognizer()
mic = sr.Microphone()

# --- GUI Setup ---
root = tk.Tk()
root.title("Veena Insurance Bot")
root.geometry("650x500")
text_area = ScrolledText(root, font=("Helvetica", 12), wrap=tk.WORD)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def append_text(speaker, message):
    text_area.insert(tk.END, f"{speaker}: {message}\n\n")
    text_area.see(tk.END)

# --- Speak using gTTS ---
def speak(text):
    global is_speaking
    is_speaking = True
    append_text("Veena", text)
    try:
        tts = gTTS(text=text, lang=selected_language)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        pygame.mixer.music.load(fp, 'mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        append_text("Error", f"Audio error: {e}")
    finally:
        is_speaking = False

# --- Background callback ---
def callback(recognizer, audio):
    global is_speaking
    if is_speaking:
        return  # Ignore input while Veena is speaking
    try:
        text = recognizer.recognize_google(audio, language=selected_language)
        append_text("User", text)
        user_input_queue.append(text.lower())
    except sr.UnknownValueError:
        append_text("System", "Sorry, I didn't catch that.")
    except sr.RequestError as e:
        append_text("Error", f"API Error: {e}")

# --- Start background listening ---
stop_listening = recognizer.listen_in_background(mic, callback)

# --- Polling function for input ---
def listen(timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if user_input_queue:
            return user_input_queue.pop(0)
        time.sleep(0.1)
    append_text("Veena", "No response detected.")
    return ""

# --- Language selection ---
def listen_language():
    global selected_language, lang_key
    speak("Hello, I am Veena from ValuEnable Life Insurance.")
    speak("Which language do you prefer? English, Hindi, Marathi or Gujarati?")
    for _ in range(3):
        res = listen()
        for lang in LANGUAGES:
            if lang in res:
                selected_language = LANGUAGES[lang]
                lang_key = lang
                speak(f"Language selected: {lang.title()}")
                return
        speak("Please repeat the language.")
    speak("Defaulting to English.")
    selected_language = 'en'
    lang_key = 'english'

# --- Script transition logic ---
def get_next_state(current_state, user_input):
    options = veena_script[current_state].get("options", {}).get(lang_key, {})

    # 1. First: keyword-based partial match
    for keyword, next_state in options.items():
        if keyword.lower() in user_input:
            return next_state

    # 2. Then: fuzzy match fallback
    matches = get_close_matches(user_input, options.keys(), n=1, cutoff=0.6)
    if matches:
        return options[matches[0]]

    return None


# --- Main conversation flow ---
def run_script():
    listen_language()
    current_state = "start"
    while current_state:
        template = veena_script[current_state]["text"][lang_key]
        text = template.replace("{policy_holder}", policy_holder)\
                       .replace("{policy_number}", policy_number)\
                       .replace("{product_name}", product_name)\
                       .replace("{policy_start_date}", policy_start_date)\
                       .replace("{total_premium_paid}", str(total_premium_paid))\
                       .replace("{premium_due_date}", premium_due_date)\
                       .replace("{outstanding_amount}", str(outstanding_amount))\
                       .replace("{sum_assured}", str(sum_assured))\
                       .replace("{fund_value}", str(fund_value))
        speak(text)
        if not veena_script[current_state].get("options", {}).get(lang_key):
            break
        response = listen()
        next_state = get_next_state(current_state, response)
        if next_state:
            current_state = next_state
        else:
            speak("I didn't understand that. Let me repeat.")

# --- Proper exit handler ---
def on_close():
    stop_listening(wait_for_stop=False)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# --- Start bot in separate thread ---
threading.Thread(target=run_script).start()

# --- Start GUI loop ---
root.mainloop()
