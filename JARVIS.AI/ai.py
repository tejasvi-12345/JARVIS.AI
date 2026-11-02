import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyautogui
import webbrowser
import os

# ---------------- TEXT TO SPEECH ----------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# ---------------- TAKE COMMAND ----------------
def take_command():
    listener = sr.Recognizer()
    listener.pause_threshold = 1
    listener.energy_threshold = 300

    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)

            audio = listener.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

        command = listener.recognize_google(audio, language="en-IN")
        command = command.lower()

        print("🧑 You said:", command)
        return command

    except sr.WaitTimeoutError:
        print("Timeout...")
        return ""

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""


# ---------------- MAIN LOGIC ----------------
def run_jarvis(command):

    # TIME
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    # OPEN CHROME
    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    # OPEN GOOGLE
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    # OPEN WHATSAPP
    elif "open whatsapp" in command or "open whats app" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    # OPEN INSTAGRAM
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    # OPEN YOUTUBE
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # OPEN LINKEDIN
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    # OPEN FACEBOOK
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    # OPEN GMAIL
    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    # OPEN CHATGPT
    elif "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    # OPEN GOOGLE MAPS
    elif "open maps" in command:
        speak("Opening Google Maps")
        webbrowser.open("https://www.google.com/maps/")

    # OPEN GITHUB
    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # VOLUME CONTROL
    elif "volume up" in command:
        pyautogui.press("volumeup")
        speak("Volume increased")

    elif "volume down" in command:
        pyautogui.press("volumedown")
        speak("Volume decreased")

    elif "mute" in command:
        pyautogui.press("volumemute")
        speak("Volume muted")

    # OPEN NOTEPAD
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    # OPEN CALCULATOR
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("start calc")

    # OPEN FILE EXPLORER
    elif "open file explorer" in command:
        speak("Opening File Explorer")
        os.system("start explorer")

    # OPEN SETTINGS
    elif "open settings" in command:
        speak("Opening Settings")
        os.system("start ms-settings:")



    # PLAY SONG
    elif command.startswith("play"):

        song = command.replace("play", "").strip()

        if song == "":
            speak("Please tell me the song name.")
        else:
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

    # WIKIPEDIA
    elif "who is" in command or "what is" in command:

        query = command.replace("who is", "")
        query = query.replace("what is", "").strip()

        try:
            info = wikipedia.summary(query, sentences=2)
            speak(info)

        except wikipedia.exceptions.DisambiguationError:
            speak("Please be more specific.")

        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find information.")

        except Exception:
            speak("Something went wrong.")

    

    # OPEN FACEBOOK
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    # OPEN GMAIL
    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    # OPEN CHATGPT
    elif "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    # OPEN GOOGLE MAPS
    elif "open maps" in command:
        speak("Opening Google Maps")
        webbrowser.open("https://maps.google.com")

    # OPEN GITHUB
    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # HELLO
    elif "hello" in command:
        speak("Hello Boss, how can I help you?")

    # SCREENSHOT
    elif "screenshot" in command:
        speak("Taking screenshot")

        image = pyautogui.screenshot()
        image.save("screenshot.png")

        speak("Screenshot saved successfully.")

    # SHUTDOWN
    elif "shutdown" in command:
        speak("Shutting down computer")
        os.system("shutdown /s /t 1")

    # RESTART
    elif "restart" in command:
        speak("Restarting computer")
        os.system("shutdown /r /t 1")

    # LOCK
    elif "lock" in command:
        speak("Locking computer")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    # EXIT
    elif "stop" in command or "exit" in command:
        speak("Goodbye Boss!")
        exit()

    # UNKNOWN
    else:
        speak("Sorry, I didn't understand that command.")


# ---------------- MAIN ----------------
if __name__ == "__main__":

    speak("Hello BOSS . Jarvis is now online for You.")

    while True:

        command = take_command()

        if command != "":
            run_jarvis(command)