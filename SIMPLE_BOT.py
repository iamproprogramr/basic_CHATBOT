
import pyttsx3
import wikipedia
print(">>>hi i am your personel chat bott assistance<<<")
voice= pyttsx3.init()
user=input("ask ma a question: ")
result= wikipedia.summary(user, sentences=3)
print(result)
voice.say(result)
voice.runAndWait()
