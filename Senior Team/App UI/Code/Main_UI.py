# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1183, 809)
        self.main_backdrop = QtWidgets.QWidget(Form)
        self.main_backdrop.setGeometry(QtCore.QRect(10, 10, 1161, 791))
        self.main_backdrop.setStyleSheet("background-color : rgb(84, 84, 84)")
        self.main_backdrop.setObjectName("main_backdrop")
        self.main_header = QtWidgets.QWidget(self.main_backdrop)
        self.main_header.setGeometry(QtCore.QRect(40, 30, 1091, 81))
        self.main_header.setStyleSheet("background-color : rgb(129, 129, 129)")
        self.main_header.setObjectName("main_header")
        self.header = QtWidgets.QLabel(self.main_header)
        self.header.setGeometry(QtCore.QRect(170, 10, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.green_strip = QtWidgets.QWidget(self.main_header)
        self.green_strip.setGeometry(QtCore.QRect(950, 0, 31, 80))
        self.green_strip.setStyleSheet("background-color : rgb(109, 255, 69)")
        self.green_strip.setObjectName("green_strip")
        self.green_strip_2 = QtWidgets.QWidget(self.main_header)
        self.green_strip_2.setGeometry(QtCore.QRect(1000, 0, 31, 80))
        self.green_strip_2.setStyleSheet("background-color : rgb(109, 255, 69)")
        self.green_strip_2.setObjectName("green_strip_2")
        self.green_strip_3 = QtWidgets.QWidget(self.green_strip_2)
        self.green_strip_3.setGeometry(QtCore.QRect(50, 0, 31, 80))
        self.green_strip_3.setStyleSheet("background-color : rgb(109, 255, 69)")
        self.green_strip_3.setObjectName("green_strip_3")
        self.green_strip_4 = QtWidgets.QWidget(self.green_strip_2)
        self.green_strip_4.setGeometry(QtCore.QRect(0, 0, 31, 80))
        self.green_strip_4.setStyleSheet("background-color : rgb(109, 255, 69)")
        self.green_strip_4.setObjectName("green_strip_4")
        self.widget_2 = QtWidgets.QWidget(self.main_header)
        self.widget_2.setGeometry(QtCore.QRect(120, 0, 31, 80))
        self.widget_2.setStyleSheet("background-color : rgb(0, 170, 255)")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.main_header)
        self.widget_3.setGeometry(QtCore.QRect(70, 0, 31, 80))
        self.widget_3.setStyleSheet("background-color : rgb(0, 170, 255)")
        self.widget_3.setObjectName("widget_3")
        self.widget = QtWidgets.QWidget(self.main_backdrop)
        self.widget.setGeometry(QtCore.QRect(40, 140, 1091, 611))
        self.widget.setStyleSheet("background-color : rgb(129, 129, 129)")
        self.widget.setObjectName("widget")
        self.main_tabs = QtWidgets.QTabWidget(self.widget)
        self.main_tabs.setGeometry(QtCore.QRect(20, 0, 1071, 611))
        self.main_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_tabs.setTabsClosable(False)
        self.main_tabs.setMovable(True)
        self.main_tabs.setObjectName("main_tabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.frwrd_btn = QtWidgets.QPushButton(self.tab1)
        self.frwrd_btn.setGeometry(QtCore.QRect(350, 60, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.frwrd_btn.setFont(font)
        self.frwrd_btn.setStyleSheet("")
        self.frwrd_btn.setObjectName("frwrd_btn")
        self.right_btn = QtWidgets.QPushButton(self.tab1)
        self.right_btn.setGeometry(QtCore.QRect(650, 150, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.right_btn.setFont(font)
        self.right_btn.setObjectName("right_btn")
        self.bkwrd_btn = QtWidgets.QPushButton(self.tab1)
        self.bkwrd_btn.setGeometry(QtCore.QRect(360, 250, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bkwrd_btn.setFont(font)
        self.bkwrd_btn.setObjectName("bkwrd_btn")
        self.left_btn = QtWidgets.QPushButton(self.tab1)
        self.left_btn.setGeometry(QtCore.QRect(190, 150, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.left_btn.setFont(font)
        self.left_btn.setObjectName("left_btn")
        self.main_tabs.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.OBJ_dtct = QtWidgets.QWidget(self.tab2)
        self.OBJ_dtct.setGeometry(QtCore.QRect(130, 30, 761, 511))
        self.OBJ_dtct.setStyleSheet("background-color : rgb(84, 84, 84)")
        self.OBJ_dtct.setObjectName("OBJ_dtct")
        self.label = QtWidgets.QLabel(self.OBJ_dtct)
        self.label.setGeometry(QtCore.QRect(210, 450, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.main_tabs.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.Sentry_cam = QtWidgets.QWidget(self.tab3)
        self.Sentry_cam.setGeometry(QtCore.QRect(130, 30, 761, 511))
        self.Sentry_cam.setStyleSheet("background-color : rgb(84, 84, 84)")
        self.Sentry_cam.setObjectName("Sentry_cam")
        self.label_2 = QtWidgets.QLabel(self.Sentry_cam)
        self.label_2.setGeometry(QtCore.QRect(210, 450, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.main_tabs.addTab(self.tab3, "")

        self.retranslateUi(Form)
        self.main_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LOGIC GATE - CONTROL APPLICATION"))
        self.header.setText(_translate("Form", "LOGIC GATE - GEMS Cambridge International, Sharjah"))
        self.frwrd_btn.setText(_translate("Form", "Forward"))
        self.right_btn.setText(_translate("Form", "Right"))
        self.bkwrd_btn.setText(_translate("Form", "Backward"))
        self.left_btn.setText(_translate("Form", "Left"))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab1), _translate("Form", "Movement"))
        self.label.setText(_translate("Form", "VIDEO CAMERA "))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab2), _translate("Form", "Camera Feed"))
        self.label_2.setText(_translate("Form", "VIDEO CAMERA "))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.tab3), _translate("Form", "Sentry Mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
