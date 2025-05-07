from audio_input_output import recordAudio,speak
from time import ctime
from gemini_content import chat
	

			
				
# initialization
speak("Welcome to machine world") 
while 1:
    data = recordAudio()
    print(chat(data))
    speak(chat(data))