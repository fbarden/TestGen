# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/edit_testcase.ui'
#
# Created: Tue Feb 12 19:39:34 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import view_send_cli as sendCLI
import view_tsw_status as TSWStatus
import view_tsw_config as TSWConfig
import view_loop as loop
import view_time as time
import testCaseParser

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_editTestcaseForm(object):

    def openSendCLI(self, parent, return_address):
        sendCLIDialog = QtGui.QDialog(parent)
        ui = sendCLI.Ui_sendCLIDialog()
        ui.setupUi(sendCLIDialog, return_address)
        sendCLIDialog.show()

    def openTSWStatus(self, parent, return_address):
        TSWStatusDialog = QtGui.QDialog(parent)
        ui = TSWStatus.Ui_TSWStatusDialog()
        ui.setupUi(TSWStatusDialog, return_address)
        TSWStatusDialog.show()

    def openTSWConfig(self, parent, return_address):
        TSWConfigDialog = QtGui.QDialog(parent)
        ui = TSWConfig.Ui_TSWConfigDialog()
        ui.setupUi(TSWConfigDialog, return_address)
        TSWConfigDialog.show()

    def openLoop(self, parent, return_address) :
        loopDialog = QtGui.QDialog(parent)
        ui = loop.Ui_loopDialog()
        ui.setupUi(loopDialog, return_address)
        loopDialog.show()

    def openTime(self, parent, return_address):
        timeDialog = QtGui.QDialog(parent)
        ui = time.Ui_timeDialog()
        ui.setupUi(timeDialog, return_address)
        timeDialog.show()

    def acceptTeststep(self, returnString):
        self.testcaseTextEdit.append(returnString)

    def updateText(self, text):
        textHTML = testCaseParser.plainToHTML(text)
        self.testcaseTextEdit.setHtml(textHTML)
        print "FOI"

    def setupUi(self, editTestcaseForm):
        editTestcaseForm.setObjectName(_fromUtf8("editTestcaseForm"))
        editTestcaseForm.resize(579, 511)
        self.parent = editTestcaseForm
        self.verticalLayout_2 = QtGui.QVBoxLayout(editTestcaseForm)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sendCLIButton = QtGui.QPushButton(editTestcaseForm)
        self.sendCLIButton.setObjectName(_fromUtf8("sendCLIButton"))
        self.horizontalLayout.addWidget(self.sendCLIButton)
        self.TSWConfigButton = QtGui.QPushButton(editTestcaseForm)
        self.TSWConfigButton.setObjectName(_fromUtf8("TSWConfigButton"))
        self.horizontalLayout.addWidget(self.TSWConfigButton)
        self.TSWStatusButton = QtGui.QPushButton(editTestcaseForm)
        self.TSWStatusButton.setObjectName(_fromUtf8("TSWStatusButton"))
        self.horizontalLayout.addWidget(self.TSWStatusButton)
        self.timeButton = QtGui.QPushButton(editTestcaseForm)
        self.timeButton.setObjectName(_fromUtf8("timeButton"))
        self.horizontalLayout.addWidget(self.timeButton)
        self.loopButton = QtGui.QPushButton(editTestcaseForm)
        self.loopButton.setObjectName(_fromUtf8("loopButton"))
        self.horizontalLayout.addWidget(self.loopButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.testcaseTextEdit = QtGui.QTextEdit(editTestcaseForm)
        self.testcaseTextEdit.setObjectName(_fromUtf8("testcaseTextEdit"))
        self.horizontalLayout_2.addWidget(self.testcaseTextEdit)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.templateButton_1 = QtGui.QPushButton(editTestcaseForm)
        self.templateButton_1.setObjectName(_fromUtf8("templateButton_1"))
        self.verticalLayout.addWidget(self.templateButton_1)
        self.templateButton_2 = QtGui.QPushButton(editTestcaseForm)
        self.templateButton_2.setObjectName(_fromUtf8("templateButton_2"))
        self.verticalLayout.addWidget(self.templateButton_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(editTestcaseForm)
        QtCore.QObject.connect(self.sendCLIButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openSendCLI(parent, return_address))
        QtCore.QObject.connect(self.TSWStatusButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openTSWStatus(parent, return_address))
        QtCore.QObject.connect(self.TSWConfigButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openTSWConfig(parent, return_address))
        QtCore.QObject.connect(self.loopButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openLoop(parent, return_address))
        QtCore.QObject.connect(self.timeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openTime(parent, return_address))
        QtCore.QObject.connect(self.testcaseTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), lambda : self.updateText(str(self.testcaseTextEdit.toPlainText())))
        QtCore.QMetaObject.connectSlotsByName(editTestcaseForm)
        editTestcaseForm.setTabOrder(self.testcaseTextEdit, self.timeButton)
        editTestcaseForm.setTabOrder(self.timeButton, self.loopButton)

    def retranslateUi(self, editTestcaseForm):
        editTestcaseForm.setWindowTitle(QtGui.QApplication.translate("editTestcaseForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.sendCLIButton.setText(QtGui.QApplication.translate("editTestcaseForm", "SendCLI", None, QtGui.QApplication.UnicodeUTF8))
        self.TSWConfigButton.setText(QtGui.QApplication.translate("editTestcaseForm", "TSWConfig", None, QtGui.QApplication.UnicodeUTF8))
        self.TSWStatusButton.setText(QtGui.QApplication.translate("editTestcaseForm", "TSWStatus", None, QtGui.QApplication.UnicodeUTF8))
        self.timeButton.setText(QtGui.QApplication.translate("editTestcaseForm", "___TIME___", None, QtGui.QApplication.UnicodeUTF8))
        self.loopButton.setText(QtGui.QApplication.translate("editTestcaseForm", "___LOOP___", None, QtGui.QApplication.UnicodeUTF8))
        self.testcaseTextEdit.setHtml(QtGui.QApplication.translate("editTestcaseForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt; font-style:italic;\">Crie aqui seu </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:italic;\">testcase</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.templateButton_1.setText(QtGui.QApplication.translate("editTestcaseForm", "Template 1", None, QtGui.QApplication.UnicodeUTF8))
        self.templateButton_2.setText(QtGui.QApplication.translate("editTestcaseForm", "Template 2", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    editTestcaseForm = QtGui.QWidget()
    ui = Ui_editTestcaseForm()
    ui.setupUi(editTestcaseForm)
    editTestcaseForm.show()
    sys.exit(app.exec_())

