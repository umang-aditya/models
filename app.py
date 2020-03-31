# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib

PATH_TO_TEST_IMAGES_DIR = pathlib.Path("models/research/object_detection/test_images")
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))
i = 0
threshold = 0.7
MODEL_NAME = 0
FILTER = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.open.setObjectName("open")
        self.Select = QtWidgets.QComboBox(self.centralwidget)
        self.Select.setGeometry(QtCore.QRect(670, 60, 91, 22))
        self.Select.setObjectName("Select")
        self.Select.addItem("")
        self.Select.setItemText(0, "Select Model")
        self.Select.addItem("")
        self.Select.addItem("")
        self.Select.addItem("")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(40, 210, 75, 23))
        self.next.setObjectName("next")
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(40, 350, 71, 21))
        self.prev.setObjectName("prev")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(40, 480, 75, 23))
        self.save.setObjectName("save")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(670, 210, 47, 13))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(670, 230, 47, 13))
        self.label2.setObjectName("label2")
        self.thres = QtWidgets.QLineEdit(self.centralwidget)
        self.thres.setGeometry(QtCore.QRect(740, 220, 31, 20))
        self.thres.setObjectName("thres")
        self.Filter = QtWidgets.QComboBox(self.centralwidget)
        self.Filter.setGeometry(QtCore.QRect(670, 300, 81, 21))
        self.Filter.setObjectName("Filter")
        self.Filter.addItem("")
        self.Filter.setItemText(0, "Label Filter")
        self.Filter.addItem("")
        self.Filter.addItem("")
        self.Filter.addItem("")
        self.Filter.addItem("")
        self.Filter.addItem("")
        self.Detect = QtWidgets.QPushButton(self.centralwidget)
        self.Detect.setGeometry(QtCore.QRect(660, 480, 111, 51))
        self.Detect.setObjectName("Detect")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(160, 50, 471, 461))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap(str(TEST_IMAGE_PATHS[0])))
        self.photo.setScaledContents(True)
        self.photo.setWordWrap(False)
        self.photo.setObjectName("photo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 101, 20))
        self.label.setObjectName("label")
        self.file_loc = QtWidgets.QLineEdit(self.centralwidget)
        self.file_loc.setGeometry(QtCore.QRect(20, 140, 113, 20))
        self.file_loc.setObjectName("file_loc")
        self.get_thresh = QtWidgets.QPushButton(self.centralwidget)
        self.get_thresh.setGeometry(QtCore.QRect(670, 250, 75, 23))
        self.get_thresh.setObjectName("get_thresh")
        self.get_model = QtWidgets.QPushButton(self.centralwidget)
        self.get_model.setGeometry(QtCore.QRect(670, 100, 75, 23))
        self.get_model.setObjectName("get_model")
        self.get_filter = QtWidgets.QPushButton(self.centralwidget)
        self.get_filter.setGeometry(QtCore.QRect(670, 340, 75, 23))
        self.get_filter.setObjectName("get_filter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.next.clicked.connect(self.show_next)
        self.prev.clicked.connect(self.show_prev)
        self.open.clicked.connect(self.open_file)
        self.get_thresh.clicked.connect(self.get_threshold)
        self.get_model.clicked.connect(self.select_model)
        self.get_filter.clicked.connect(self.select_filter)
        self.Detect.clicked.connect(self.detect_clicked)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open.setText(_translate("MainWindow", "Open Folder"))
        self.Select.setItemText(1, _translate("MainWindow", "FRCNN"))
        self.Select.setItemText(2, _translate("MainWindow", "Mobilenet"))
        self.Select.setItemText(3, _translate("MainWindow", "SSD"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.prev.setText(_translate("MainWindow", "Previous"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.label1.setText(_translate("MainWindow", "Detection"))
        self.label2.setText(_translate("MainWindow", "Threshold"))
        self.Filter.setItemText(1, _translate("MainWindow", "Person"))
        self.Filter.setItemText(2, _translate("MainWindow", "Cat"))
        self.Filter.setItemText(3, _translate("MainWindow", "Dog"))
        self.Filter.setItemText(4, _translate("MainWindow", "Bottle"))
        self.Filter.setItemText(5, _translate("MainWindow", "Chair"))
        self.Detect.setText(_translate("MainWindow", "Detect"))
        self.label.setText(_translate("MainWindow", "Iput Folder Location:"))
        self.get_thresh.setText(_translate("MainWindow", "Enter"))
        self.get_model.setText(_translate("MainWindow", "Enter"))
        self.get_filter.setText(_translate("MainWindow", "Enter"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        
    def show_next(self):
        global i
        i = i+1
        self.photo.setPixmap(QtGui.QPixmap(str(TEST_IMAGE_PATHS[i])))
        print(i)

    def show_prev(self):
        global i
        i = i-1
        self.photo.setPixmap(QtGui.QPixmap(str(TEST_IMAGE_PATHS[i])))
        print(i)
    
    def open_file(self):
        global i
        i = 0
        path = self.file_loc.text()
        print(path)
        global PATH_TO_TEST_IMAGES_DIR, TEST_IMAGE_PATHS
        PATH_TO_TEST_IMAGES_DIR = pathlib.Path(path)
        TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))
        TEST_IMAGE_PATHS
       
    def get_threshold(self):
        global threshold
        threshold = self.thres.text()
        print(threshold)
        
    def detect_clicked(self):
        pass
    
    def select_model(self):
        global MODEL_NAME
        MODEL_NAME = self.Select.currentText()
        print(MODEL_NAME)
        
    def select_filter(self):
        global FILTER
        FILTER = self.Filter.currentText()
        print(FILTER)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
