import os
import pychromecast
import socket
import subprocess
import time
from gtts import gTTS


device_name = "Google Home"
mp3_file_name = "voice.mp3"
ip = socket.gethostbyname(socket.gethostname())
port = 8888

# run server
proc = subprocess.Popen(f"python -m http.server {port}")
time.sleep(1)

# input text what you want googlehome to speak.
input = input("何て喋りましょうか？( extra 内のファイル名を指定するとその音声を使用します。)")

# get text from file if input was blank.
if not input:
    with open("./voice.txt", encoding="utf-8") as f:
        input = f.read()

# save as mp3 from input.
if input:
    tts = gTTS(text=input, lang='ja')
    tts.save(f'./{mp3_file_name}')

# use extra mp3 if input was file name.
file_name = f"./extra/{input}"
if os.path.isfile(file_name):
    mp3_file_name = file_name

# get device instance.
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names = [device_name])
cast = chromecasts[0]
cast.wait()

# send http request to local.
mc = cast.media_controller
mc.play_media(f'http://{ip}:{port}/sound.mp3', 'audio/mp3')
time.sleep(2)
mc.play_media(f'http://{ip}:{port}/{mp3_file_name}', 'audio/mp3')
mc.block_until_active()

# kill process.
proc.kill()
