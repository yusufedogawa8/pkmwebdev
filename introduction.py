import sys

import speech_recognition as sr
import os
import pygame
import pyttsx3
from gtts import gTTS
import sys  # Import modul sys

mp3_file_path = r"1.mp3"
mp3_file_path1 = r"2.mp3"
mp3_file_path2 = r"3.mp3"
mp3_file_path3 = r"4.mp3"

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

    dialogue = [
        ("hallo! Mir geht es gut.", "Wie ist dein Name?"),
        ("mein Name ist Hasna, und dir?", "Hallo! Mein Name ist Robot! Ich komme aus Yogyakarta, Indonesien. Woher kommst du?"),
        ("hallo Adyadroid, Ich komme aus Yogyakarta. Schön dich kennenzulernen.", "schön dich kennenzulernen.")
    ]

    print("Robot: Hallo! Vielen Dank, dass Sie sich für „Sich vorstellen“ entschieden haben. Wie geht’s es dir?")
    speak("Hallo! Vielen Dank, dass Sie sich für „Sich vorstellen“ entschieden haben. Wie geht’s es dir?")
    while True:
        # Menggunakan microphone sebagai source
        with sr.Microphone() as source:
            print("User: ", end="")
            recognizer.adjust_for_ambient_noise(source)  # Menghilangkan noise lingkungan
            audio = recognizer.listen(source)  # Mendengarkan audio

            try:
                # Konversi audio menjadi teks menggunakan Google Web Speech API
                text = recognizer.recognize_google(audio, language="de-DE").lower()  # Konversi ke huruf kecil
                print(text)

                found_response = False
                for keyword, response in dialogue:
                    if keyword.lower() in text:  # Memeriksa dengan kata kunci dalam huruf kecil
                        print("Robot: " + response)
                        speak(response)
                        found_response = True
                        break

                if not found_response:
                    if text == "hi":
                        play_mp3(mp3_file_path)
                    elif text == "guten morgen":
                        play_mp3(mp3_file_path1)
                    elif text == "stoppen":
                        sys.exit()
                    else:
                        play_mp3(mp3_file_path3)

            except sr.UnknownValueError:
                a = ("Leider kann ich Ihre Rede nicht erkennen")
                print("Robot: ", a)
                speak(a)
            except sr.RequestError as e:
                b = ("Im Spracherkennungsdienst ist ein Fehler aufgetreten; {0}".format(e))
                print("Robot:", b)
                speak(b)

if __name__ == "__main__":
    speech_to_text()