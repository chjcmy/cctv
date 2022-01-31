import paho.mqtt.client as mqtt;
import PIL
import PIL.Image as pilimg
from PIL import Image
import datetime
import ast
import os

from regi import face


def on_connect(client, userdata, flags, rc):
    print("connect.." + str(rc));
    if rc == 0:  # 0이 정상 연결 -> 구독신청
        client.subscribe("mydata/whoareyou/#");  # Topic명
    else:
        print("연결 실패");


def on_message(client, userdata, msg):
    if msg.topic == 'mydata/whoareyou/getimage':
        data = ast.literal_eval(msg.payload.decode())
        frame = data[0]
        filename = data[1]
        filePath = 'C:/Users/USER/Desktop/project3/lastback/backend/cctv/pictures/' + filename  # 이곳에 사진을 저장할 절대경로를 적으세요
        f = open(filePath, "wb");
        f.write(frame);
        f.close();
    elif msg.topic == 'mydata/whoareyou/getkeypad':
        data = ast.literal_eval(msg.payload.decode())
        keypad_touched_time = data[1]
        print('방문자가 키패드를 만졌습니다!!!!!!!' + keypad_touched_time)
    elif msg.topic == 'mydata/whoareyou/getdoorhandle':
        data = ast.literal_eval(msg.payload.decode())
        doorhandle_touched_time = data[1]
        print('방문자가 문고리를 돌렸습니다!!!!!!!' + doorhandle_touched_time)
        print(keypad_touched_time)
    # face
    f_category = face.face_recognition(filePath)
    # yolo

    # sensor

    # danger


mqttClient = mqtt.Client();
mqttClient.on_connect = on_connect;
mqttClient.on_message = on_message;
mqttClient.connect("192.168.0.68", 1883, 60);
