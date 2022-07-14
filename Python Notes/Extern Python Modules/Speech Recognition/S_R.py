import speech_recognition as sr

#create an instance called 'r' of the sr.Recognizer class:

r=sr.Recognizer()
#-----------------------------------------------------------------
#Now we import the open as a source:

hello = sr.AudioFile('Audio_File.wav')

#No we create the audio_data instance:
#This is for a case that we are using an actual audio
#and not the input from the microphone.
#-----------------------------------------------------------------

with hello as source:
	audio_data = r.record(source)

#-----------------------------------------------------------------
#Here we have created the AudioData instance, called "audio_data"
#of the module speech_recognition.

#in order to print a text in the screen you need two things,
#an instance of the class sr.Recognizer and another one from the
#class speech_recognition.AudioData, now that we have them, lets
#use them with the google method as it follows:
#-----------------------------------------------------------------

print(r.recognize_google(audio_data))