# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/testgen.ui'
#
# Created: Thu Mar  7 10:46:40 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import view_edit_testcase as editTestcase
import paths

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):

    def openEditTestcase(self, parent, filename=None) :
        editTestcaseForm = QtGui.QWidget(parent)
        ui = editTestcase.Ui_editTestcaseForm()
        ui.setupUi(editTestcaseForm, filename)
        if filename==None :
            self.tabWidget.addTab(editTestcaseForm, "new_testcase")
        else :
            self.tabWidget.addTab(editTestcaseForm, filename.rpartition('/')[2])
            ui.loadFile(filename)

    def openTestcase(self, parent) :
        fileNames = QtGui.QFileDialog.getOpenFileNames(parent, ("Open File"),paths.get_testcases_path(),("All Files (pd*.txt)"));
        for fname in fileNames:
            self.openEditTestcase(parent, str(fname))

    def saveTestcase(self, parent) :
        if parent.count() == 0 :
            return
        widget = parent.currentWidget()
        filename = widget.objectName()
        if filename :
            with open(filename, 'w') as f :
                textEdit = widget.findChild(QtGui.QTextEdit, "testcaseTextEdit")
                f.write(textEdit.toPlainText())
        else :
            self.saveAsTestcase(parent)

    def saveAsTestcase(self, parent) :
        filename = QtGui.QFileDialog.getSaveFileName(parent, ("Save File"),paths.get_testcases_path(),("All Files (*)"));
        if not filename :
            return
        with open(filename, 'w') as f :
            widget = parent.currentWidget()
            widget.setObjectName(filename)
            parent.setTabText(parent.currentIndex(), str(filename).rpartition('/')[2])
            textEdit = widget.findChild(QtGui.QTextEdit, "testcaseTextEdit")
            f.write(textEdit.toPlainText())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTestcases = QtGui.QMenu(self.menubar)
        self.menuTestcases.setObjectName(_fromUtf8("menuTestcases"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
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
        self.menuTestcases.addAction(self.actionNew_Testcase)
        self.menuTestcases.addAction(self.actionOpen_Testcase)
        self.menuTestcases.addAction(self.actionSave_Testcase)
        self.menuTestcases.addAction(self.actionSave_as_Testcase)
        self.menuAbout.addAction(self.actionAbout_TestGen)
        self.menubar.addAction(self.menuTestcases.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.closeTabShortcut = QtGui.QShortcut(MainWindow)
        self.closeTabShortcut.setKey('CTRL+W')
        self.previousTabShortcut = QtGui.QShortcut(MainWindow)
        self.previousTabShortcut.setKey('CTRL+SHIFT+Tab')
        self.nextTabShortcut = QtGui.QShortcut(MainWindow)
        self.nextTabShortcut.setKey('CTRL+TAB')

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionNew_Testcase, QtCore.SIGNAL(_fromUtf8("triggered()")), lambda : self.openEditTestcase(self.tabWidget))
        QtCore.QObject.connect(self.actionOpen_Testcase, QtCore.SIGNAL(_fromUtf8("triggered()")), lambda : self.openTestcase(self.tabWidget))
        QtCore.QObject.connect(self.actionSave_Testcase, QtCore.SIGNAL(_fromUtf8("triggered()")), lambda : self.saveTestcase(self.tabWidget))
        QtCore.QObject.connect(self.actionSave_as_Testcase, QtCore.SIGNAL(_fromUtf8("triggered()")), lambda : self.saveAsTestcase(self.tabWidget))
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("tabCloseRequested(int)")), self.tabWidget.removeTab)
        QtCore.QObject.connect(self.closeTabShortcut, QtCore.SIGNAL(_fromUtf8("activated()")), lambda : self.tabWidget.removeTab(self.tabWidget.currentIndex()))
        QtCore.QObject.connect(self.previousTabShortcut, QtCore.SIGNAL(_fromUtf8("activated()")), lambda : self.tabWidget.setCurrentIndex((self.tabWidget.currentIndex()-1)%self.tabWidget.count()))
        QtCore.QObject.connect(self.nextTabShortcut, QtCore.SIGNAL(_fromUtf8("activated()")), lambda : self.tabWidget.setCurrentIndex((self.tabWidget.currentIndex()+1)%self.tabWidget.count()))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTestcases.setTitle(QtGui.QApplication.translate("MainWindow", "Testcases", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Testcase.setText(QtGui.QApplication.translate("MainWindow", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Testcase.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Testcase.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Testcase.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Testcase.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Testcase.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as_Testcase.setText(QtGui.QApplication.translate("MainWindow", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_TestGen.setText(QtGui.QApplication.translate("MainWindow", "About TestGen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTestcases.setText(QtGui.QApplication.translate("MainWindow", "Testcases", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())