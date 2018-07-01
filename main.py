import sys
from PyQt5.QtWidgets import QApplication
from GUI import App
from Training import Training

import multiprocessing

def AppDisplay():
    app = QApplication(sys.argv)
    ui_Form = App()
    ui_Form.show()
    sys.exit(app.exec_())

def ImageProcess():
    Training()


if __name__ == '__main__':

    process_1 = multiprocessing.Process(target=AppDisplay)
    process_2 = multiprocessing.Process(target=ImageProcess)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()






