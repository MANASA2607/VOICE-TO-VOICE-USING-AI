import speech_recognition as sr

# Function to recognize speech from the microphone
def recognize_speech_from_mic(duration):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    print("Adjusting for ambient noise... Please wait.")
    # Use the microphone as source for input.
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        # Listen for the user's input
        audio = recognizer.listen(source, timeout=duration)
    print("Recognizing speech....")

    try:
        transcription = recognizer.recognize_google(audio)
        print(f"You said: {transcription}")
    except sr.RequestError:
        print("API unavailable")
    except sr.UnknownValueError:
        # Speech was unintelligible
        print("Unable to recognize speech")

# Call the function to recognize speech
recognize_speech_from_mic(duration=5)  # Set the duration for listening
