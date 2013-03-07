# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/testgen.ui'
#
# Created: Sat Feb 16 12:00:09 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTestcases = QtGui.QMenu(self.menubar)
        self.menuTestcases.setObjectName(_fromUtf8("menuTestcases"))
        self.menuTestplan = QtGui.QMenu(self.menubar)
        self.menuTestplan.setObjectName(_fromUtf8("menuTestplan"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuDatabase = QtGui.QMenu(self.menubar)
        self.menuDatabase.setObjectName(_fromUtf8("menuDatabase"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Testcase = QtGui.QAction(MainWindow)
        self.actionNew_Testcase.setObjectName(_fromUtf8("actionNew_Testcase"))
        self.actionOpen_Testcase = QtGui.QAction(MainWindow)
        self.actionOpen_Testcase.setObjectName(_fromUtf8("actionOpen_Testcase"))
        self.actionSave_Testcase = QtGui.QAction(MainWindow)
        self.actionSave_Testcase.setObjectName(_fromUtf8("actionSave_Testcase"))
        self.actionSave_as_Testcase = QtGui.QAction(MainWindow)
        self.actionSave_as_Testcase.setObjectName(_fromUtf8("actionSave_as_Testcase"))
        self.actionAbout_TestGen = QtGui.QAction(MainWindow)
        self.actionAbout_TestGen.setObjectName(_fromUtf8("actionAbout_TestGen"))
        self.actionTestcases = QtGui.QAction(MainWindow)
        self.actionTestcases.setObjectName(_fromUtf8("actionTestcases"))
        self.actionTestplans = QtGui.QAction(MainWindow)
        self.actionTestplans.setObjectName(_fromUtf8("actionTestplans"))
        self.actionTestsuites = QtGui.QAction(MainWindow)
        self.actionTestsuites.setObjectName(_fromUtf8("actionTestsuites"))
        self.menuTestcases.addAction(self.actionNew_Testcase)
        self.menuTestcases.addAction(self.actionOpen_Testcase)
        self.menuTestcases.addAction(self.actionSave_Testcase)
        self.menuTestcases.addAction(self.actionSave_as_Testcase)
        self.menuAbout.addAction(self.actionAbout_TestGen)
        self.menuDatabase.addAction(self.actionTestcases)
        self.menuDatabase.addAction(self.actionTestplans)
        self.menuDatabase.addAction(self.actionTestsuites)
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuTestcases.menuAction())
        self.menubar.addAction(self.menuTestplan.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTestcases.setTitle(QtGui.QApplication.translate("MainWindow", "Testcases", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTestplan.setTitle(QtGui.QApplication.translate("MainWindow", "Testplan", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatabase.setTitle(QtGui.QApplication.translate("MainWindow", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Testcase.setText(QtGui.QApplication.translate("MainWindow", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Testcase.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Testcase.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as_Testcase.setText(QtGui.QApplication.translate("MainWindow", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_TestGen.setText(QtGui.QApplication.translate("MainWindow", "About TestGen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTestcases.setText(QtGui.QApplication.translate("MainWindow", "Testcases", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTestplans.setText(QtGui.QApplication.translate("MainWindow", "Testplans", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTestsuites.setText(QtGui.QApplication.translate("MainWindow", "Testsuites", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

