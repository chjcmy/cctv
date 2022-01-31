import torch
import argparse
from IPython.display import Image
import os
from glob import glob
import subprocess
import detect
import paho.mqtt.publish as publish


# val_img_list = glob('../yolo/test_images/*')
cnt = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='best.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='test_images/test_8.jpg', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum number of detections per image')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-crop', action='store_true', help='save cropped prediction boxes')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
    opt = parser.parse_args()
    print(opt)
    obj_list =  detect.detect(opt)

    # face_recognition 결과값 반환
    who = 'famil' # or 'known' or 'unknown'

    # 센서값 반환
    sensor = ["문고리센서값", "키패드센서값"]


    # 위험도 분류
    # 안전 - 0, 수상 - 1, 위험 - 2

    def danger(setList, who, sensor) :
        danger = 0
        # 0차 분류
        if who == 'family' :
            return 0
        else :
            if "knife" in setList or "bat" in setList :
                print("위험 : unknown1이 칼이나 몽둥이를 소지하고 있습니다")
                return 2
            elif len(sensor) :
                print("위험 : unknown1이 침입을 시도한 흔적이 있습니다")
                return 2
            elif len(setList) >= 2 :
                print("수상 : unknown1의 복장이 수상합니다")
                return 1

    print(danger(obj_list, who, sensor))
    data = str(danger(obj_list, who, sensor))
    publish.single("model_result", data, hostname="192.168.0.55")

    print("finished!!")

# for img in val_img_list:
#     cnt += 1
#     if cnt >7 :
#         break
#     val_img_path = img
    # !python detect.py --weights ../yolo/best.pt --img 416 --conf 0.2 --source "{val_img_path}"

print("finished")
