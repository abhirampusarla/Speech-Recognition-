#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Implementation of Sentiment Analysis by recognising speech

import speech_recognition as sr
from textblob import TextBlob

# Initialize the recognizer
recognizer = sr.Recognizer()

# Record audio from the microphone
def record_audio():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
    return audio

# Perform speech recognition
def recognize_speech(audio):
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))
        return None

# Perform sentiment analysis
def analyze_sentiment(text):
    if text:
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        if sentiment_score > 0:
            print("Positive sentiment")
        elif sentiment_score < 0:
            print("Negative sentiment")
        else:
            print("Neutral sentiment")
    else:
        print("No text to analyze")

# Main function
def main():
    audio = record_audio()
    text = recognize_speech(audio)
    analyze_sentiment(text)

if __name__ == "__main__":
    main()


# In[2]:


# Recognizing Natural language other than Default Language.

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Recording audio from microphone
def record_audio():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
    return audio

# Performing speech recognition
def recognize_speech(audio, language="en-US"):
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language=language)
        print(text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error occurred: {e}")
        return None

# Main function
def main():
    audio = record_audio()
    text = recognize_speech(audio, language="te-IN")  
if __name__ == "__main__":
    main()


# In[ ]:




