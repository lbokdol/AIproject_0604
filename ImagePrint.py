from PyQt5.QtCore import *
from PyQt5.QtGui import QImage
import win32gui as win32g
import numpy as np
from PIL import ImageGrab
import cv2

# GUI에 표시되는 이미지들을 갱신하기 위한 QThread
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)   #Signal
    changeStatusPixmap = pyqtSignal(QImage)
    changeCoordPixmap = pyqtSignal(QImage)

    def run(self):
        hwnd = win32g.FindWindow(None, 'Object')    # 프로그램을 찾는다 [Object = 찾을 프로그램 명]
        win32g.SetForegroundWindow(hwnd)    # 찾은 프로그램을 화면의 제일 위로 올린다 (활성화시킨다)

        while (True):
            hwndsize = win32g.GetWindowRect(hwnd)   # 프로그램의 크기를 갖는다
            cap = np.array(ImageGrab.grab(hwndsize))    #크기만큼의 화면을 가져온다 가져온 뒤 Numpy를 이용해 배열로 저장

            MainArea = cap[30:680, 5:815]   # 원하는만큼 화면을 자름
            Main_Screen = cv2.cvtColor(MainArea, cv2.COLOR_BGR2RGB) # QLabel에 넣기 위해 cv2를 이용해 BGR 이미지를 RGB로 바꾼다
            StatusArea = cap[690:720, 885:1010]
            Status_Screen = cv2.cvtColor(StatusArea, cv2.COLOR_BGR2RGB)
            CoordinateArea = cap[760:780, 890:1015]
            Coordinate_Screen = cv2.cvtColor(CoordinateArea, cv2.COLOR_BGR2RGB)

            qImg = QImage(Main_Screen.data, Main_Screen.shape[1], Main_Screen.shape[0], Main_Screen.shape[1] * 3,
                                 QImage.Format_RGB888) # QImage의 형태로 변환해서 저장
            statusImg = QImage(Status_Screen.data, Status_Screen.shape[1], Status_Screen.shape[0],
                                 Status_Screen.shape[1] * 3, QImage.Format_RGB888)
            coordImg = QImage(Coordinate_Screen.data, Coordinate_Screen.shape[1], Coordinate_Screen.shape[0],
                                 Coordinate_Screen.shape[1] * 3, QImage.Format_RGB888)

            resizeImage = qImg.scaled(256, 199, Qt.KeepAspectRatio) # GUI에서 표시될 때의 이미지 크기를 비율에 맞춰 조절
            resizestatus = statusImg.scaled(180, 60, Qt.KeepAspectRatio)
            resizecoord = coordImg.scaled(180, 30, Qt.KeepAspectRatio)

            self.changePixmap.emit(resizeImage) #Signal
            self.changeStatusPixmap.emit(resizestatus)
            self.changeCoordPixmap.emit(resizecoord)



            #if cv2.waitKey(25) & 0xFF == ord('q'):
                #cv2.destroyAllWindows()
                #break
