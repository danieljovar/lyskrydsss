#Statemachine til beskrivelse af livets gang
from gpiozero import LED,Button
from time import sleep
from multiprocessing import Process
from picamera import PiCamera
import datetime

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
EVred=LED(8)
EVgul=LED(7)
EVgreen=LED(1)
sleepy=2

button1=Button(16)
button2=Button(20)
button3=Button(21)


camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

def capture():
    timestamp = datetime.datetime.now().isoformat()
    camera.capture('/home/pi/foto/%s.jpg' % timestamp)

def foto():
    while True:
        if button1.value==1 and NSred.value==1:
            capture()
        elif button1.value == 1 and NSred.value == 1:
            capture()
        elif button2.value==1 and EVred.value==1:
            capture()
        elif button2.value==1 and EVred.value==1:
           capture()



print(NSred.value)
def redred(x):# UDGANGS PUNKT FOR LYSKRYDSET
    if x=="NS": #HVIS LYSKRYDSET KOMMER FRA NS SKAL DEN GÅ TIL EV
        x="EV"
        print("NS RED   EV RED")
        NSred.on()
        print(NSred.value,"      ",EVred.value)
        EVred.on()
        sleep(2)
        return EV()
    elif x=="EV": #HVIS LYSKRYDSET KOMMER FRA EV SKAL DEN GÅ TIL NS
        x="NS"
        print("NS RED   EV RED")
        NSred.on()
        print(NSred.value,"      ",EVred.value)
        EVred.on()
        sleep(2)
        return NS()

def NS():
    NSgul.on()
    NSred.on()
    print(NSred.value, "      ", EVred.value)
    sleep(2)
    return NS_GREEN()


def NS_GREEN():
    NSgreen.on()
    NSgul.off()
    NSred.off()
    print(NSred.value,"      ",EVred.value)
    sleep(3)
    return NS_GUL()

def NS_GUL():
    NSgul.on()
    NSgreen.off()
    print(NSred.value, "      ", EVred.value)
    sleep(2)
    NSgul.off()
    x="NS"
    return redred(x)

def EV():
    EVgul.on()
    print(NSred.value, "      ", EVred.value)
    sleep(2)
    return EV_GREEN()

def EV_GREEN():
    EVgul.off()
    EVred.off()
    EVgreen.on()
    print(NSred.value, "      ", EVred.value)
    sleep(3)
    return EV_GUL()

def EV_GUL():
    EVgul.on()
    EVgreen.off()
    sleep(2)
    EVgul.off()
    print(NSred.value, "      ", EVred.value)
    x="EV"
    return redred(x)

p = Process(target=foto)
p.start()

state=redred(x="EV")
while state: state=redred(x="EV")
