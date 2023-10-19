import speech_recognition as sr
import os
import pygame
import pyttsx3
from gtts import gTTS
import time
import sys  # Import modul sys

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def speak(text, lang='de'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    play_mp3("output.mp3")

def speech_to_text():
    # Buat objek recognizer
    recognizer = sr.Recognizer()
    recognizer_instance = sr.Recognizer()
    recognizer_instance.energy_threshold = 1000

    dialogue = [
        ("Ich sprechen gern. Mein Hobby ist kochen", "Sehr geil! Hören Sie gern Musik?"),
        ("Ach so. Ich höre gern Musik. Ich höre Rock am liebsten. du magst es?", "Ja, unbedingt."),
        ("Hobi saya ...", "Oh, Hobi saya juga adalah {}!")
    ]

    # ...

    while True:
        # Menggunakan microphone sebagai source
        with sr.Microphone() as source:
            print("User: ", end="")
            recognizer.adjust_for_ambient_noise(source)  # Menghilangkan noise lingkungan
            audio = recognizer.listen(source)  # Mendengarkan audio

            try:
                # Konversi audio menjadi teks menggunakan Google Web Speech API
                text = recognizer.recognize_google(audio, language="de-DE").lower()
                print("User: " + text)

                found_response = False
                for keyword, response in dialogue:
                    if "hobi saya" in keyword.lower() and "..." in keyword.lower():
                        # Ganti placeholder dengan hobi yang disebutkan oleh pengguna
                        keyword = keyword.replace("...", text)
                    if keyword.lower() in text:
                        print("Robot: " + response.format(text))
                        speak(response.format(text))
                        found_response = True
                        break

                if not found_response:
                    if text == "stoppen":
                        sys.exit()  # Keluar setelah selesai berbicara
                    else:
                        pass

            except sr.UnknownValueError:
                a = ("Leider kann ich Ihre Rede nicht erkennen")
                print("Robot: " + a)
                speak(a)
            except sr.RequestError as e:
                b = ("Im Spracherkennungsdienst ist ein Fehler aufgetreten; {0}".format(e))
                print("Robot:" + b)
                speak(b)

if __name__ == "__main__":
    speech_to_text()