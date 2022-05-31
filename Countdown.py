#Countdown timer to play a song.
import time
from playsound import playsound 

def countdown(s):

    while s:
        mins, secs = divmod(s, 60) #divmod returns a quotient and remainder tuple
        print("{:02d}:{:02d}".format(mins, secs), end="\r")
        time.sleep(1)
        s -= 1
    print("Playing Sungba Remix ~ Asake ft. Burna Boy")
    playsound(r'C:\Users\Kitch Mensah-Bonsu\Desktop\sungba.mp3') # 'r'converts normal string to raw string

t = input("Enter time in seconds: ")
countdown(int(t))

