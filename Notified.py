import pyttsx3 
import datetime
import time
from win10toast import ToastNotifier  
toaster = ToastNotifier()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id) #For Male Voice
engine.setProperty('voice', voices[1].id) #For Female Voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def nowtime():
    strTime = datetime.datetime.now().strftime("%H")
    return strTime


nowtime = nowtime()



query = {
    "Wake UP": 6,
    "Brush ": 7,
    "have your breakfast": 9,
    "join class": 11,
    "Take Rest": 11,
    "Have Your Lunch": 14,
    "Join College Metting": 15
}


while True:
    for i in range(0, len(query)):
        task = tuple(query.items())[i][0]
        y = int(query.get(task))
        

        if y == int(nowtime):
            print(task+" at "+str(y))
            speak("it is,"+str(nowtime)+" ,now"+str(task))
            toaster.show_toast(str(task), "It is "+str(nowtime)+", now "+str(task), duration=10)
    time.sleep(3600)
