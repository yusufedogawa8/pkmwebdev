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
    recognizer = sr.Recognizer()

    dialogue = {
        ("hallo! mir geht es gut.", "Wie ist dein Name?"),
        ("mein Name ist", "Hallo! Mein Name ist Robot! Ich komme aus Yogyakarta, Indonesien. Woher kommst du?"),
        ("hallo Adyadroid, ich komme aus", "Schön dich kennenzulernen.")
    }

    print("Robot: Hallo! Vielen Dank, dass Sie sich für „Sich vorstellen“ entschieden haben. Wie geht's dir?")
    speak("Hallo! Vielen Dank, dass Sie sich für „Sich vorstellen“ entschieden haben. Wie geht's dir?")

    while True:
        with sr.Microphone() as source:
            print("User: ", end="")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language="de-DE").lower()
                print(text)

                found_response = False
                for keyword, response in dialogue.items():
                    if keyword in text:
                        print("Robot: " + response)
                        speak(response)
                        found_response = True
                        if "mein Name ist" in text:
                            user_name = text.replace("mein Name ist", "").strip()
                            response = f"Hallo {user_name}! Mein Name ist Adyadroid! Ich komme aus Yogyakarta, Indonesien. Woher kommst du?"
                            print("Robot: " + response)
                            speak(response)
                            if "ich komme aus" in text:
                                user_city = text.replace("ich komme aus", "").strip()
                                response = f"Schön dich kennenzulernen. Ich komme auch aus {user_city}."
                                print("Robot: " + response)
                                speak(response)
                        break

                if not found_response:
                    if "stoppen" in text:
                        sys.exit()
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
