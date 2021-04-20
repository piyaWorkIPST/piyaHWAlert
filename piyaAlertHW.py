from playsound import playsound
import time

timeAlertNeeded = float(input("enter how much seconds you need for sound to be triggered (measured in seconds) : "))

while 3 > 2:
    time.sleep(timeAlertNeeded)

    playsound("stopHOMEWORK.mp3")

    print("Homework Break Alert!")