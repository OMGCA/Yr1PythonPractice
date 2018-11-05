import sys
import os
import shutil
import cv2
from PyQt4.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        startb = QPushButton('Start Recording', self)
        startb.move(30, 140)

        stopb = QPushButton('Stop Recording ', self)
        stopb.move(150, 140)

        pInfo = QLabel('Reference Number:', self)
        pInfo.move(10, 50)

        Info1 = QLineEdit(self)
        Info1.move(120, 48)

        startb.clicked.connect(self.startRecording)
        stopb.clicked.connect(self.stopRecording)

        # set window position
        self.setGeometry(150, 100, 280, 170)
        self.setWindowTitle('Recording')
        self.show()
                
    def startRecording(self):
        source = self.sender()
        cap = cv2.VideoCapture(0)

        # Create folder
        os.makedirs('d:/test')
        # Define codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('p1.avi', fourcc, 20.0, (640, 480))

        while True:
            ret, frame = cap.read()
            out.write(frame)
            cv2.imshow('ClearSky', frame)
            cv2.waitKey(1)
            
        out.release()
        cap.release()
        cv2.destroyAllWindows()

        shutil.copy('d:/p1.avi', 'd:/test')

    def stopRecording(self):
        source = self.sender()
        sys.exit()       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
