from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import pymysql
import os

#camera = PiCamera()
#pir = MotionSensor(4)
videoNum = 0
Host = "localhost"
User = "picam_user"
Password = "password"
Database = "picam"

conn = pymysql.connect(host=Host, user=User, password=Password, database=Database)

cur = conn.cursor()
going = True

while going == True:
    #pir.wait_for_motion()
    videoPath = "/home/kpomroy/Desktop/CS121/finalProject/videos/video" + str(videoNum)
    print("Starting recording")
    #camera.start_recording(videoPath + ".h264")
    #sleep(30)
    #camera.stop_recording()
    print("Stopped recording")
    videoNum+=1

    #save to database
    query = f"INSERT INTO videos (path) VALUES ('videos/video" + str(videoNum) + ".mp4')"
    cur.execute(query)
    conn.commit()
    conn.close()
    
    #make a copy of video as mp4
    os.system('ffmpeg -f h264 -i ' + videoPath + '.h264 -c:v copy ' + videoPath + '.mp4')

    going = False

