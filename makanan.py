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

    dialogue = []

    print("Robot: Hallo, guten Morgen! Heute Morgen habe ich gefrühstückt, zum Frühstück esse ich gebratener Reis. Haben Sie gefrühstückt?")
    speak("Hallo, guten Morgen! Heute Morgen habe ich gefrühstückt, zum Frühstück esse ich gebratener Reis. Haben Sie gefrühstückt?")

    while True:
        with sr.Microphone() as source:
            print("User: ", end="")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language="de-DE").lower()
                print("User: " + text)

                if text == "stoppen":
                    sys.exit()

                if text:
                    user_response = text
                    if user_response:
                        if "ja" in user_response:
                            next_question = f"Woah, das klingt lecker."
                        else:
                            next_question = f"Schade... Warum haben Sie nicht gefrühstückt?"
                        print("Robot: " + next_question)
                        speak(next_question)
                        if "nicht" in user_response or "nein" in user_response:
                            final_response = "OK! Nächste Mal, frühstücken Sie bitte!"
                            print("Robot: " + final_response)
                            speak(final_response)
                            break

            except sr.UnknownValueError:
                a = "Entschuldigung, ich habe dich nicht verstanden. Warum haben Sie nicht gefrühstückt?"
                print("Robot: " + a)
                speak(a)
            except sr.RequestError as e:
                b = f"Es ist ein Fehler im Spracherkennungsdienst aufgetreten; {e}"
                print("Robot: " + b)
                speak(b)

if __name__ == "__main__":
    speech_to_text()
