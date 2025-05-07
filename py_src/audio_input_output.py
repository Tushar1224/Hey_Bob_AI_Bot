
import speech_recognition as sr

import win32com.client

def speak(audioString):
    print("Bob: "+audioString)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(audioString)

def check_device():
    # Check for available audio devices
    print("Available audio devices:")
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        # print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(i, name))
        print(i," : ",name)

    # Prompt user to select a device
    device_index = int(input("Select the device index you want to use: "))
    return device_index
    

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.energy_threshold=280  # minimum audio energy to consider for recording
        #r.dynamic_energy_threshold = True
        #r.dynamic_energy_adjustment_damping = 0.15
        r.dynamic_energy_ratio = 0.1
        #r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
        #r.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

        r.phrase_threshold = 0.1  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        #r.non_speaking_duration = 0 # seconds of non-speaking audio to keep on both sides of the recording

        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source,phrase_time_limit=4)
    
    data = ""
    try:
        print("Audio Recorded")
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language='en-IN')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        check=1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
    return data