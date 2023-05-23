# -*- coding: utf-8 -*-
import sys
import matplotlib.pyplot as plt
import struct, time

import numpy as np




from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess

from PyQt5.QtWidgets import QFileDialog

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 854)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.plot_box = QtWidgets.QGroupBox(self.centralwidget)
        self.plot_box.setGeometry(QtCore.QRect(11, 11, 1201, 801))
        self.plot_box.setObjectName("plot_box")

        self.plot_widget = QtWidgets.QWidget(self.plot_box)
        self.plot_widget.setGeometry(QtCore.QRect(10, 20, 1181, 771))
        self.plot_widget.setObjectName("plot_widget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 810, 321, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.select_file = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.select_file.setObjectName("select_file")
        self.select_file.clicked.connect(self.choose_file)

        self.horizontalLayout_2.addWidget(self.select_file)

        self.clear_the_plot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clear_the_plot.setObjectName("clear_the_plot")

        self.horizontalLayout_2.addWidget(self.clear_the_plot)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plot_box.setTitle(_translate("MainWindow", "Plot"))
        self.select_file.setText(_translate("MainWindow", "Select File"))
        self.clear_the_plot.setText(_translate("MainWindow", "Clear the Plot"))

    def choose_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;JPEG Files(*.jpeg);;\
                                                         PNG Files(*.png);;GIF File(*.gif);;All Files(*)")

    def ReadPHUFile(file_path, plot=False):
        """
        задается путь к фалу и ставиться флаг строить считыне кривые или нет
        возвращает массив кривых и кол-во кривых файле
        """
        # Tag Types
        tyEmpty8 = struct.unpack(">i", bytes.fromhex("FFFF0008"))[0]
        tyBool8 = struct.unpack(">i", bytes.fromhex("00000008"))[0]
        tyInt8 = struct.unpack(">i", bytes.fromhex("10000008"))[0]
        tyBitSet64 = struct.unpack(">i", bytes.fromhex("11000008"))[0]
        tyColor8 = struct.unpack(">i", bytes.fromhex("12000008"))[0]
        tyFloat8 = struct.unpack(">i", bytes.fromhex("20000008"))[0]
        tyTDateTime = struct.unpack(">i", bytes.fromhex("21000008"))[0]
        tyFloat8Array = struct.unpack(">i", bytes.fromhex("2001FFFF"))[0]
        tyAnsiString = struct.unpack(">i", bytes.fromhex("4001FFFF"))[0]
        tyWideString = struct.unpack(">i", bytes.fromhex("4002FFFF"))[0]
        tyBinaryBlob = struct.unpack(">i", bytes.fromhex("FFFFFFFF"))[0]

        inputfile = open(file_path, "rb")
        magic = inputfile.read(8).decode("ascii").strip('\0')
        if magic != "PQHISTO":
            print("ERROR: Magic invalid, this is not a PHU file.")
            exit(0)

        version = inputfile.read(8).decode("ascii").strip('\0')
        tagDataList = []  # Contains tuples of (tagName, tagValue)
        while True:
            tagIdent = inputfile.read(32).decode("ascii").strip('\0')
            tagIdx = struct.unpack("<i", inputfile.read(4))[0]
            tagTyp = struct.unpack("<i", inputfile.read(4))[0]
            if tagIdx > -1:
                evalName = tagIdent + '(' + str(tagIdx) + ')'
            else:
                evalName = tagIdent
            if tagTyp == tyEmpty8:
                inputfile.read(8)
                tagDataList.append((evalName, "<empty Tag>"))
            elif tagTyp == tyBool8:
                tagInt = struct.unpack("<q", inputfile.read(8))[0]
                if tagInt == 0:
                    tagDataList.append((evalName, "False"))
                else:
                    tagDataList.append((evalName, "True"))
            elif tagTyp == tyInt8:
                tagInt = struct.unpack("<q", inputfile.read(8))[0]
                tagDataList.append((evalName, tagInt))
            elif tagTyp == tyBitSet64:
                tagInt = struct.unpack("<q", inputfile.read(8))[0]
                tagDataList.append((evalName, tagInt))
            elif tagTyp == tyColor8:
                tagInt = struct.unpack("<q", inputfile.read(8))[0]
                tagDataList.append((evalName, tagInt))
            elif tagTyp == tyFloat8:
                tagFloat = struct.unpack("<d", inputfile.read(8))[0]
                tagDataList.append((evalName, tagFloat))
            elif tagTyp == tyFloat8Array:
                tagInt = struct.unpack("<q", inputfile.read(8))[0]
                tagDataList.append((evalName, tagInt))
            elif tagTyp == tyTDateTime:
                tagFloat = struct.unpack("<d", inputfile.read(8))[0]
                tagTime = int((tagFloat - 25569) * 86400)
                tagTime = time.gmtime(tagTime)
                tagDataList.append((evalName, tagTime))
            elif tagTyp == tyAnsiString:
                tagInt = struct.unpack("<q", inputfile.read(8))[0]
                tagString = inputfile.read(tagInt).decode("ascii").strip("\0")
                tagDataList.append((evalName, tagString))
            elif tagTyp == tyWideString:
                tagInt = struct.unpack("<q", inputfile.read(8))[0]
                tagString = inputfile.read(tagInt).decode("ascii").strip("\0")
                tagDataList.append((evalName, tagString))
            elif tagTyp == tyBinaryBlob:
                tagInt = struct.unpack("<q", inputfile.read(8))[0]
                tagDataList.append((evalName, tagInt))
            else:
                print("ERROR: Unknown tag type")
                exit(0)
            if tagIdent == "Header_End":
                break

        # Reformat the saved data for easier access
        tagNames = [tagDataList[i][0] for i in range(0, len(tagDataList))]
        tagValues = [tagDataList[i][1] for i in range(0, len(tagDataList))]

        # Write histogram data to file
        curveIndices = [tagValues[i] for i in range(0, len(tagNames)) \
                        if tagNames[i][0:-3] == "HistResDscr_CurveIndex"]
        curves = []
        for i in curveIndices:
            histogramBins = tagValues[tagNames.index("HistResDscr_HistogramBins(%d)" % i)]
            resolution = tagValues[tagNames.index("HistResDscr_MDescResolution(%d)" % i)]
            t = np.linspace(0, round(histogramBins * resolution * 1e9), histogramBins, False)
            hist_data = []
            for j in range(0, histogramBins):
                try:
                    histogramData = struct.unpack("<i", inputfile.read(4))[0]
                except:
                    print("The file ended earlier than expected, at bin %d/%d." \
                          % (j, histogramBins))
                hist_data.append(histogramData)

            curves.append(np.array([t, np.array(hist_data)]).transpose())

        inputfile.close()
        n = 0
        if plot:
            for i in curves:
                plt.plot(i[:, 0], i[:, 1], label=str(n))
                n += 1
            plt.xlabel("time, ns")
            plt.ylabel("Intensity, counts")
            plt.yscale("log")
            plt.grid()
            plt.legend()
            plt.show()

        return curves, n

    path = "phu_example.phu"

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
