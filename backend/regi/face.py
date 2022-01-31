from deepface import DeepFace
import pandas as pd
import os
import collections
import db_user
import shutil
from backend import settings
import datetime


def image_copy(src, db_path):
    dst = os.path.join(db_path, 'unknown/')
    if not os.path.isdir(dst):
        os.mkdir(dst)
    shutil.copy(src, dst)
    return dst


# 사용자 사진 등록 시 마다 pkl file 삭제 후 새로 갱신 필요
def del_face_pkl(user_id):
    path = "../whoareyou/my_db/{}/representations_arcface.pkl".format(user_id)
    if os.path.isfile(path):
        os.remove(path)

def face_recognition(img_path):
    # 라즈베리파이에서 찍힌 사진
    file_name = os.path.basename(img_path)

    # DB
    user_id = db_user.get_user_id()
    db_path = "../whoareyou/my_db/{}/".format(user_id)

    del_face_pkl(user_id)
    # 안면인식 모델
    try:
        df = DeepFace.find(img_path=img_path, db_path=db_path, model_name='ArcFace')
        # print(df)
    except:
        df = pd.DataFrame()
        # print(df)

    if len(df) > 0:
        # 안면인식결과에서 폴더명 가져옴
        tmp = []
        for i in df['identity']:
            path = os.path.dirname(i)
            folder = os.path.basename(path)
            tmp.append(folder)

        floder_count = collections.Counter(tmp)
        category = floder_count.most_common()[0][0]

        if category == 'family':
            print('가족입니다')
            danger = 0  # 안전
        else:
            print('가족이 아닙니다.')
            danger = 1  # 수상

    # table에 일치하는사람이 없으면 people table에 저장, image upload
    elif len(df) == 0:
        print('db에 일치하는 사람 없음')
        category = 'unknown'
        danger = 1  # 수상

        # image copy to unknown folder
        dst = image_copy(img_path, db_path)

        new_path = os.path.join(dst, file_name)
        category_num = 0
        pub_date = datetime.datetime.now()

        data = (category_num, danger, pub_date, new_path, user_id)  # category, danger, pub_date, pic, user_id
        db_user.insert_unknown(data)

    return category


# img = "C:/whoareyou/rasberry/1.jpg"
img = os.path.join(settings.IMAGES_DIR, 'rasberry/3.jpg')
category = face_recognition(img)
print(category)
