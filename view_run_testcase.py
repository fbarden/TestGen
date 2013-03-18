# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/runTestcase.ui'
#
# Created: Sun Mar 17 18:35:12 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import threading
import socket

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_runTestcaseForm(object):

    def highlightCurrentLine(self, cursor, color):
        selection = QtGui.QTextEdit.ExtraSelection()
        lineColor = QtGui.QColor(color).lighter(160)
        selection.format.setBackground(lineColor)
        selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, QtCore.QVariant(True))
        selection.cursor = cursor
        selection.cursor.clearSelection()
        self.extraSelections.append(selection)
        self.runTestcaseBrowser.setExtraSelections(self.extraSelections)

    def listenTestAutomation(self) :
        self.extraSelections = []
        testAutomationListener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        testAutomationListener.bind(('127.0.0.1', 8981))
        teststep = None
        while (teststep!="End Testcase") :
            teststep = testAutomationListener.recv(1024)
            self.runTestcaseBrowser.append(teststep)
        cursor = self.runTestcaseBrowser.textCursor()
        cursor.movePosition(cursor.Start)
        teststep = None
        while (teststep!="End") :
            teststep = testAutomationListener.recv(10)
            if teststep=="Failed" :
                self.highlightCurrentLine(cursor, QtCore.Qt.red)
                cursor.movePosition(cursor.EndOfBlock)
                self.runTestcaseBrowser.setTextCursor(cursor)
                self.runTestcaseBrowser.insertPlainText("    | FAILED |")
                self.runTestcaseBrowser.insertHtml(("   <a href = \"pd26_XXX.txt\"> LOG </a>"))
                cursor.movePosition(cursor.NextBlock)
            if teststep=="Passed" :
                self.highlightCurrentLine(cursor, QtCore.Qt.green)
                cursor.movePosition(cursor.EndOfBlock)
                self.runTestcaseBrowser.setTextCursor(cursor)
                self.runTestcaseBrowser.insertPlainText("    | PASSED |")
                cursor.movePosition(cursor.NextBlock)

    def fillTestcase(self) :
        t = threading.Thread(target=self.listenTestAutomation, name='testAutomationListener')
        t.start()

    def setupUi(self, runTestcaseForm):
        runTestcaseForm.setObjectName(_fromUtf8("runTestcaseForm"))
        runTestcaseForm.resize(1046, 623)
        self.verticalLayout = QtGui.QVBoxLayout(runTestcaseForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(runTestcaseForm)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.runTestcaseBrowser = QtGui.QTextBrowser(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.runTestcaseBrowser.sizePolicy().hasHeightForWidth())
        self.runTestcaseBrowser.setSizePolicy(sizePolicy)
        self.runTestcaseBrowser.setObjectName(_fromUtf8("runTestcaseBrowser"))
        self.runTestcaseBrowser.setOpenLinks(False)
        self.logTextBrowser = QtGui.QTextBrowser(self.splitter)
        self.logTextBrowser.setAcceptRichText(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logTextBrowser.sizePolicy().hasHeightForWidth())
        self.logTextBrowser.setSizePolicy(sizePolicy)
        self.logTextBrowser.setObjectName(_fromUtf8("logTextBrowser"))
        self.verticalLayout.addWidget(self.splitter)
        self.fillTestcase()

        self.retranslateUi(runTestcaseForm)
        QtCore.QObject.connect(self.runTestcaseBrowser, QtCore.SIGNAL(_fromUtf8("anchorClicked(QUrl)")), self.logTextBrowser.setSource)
        QtCore.QMetaObject.connectSlotsByName(runTestcaseForm)

    def retranslateUi(self, runTestcaseForm):
        runTestcaseForm.setWindowTitle(QtGui.QApplication.translate("runTestcaseForm", "runTestcaseForm", None, QtGui.QApplication.UnicodeUTF8))

