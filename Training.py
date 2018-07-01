from grabscreen import grab_screen
from getkeys import key_check
import os
import numpy as np
from PIL import ImageGrab
import cv2
import win32gui as win32g
import time



def keys_to_output(keys):
    output = [0, 0, 0, 0]

    if 'A' in keys:
        output[0] = 1
    elif 'S' in keys:
        output[1] = 1
    elif 'D' in keys:
        output[2] = 1
    elif 'W' in keys:
        output[3] = 1

    return output

class Training():
    def __init__(self):
        super().__init__()


        self.ImageProcess()

        print('훈련 시작')

    def ImageProcess(self):

        file_name = 'training_data.npy'
        # 이미 파일이 존재하면 기존데이터를 불러오고
        if os.path.isfile(file_name):
            print("File exist, loading previouss data!")
            training_data = list(np.load(file_name))
            # 없는 경우는 빈 리스트를 생성한다
        else:
            print('File does not exist, starting fresh')
            training_data = []

        hwnd = win32g.FindWindow(None, '바람의나라')
        win32g.SetForegroundWindow(hwnd)
        hwndsize = win32g.GetWindowRect(hwnd)
        # cap = np.array(ImageGrab.grab(hwndsize))

        while (True):
            cap = np.array(ImageGrab.grab(hwndsize))
            #time.sleep(0.2)
            # MainArea = cap[30:680, 5:815]
            # StatusArea = cap[690:720, 885:1010]

            # MainArea = cv2.cvtColor(MainArea, cv2.COLOR_RGB2GRAY)
            # tf_StatusArea = cv2.cvtColor(StatusArea, cv2.COLOR_RGB2GRAY)
            tf_CoordinateAreaX = cap[760:780, 918:945]
            tf_CoordinateAreaY = cap[760:780, 976:1003]
            tf_CoordinateAreaX = cv2.cvtColor(tf_CoordinateAreaX, cv2.COLOR_RGB2GRAY)
            tf_CoordinateAreaY = cv2.cvtColor(tf_CoordinateAreaY, cv2.COLOR_RGB2GRAY)

            # MainArea = cv2.resize(MainArea, (325, 405))

            keys = key_check()  # 조작하는 사람이 어떤 키를 누르는지 지켜보다가
            output = keys_to_output(keys)  # 특정키를 누르면 [0,1,0] 같은 행렬로 반환한다
            training_data.append([tf_CoordinateAreaX, tf_CoordinateAreaY, output])  # 그리고 학습데이터에 저장한다

            print(output)
            if len(training_data) % 500 == 0:  # 500번의 루프마다 file.npy에 저장한다
                print(len(training_data))
                np.save(file_name, training_data)



