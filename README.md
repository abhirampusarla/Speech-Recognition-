# 🎙️ Speech-Based Sentiment Analysis

## 🧩 Introduction
This project focuses on implementing sentiment analysis on spoken input using Natural Language Processing (NLP). It captures audio from the microphone, converts it into text using speech recognition, and then analyzes the sentiment (positive, negative, or neutral) of the recognized text. The implementation also includes support for regional languages like Telugu.

## 🎯 Objective
### The main goal is to:
Record real-time audio from the user.
Convert speech into text using Google's Speech Recognition API.
Analyze the sentiment of the transcribed text using TextBlob.
Extend support to multiple languages (e.g., Telugu using "te-IN").
## 🛠️ Technologies Used
Python
SpeechRecognition – To convert speech to text.
TextBlob – For sentiment polarity analysis.
Google Speech API – As the backend recognizer.
Microphone (input device)
## 🧪 Implementation
### 1. Audio Recording

Uses speech_recognition.Microphone to capture audio input from the user.

with sr.Microphone() as source:
    audio = recognizer.listen(source)
### 2. Speech-to-Text Conversion

Uses recognizer.recognize_google() to convert the audio signal into textual data.

text = recognizer.recognize_google(audio, language="en-US")
### 3. Sentiment Analysis

Utilizes TextBlob to evaluate the sentiment polarity of the recognized text:

Positive (score > 0)
Negative (score < 0)
Neutral (score = 0)
blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity
### 4. Multilingual Support

The code includes functionality to change the language, demonstrated with "te-IN" for Telugu.

text = recognizer.recognize_google(audio, language="te-IN")
## ✅ Output Examples
Input Speech: "I love this weather!"
Recognized Text: "I love this weather!"
Sentiment: Positive
Input Speech: "This is terrible."
Recognized Text: "This is terrible."
Sentiment: Negative
## 🧾 Conclusion
This project showcases how to bridge audio input and textual sentiment analysis using Python. It demonstrates a simple yet powerful approach for enabling human-computer interaction via voice and supports multiple languages for broader usability. Future improvements can include:

Real-time sentiment dashboards,
Language translation support,
Context-based sentiment evaluation.
