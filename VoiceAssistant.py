import pyttsx3 #text to speech library
import speech_recognition as sr #for speech recognization
import datetime 
import wikipedia #for wikipedia summary
import webbrowser #for searching query on browser
import os
import smtplib
import pyaudio
engine = pyttsx3.init() #object creation
rate = engine.getProperty('rate') #for set the rate/speed of voice
engine.setProperty('rate',180)
voices = engine.getProperty('voices') 
engine.setProperty('voices',voices[1].id) #for setting voice male(0) or female(1) 
engine.say('Hello. I am Nikk,Your assistant!')
engine.runAndWait()
print("\nask me anything !\n")
engine.say("how can i help you?")
engine.runAndWait()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def takeCommand():
	r = sr.Recognizer() #object for speech recognizing
	# user_input=""
	with sr.Microphone() as source:
		print("\nlistening....\n")
		speak("Listening")
		r.pause_threshold=1
		audio = r.listen(source)

	try:
		print("Recognizing...\n")
		speak("Recognizing")
		query = r.recognize_google(audio,language='hi-in') #found query on google
		print(f"said:- {query}\n") #will print what we said

	except Exception as e: #exception if machine did not understand what we said
		print("say that again please...\n")
		return "None"
	return query
if _name_ == "_main_":

	while True:
		query = takeCommand().lower() 
		sum=wikipedia.summary(query) #directly access the all wikipedia summary about query
		print(sum) #will print the summary of wikipedia
		speak(sum) #will speak the wikipedia summary