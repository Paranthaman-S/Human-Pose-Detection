# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/spara/Downloads/Main_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import pyglet.media
from cvzone.FaceMeshModule import FaceMeshDetector
import csv
from datetime import datetime
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import cv2
import os
from PIL.ImageQt import ImageQt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1926, 969)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Livevideo = QtWidgets.QLabel(self.centralwidget)
        self.Livevideo.setGeometry(QtCore.QRect(60, 90, 1171, 651))
        self.Livevideo.setStyleSheet("background-color: rgb(215, 215, 215);")
        self.Livevideo.setText("")
        self.Livevideo.setObjectName("Livevideo")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1580, 620, 161, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(1580, 820, 161, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(1580, 720, 161, 51))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1380, 620, 151, 51))
        self.label_2.setStyleSheet("font: 14pt \"Sitka Display\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1380, 820, 141, 51))
        self.label_3.setStyleSheet("font: 14pt \"Sitka Display\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1380, 720, 161, 51))
        self.label_4.setStyleSheet("font: 14pt \"Sitka Display\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 770, 171, 71))
        self.pushButton.setStyleSheet("font: 14pt \"Sitka Display\";")
        self.pushButton.setObjectName("pushButton")
        
        # assuming you have created the push button and defined its properties
        self.pushButton.clicked.connect(self.runcode)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 35, 161, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Sitka Display\";")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1320, 50, 561, 361))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1530, 430, 171, 61))
        self.pushButton_2.setStyleSheet("font: 75 14pt \"Sitka Display\";")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.Test)    
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 1901, 911))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("360_F_511035263_v5UQodVFn2ZGQwsArjVdDevoC4sgdpOo.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.Displayoutput = QtWidgets.QLabel(self.centralwidget)
        self.Displayoutput.setGeometry(QtCore.QRect(1560, 520, 241, 51))
        self.Displayoutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Displayoutput.setText("")
        self.Displayoutput.setObjectName("Displayoutput")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1380, 520, 171, 51))
        self.label_6.setStyleSheet("font: 14pt \"Sitka Display\";\n"
"\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_8.raise_()
        self.Livevideo.raise_()
        self.lcdNumber.raise_()
        self.lcdNumber_2.raise_()
        self.lcdNumber_3.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.Displayoutput.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1926, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Left Eye Ratio :"))
        self.label_3.setText(_translate("MainWindow", "Mouth Ratio :"))
        self.label_4.setText(_translate("MainWindow", "Right Eye Ratio :"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.label_5.setText(_translate("MainWindow", "LIVE VIDEO :"))
        self.pushButton_2.setText(_translate("MainWindow", "TEST"))
        self.label_6.setText(_translate("MainWindow", "Output Display :"))

    def runcode(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 1280)
        cap.set(4, 720)

        detector = FaceMeshDetector(maxFaces=3)


        breakcount_s, breakcount_y = 0, 0
        counter_s, counter_y = 0, 0
        state_s, state_y = False, False

        sound = pyglet.media.load("alarm.wav", streaming=False)
            

        def alert():
            #cv2.rectangle(img, (700, 20), (1250, 80), (0, 0, 255), cv2.FILLED)
            #cv2.putText(img, "DROWSINESS ALERT!!!", (710, 60),
                        #cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
            # Get current date and time for the snapshot filename
            now = datetime.now()
            dtString = now.strftime("%d-%m-%Y_%H-%M-%S")
            
            # Set the file path to save the image
            filepath = os.path.join("C:/Users/spara/OneDrive/Desktop/drowsiness-detection-main/snapshot", f"snapshot_{dtString}.jpg")

            # Save snapshot to file
            cv2.imwrite(filepath, img)
            
            # Set the pixmap of label_7 with the captured image
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * img.shape[2], QtGui.QImage.Format_RGB888))
            pixmap = pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(QtCore.Qt.AlignCenter)

        def recordData(condition):  
            file = open("database.csv", "a", newline="")
            now = datetime.now()
            dtString = now.strftime("%d-%m-%Y %H:%M:%S")
            tuple = (dtString, condition)
            writer = csv.writer(file)
            writer.writerow(tuple)
            file.close()

        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)

            img, faces = detector.findFaceMesh(img, draw=False)

            if faces:
                face = faces[0]
                eyeLeft = [27, 23, 130, 243]  # up, down, left, right
                eyeRight = [257, 253, 463, 359]  # up, down, left, right
                mouth = [11, 16, 57, 287]  # up, down, left, right
                faceId = [27, 23, 130, 243, 257, 253, 463, 359, 11, 16, 57, 287]

                #calculate eye left distance ratio
                eyeLeft_ver, _ = detector.findDistance(face[eyeLeft[0]], face[eyeLeft[1]])
                eyeLeft_hor, _ = detector.findDistance(face[eyeLeft[2]], face[eyeLeft[3]])
                eyeLeft_ratio = int((eyeLeft_ver/eyeLeft_hor)*100)
                
                self.lcdNumber.display(eyeLeft_ratio)
                
                # calculate eye right distance ratio
                eyeRight_ver, _ = detector.findDistance(face[eyeRight[0]], face[eyeRight[1]])   
                eyeRight_hor, _ = detector.findDistance(face[eyeRight[2]], face[eyeRight[3]])
                eyeRight_ratio = int((eyeRight_ver / eyeRight_hor) * 100)
                
                self.lcdNumber_3.display(eyeRight_ratio)
                
                # calculate mouth distance ratio
                mouth_ver, _ = detector.findDistance(face[mouth[0]], face[mouth[1]])
                mouth_hor, _ = detector.findDistance(face[mouth[2]], face[mouth[3]])
                mouth_ratio = int((mouth_ver / mouth_hor) * 100)
                
                self.lcdNumber_2.display(mouth_ratio)

                #display text on image   cv2.rectangle(img, (30,20), (400,150), (0,255,255), cv2.FILLED)
                #def displayLeftEyeRatio(self, ratio):
                 #   cv2.putText(img, f'Eye Left Ratio: {eyeLeft_ratio}', (50, 60),
                  #              cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
                   # self.LeftEyeRatio.display(ratio)
                    
                #def displayRightEyeRatio(self, ratio):
                 #   cv2.putText(img, f'Eye Right Ratio: {eyeRight_ratio}', (50, 100),
                  #              cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                   # self.RightEyeRatio.display(ratio)
                
                #def displayMouthRatio(self, ratio):
                 #   cv2.putText(img, f'Eye Mouth Ratio: {mouth_ratio}', (50, 140),
                  #              cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                   # self.MouthRatio.display(ratio)

                #cv2.rectangle(img, (30, 200), (350, 300), (255,0,0), cv2.FILLED)
                #cv2.putText(img, f'Sleep Count: {counter_s}', (40, 240),
                 #           cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
                #cv2.putText(img, f'Yawn Count: {counter_y}', (40, 280),
                 #           cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

             
                #drowsiness detection logic

                #------------------------Eye-----------------------------
                if eyeLeft_ratio <= 60 and eyeRight_ratio <= 60:
                    breakcount_s += 1
                    if breakcount_s >= 50:
                        if state_s == False:
                            state_s = not state_s
                            start_time = datetime.now()
                else:
                    breakcount_s = 0
                    if state_s:
                        state_s = not state_s
                        elapsed_time = datetime.now() - start_time
                        if elapsed_time.total_seconds() >=2: 
                            alert()
                            counter_s += 1
                            recordData("sleep")

                # ------------------------Mouth-----------------------------
                if mouth_ratio > 40:
                    breakcount_y += 1
                    if breakcount_y >= 20: 
                        alert()
                        if state_y == False:
                            counter_y += 1
                            #sound.play()
                            recordData("Yawn")
                            state_y = not state_y
                else:
                    breakcount_y = 0
                    if state_y:
                        state_y = not state_y

                # print(f'Sleep Count = {counter_s}')
                # print(f'Yawn Count = {counter_y}')



                for id in faceId:
                    cv2.circle(img,face[id], 5, (0,0,255), cv2.FILLED)
                    
            #cv2.imshow("Image", img))
            key = cv2.waitKey(1) & 0xFF
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * img.shape[2], QtGui.QImage.Format_RGB888))
            self.Livevideo.setPixmap(pixmap)
            if key == ord('q'):
                break

        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()

    def Test(self):
        # Load the saved model
        model = tf.keras.models.load_model('saved_model')
    
        # Load the image from label
        pixmap = self.label.pixmap()
        image_path = 'C:/Users/spara/OneDrive/Desktop/drowsiness-detection-main/snapshot/image.jpg'  # Replace with the path to your image
        pixmap.save(image_path)
    
        # Process the image with the model
        for i in os.listdir('C:/Users/spara/OneDrive/Desktop/drowsiness-detection-main/snapshot'):
            img = image.load_img('C:/Users/spara/OneDrive/Desktop/drowsiness-detection-main/snapshot/'+i, target_size=(224, 224))
    
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            images = np.vstack([x])
            val = model.predict(images)
            if val.argmax() == 0:
                self.Displayoutput.setText("eyes closed")
            elif val.argmax() == 1:
                self.Displayoutput.setText("eyes opened")
            elif val.argmax() == 2:
               self.Displayoutput.setText("no yawn")
            else:
               self.Displayoutput.setText("yawn")
    
        # Convert the processed image to a QPixmap and set it to the label
        img_pixmap = QtGui.QPixmap.fromImage(ImageQt(img))
        img_pixmap = img_pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(img_pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

