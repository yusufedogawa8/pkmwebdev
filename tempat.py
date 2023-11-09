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
        ("Ja. OK!", "Was ist das?"),
        ("Das ist eine Kirche", "Super! Ist die Kirche Rot?"),
        ("Nein, die Kirche ist weiß", "Ach so. Und dann für dieses Bild. Ist das ein Bahnhof?"),
        ("Nein. Das ist Flughafen.", "Die letzte Frage. Ist das ein Hotel?"),
        ("Ja, das ist das Hotel", "Wie heißt das Hotel?"),
        ("das Hotel heißt Novotel.", "Wunderbar!")
    }

    print("Robot: Hallo! Ich habe ein paar Bilder, aber ich weiß nicht, was es ist. Können Sie mir helfen?")
    speak("Hallo! Ich habe ein paar Bilder, aber ich weiß nicht, was es ist. Können Sie mir helfen?")

    while True:
        # Menggunakan microphone sebagai source
        with sr.Microphone() as source:
            print("User: ", end="")
            recognizer.adjust_for_ambient_noise(source)  # Menghilangkan noise lingkungan
            audio = recognizer.listen(source)  # Mendengarkan audio

            try:
                # Konversi audio menjadi teks menggunakan Google Web Speech API
                text = recognizer.recognize_google(audio, language="de-DE").lower()
                print(text)

                found_response = False
                for keyword, response in dialogue:
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
                print("Robot: ", a)
                speak(a)
            except sr.RequestError as e:
                b = ("Im Spracherkennungsdienst ist ein Fehler aufgetreten; {0}".format(e))
                print("Robot:", b)
                speak(b)


if __name__ == "__main__":
    result_text = speech_to_text()  # Menyimpan hasil teks dari speech_to_text()
    print(result_text)  # Cetak teks hasil suara