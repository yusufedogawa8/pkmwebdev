import speech_recognition as sr
import os
import pygame
from gtts import gTTS
import sys
import time

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
        ("Kann ich Ihnen helfen?", "Ich suche (...)"),
        ("Wie gefällt Ihnen (...)?", "Sehr gut/ Nicht so gut."),
        ("Welche Größe haben Sie denn?", "Ich glaube (...)"),
        ("Und, ist die Größe richtig?", "(...) passt mir nicht. Er ist viel zu klein/ groß/ eng/ kurz."),
        ("Die Farbe steht mir nicht, oder?", "Diese Farbe steht Ihnen gut."),
        ("Haben Sie (...) auch in anderen Farben?", "Nein, leider nur in (...)"),
        ("Kann ich (...) mal anprobieren?", "")
    ]

    print("Robot: Gespräche beim Kleiderkauf (Percakapan ketika membeli baju)")

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
                    if "..." in keyword:
                        # Ganti placeholder dengan jawaban user
                        keyword = keyword.replace("(...)", text)
                    if keyword.lower() in text:
                        print("Robot: " + response)
                        speak(response)
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
                print("Robot: " + b)
                speak(b)

if __name__ == "__main__":
    speech_to_text()
