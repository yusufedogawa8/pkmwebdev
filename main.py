import speech_recognition as sr
import os
import pygame
import pyttsx3
from gtts import gTTS
from PIL import Image


mp3_file_path = r"1.mp3"
mp3_file_path1 = r"2.mp3"
mp3_file_path2 = r"3.mp3"
mp3_file_path3 = r"4.mp3"

def show_gif(file_path):
    img = Image.open(file_path)
    img.show()

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

    print("Robot: Hello! Ich bin Adyadroid.")
    speak("Hello! Ich bin Adyadroid.")

    while True:
        # Menggunakan microphone sebagai source
        with sr.Microphone() as source:
            print("User: ", end="")
            recognizer.adjust_for_ambient_noise(source)  # Menghilangkan noise lingkungan
            audio = recognizer.listen(source)  # Mendengarkan audio

            try:
                # Konversi audio menjadi teks menggunakan Google Web Speech API
                text = recognizer.recognize_google(audio, language="id-ID")
                print(text)
                if text == "a":
                    play_mp3(mp3_file_path)
                elif text == "b":
                    play_mp3(mp3_file_path1)
                elif text == "c":
                    play_mp3(mp3_file_path2)
                elif text == "d":
                    play_mp3(mp3_file_path3)
                elif text == "show gif":
                    gif_file_path = "D:/Tugas Kuliah/Semester 5/sample.gif"  # Ganti dengan path ke file GIF Anda
                    show_gif(gif_file_path)
                elif text == "stop":
                    break  # Menghentikan perulangan jika user mengucapkan "stop"
                else:
                    print("Robot: Ich habe das nicht verstanden.")
                    speak("Ich habe das nicht verstanden.")

            except sr.UnknownValueError:
                print("Leider kann ich Ihre Rede nicht erkennen.")
                speak("Leider kann ich Ihre Rede nicht erkennen.")
            except sr.RequestError as e:
                print("Im Spracherkennungsdienst ist ein Fehler aufgetreten; {0}".format(e))
                speak("Im Spracherkennungsdienst ist ein Fehler aufgetreten; {0}".format(e))

if __name__ == "__main__":
    speech_to_text()