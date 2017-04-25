import os 
import json, requests
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

# setup path whcih contains the audio files
# Names should be: 0.mp3, 1.mp3, 2.mp3 and so on
soundPath = 'sounds'

# array of used pins for push buttons
inputs = [23, 24, 25, 12, 16, 20, 21, 26, 19, 13]

# setup the GPIO Pins from array
GPIO.setmode(GPIO.BCM)
for pin in inputs:
   GPIO.setup(pin, GPIO.IN)

# check if song is currently playing, pause if so and play soundfile, resume if song played before
def playSound(file):
    # stop mpg123 before to be sure that no other sound is played
    os.system('pkill -STOP mpg123')
    os.system('pkill -CONT mpg123')

    # check if there is something played with xmbc/osmc
    payload = {'jsonrpc': '2.0', 'method': 'Player.GetProperties', 'params': {'playerid': 0, 'properties': ['speed']}, 'id': 1}
    headers = {'content-type': 'application/json'}
    url = 'http://localhost:8080/jsonrpc'
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()
    speed = data['result']['speed']
    
    if speed == 1:
        os.system('xbmc-send --action="PlayerControl(Play)"')
        sleep(0.1)
    
    # play intro horn sound
    os.system('mpg123 -q horn.mp3')
    sleep(0.1)
    os.system('mpg123 -q ' + file)

    if speed == 1:   
        os.system('xbmc-send --action="PlayerControl(Play)"')

# Listen to GPIO inputs
while True:
    for index, num in enumerate(inputs):
        
        if (GPIO.input(num) == False):
            try:
                playSound(soundPath + '/' + str(index) + '.mp3')
            except:
                print('Could not play sound file: ' + str(index) + '.mp3')
    
    sleep(0.1)
