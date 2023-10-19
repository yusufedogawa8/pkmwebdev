import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import pygame  # Import modul pygame
import time
import sys  # Import modul sys
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mp3_file_path = r"awal.mp3"

def set_system_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

# Set the system volume to reduce it by 6 dB (half volume)
set_system_volume(0.9)

def speak(text, lang='de'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    play_mp3("output.mp3")
    sys.exit()  # Keluar setelah selesai berbicara

def play_mp3(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def speech_to_text():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 1000

    print("Robot: Hallo! Ich bin Adyadroid. Klicken Sie auf „Start“, um die Aktivität zu starten.")
    speak("Hallo! Ich bin Adyadroid. Klicken Sie auf „Start“, um die Aktivität zu starten")

    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language="de-DE")
                text = text.lower()
                print(text)
                break
            except sr.UnknownValueError:
                error_message = "Robot: Entschuldigung, ich habe dich nicht verstanden."
                with open("error.txt", "w") as error_file:
                    error_file.write(error_message)
            except sr.RequestError as e:
                print("Robot: Es gab einen Fehler bei der Anfrage. {0}".format(e))

if __name__ == "__main__":
    speech_to_text()
