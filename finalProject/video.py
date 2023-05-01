from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import pymysql
import os
import random

camera = PiCamera()
camera.vflip = True
pir = MotionSensor(4)
Host = "localhost"
User = "picam_user"
Password = "password"
Database = "picam"

going = True

while going == True:
    conn = pymysql.connect(host=Host, user=User, password=Password, database=Database)
    cur = conn.cursor()
    videoNum = random.randrange(0,1000000)
    pir.wait_for_motion()
    videoPath = "/home/kpomroy/Desktop/CS121/finalProject/static/video" + str(videoNum)
    print("Starting recording")
    camera.start_recording(videoPath + ".h264")
    sleep(26)
    camera.stop_recording()
    print("Stopped recording")

    #save to database
    query = f"INSERT INTO videos (path) VALUES ('video" + str(videoNum) + ".mp4')"
    cur.execute(query)
    conn.commit()
    conn.close()
    
    #make a copy of video as mp4
    os.system('ffmpeg -f h264 -i ' + videoPath + '.h264 -c:v copy ' + videoPath + '.mp4')

