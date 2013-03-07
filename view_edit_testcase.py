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

import view_template_modes as templateModes

import testCaseParser
import templates

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_editTestcaseForm(object):

    def createTemplateButtons(self, parent):
        templateList = templates.get_templates_list()
        self.templateButtons = [0]*len(templateList)
        for template in templateList :
            templateIndex = templateList.index(template)
            self.templateButtons[templateIndex] = QtGui.QPushButton(parent)
            self.templateButtons[templateIndex].setObjectName(_fromUtf8(template)+"Button")
            self.templateButtons[templateIndex].setText(template)

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

    def openTemplateModes(self, parent, return_address, template) :
        templateModeDialog = QtGui.QDialog(parent)
        ui = templateModes.Ui_templateModesDialog()
        ui.setupUi(templateModeDialog, return_address, template)
        templateModeDialog.show()

    def acceptTeststep(self, returnString):
        self.testcaseTextEdit.blockSignals(True)
        self.testcaseTextEdit.insertPlainText(returnString)
        cursor = self.testcaseTextEdit.textCursor()
        cursor.movePosition(cursor.PreviousBlock)
        testCaseParser.highlightBlock(cursor)
        self.testcaseTextEdit.blockSignals(False)

    def updateText(self):
        self.testcaseTextEdit.blockSignals(True)
        cursor = self.testcaseTextEdit.textCursor()
        cursor.select(cursor.WordUnderCursor)
        testCaseParser.highlightBlock(cursor)
        self.testcaseTextEdit.blockSignals(False)

    def updateAllText(self):
        self.testcaseTextEdit.blockSignals(True)
        cursor = self.testcaseTextEdit.textCursor()
        cursor.select(cursor.WordUnderCursor)
        cursor.movePosition(cursor.Start)
        testCaseParser.highlightBlock(cursor)
        while (cursor.movePosition(cursor.NextBlock)) :
			testCaseParser.highlightBlock(cursor)
        self.testcaseTextEdit.blockSignals(False)

    def setupUi(self, editTestcaseForm):
        self.textChanged = False
        editTestcaseForm.setObjectName(_fromUtf8("editTestcaseForm"))
        editTestcaseForm.resize(579, 511)
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
        self.createTemplateButtons(editTestcaseForm)
        for button in self.templateButtons :
            self.verticalLayout.addWidget(button)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.updateTextShortcut = QtGui.QShortcut(editTestcaseForm)
        self.updateTextShortcut.setKey('F5')

        self.retranslateUi(editTestcaseForm)
        QtCore.QObject.connect(self.sendCLIButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openSendCLI(parent, return_address))
        QtCore.QObject.connect(self.TSWStatusButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openTSWStatus(parent, return_address))
        QtCore.QObject.connect(self.TSWConfigButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openTSWConfig(parent, return_address))
        QtCore.QObject.connect(self.loopButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openLoop(parent, return_address))
        QtCore.QObject.connect(self.timeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self: self.openTime(parent, return_address))
        QtCore.QObject.connect(self.testcaseTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), lambda : self.updateText())
        QtCore.QObject.connect(self.updateTextShortcut, QtCore.SIGNAL(_fromUtf8("activated()")), lambda : self.updateAllText())
        for button in self.templateButtons :
            QtCore.QObject.connect(button, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda parent=editTestcaseForm, return_address=self, template=str(button.text()) : self.openTemplateModes(parent, return_address, template))
        QtCore.QObject.connect(self.updateTextShortcut, QtCore.SIGNAL(_fromUtf8("activated()")), lambda : self.updateAllText())
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



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    editTestcaseForm = QtGui.QWidget()
    ui = Ui_editTestcaseForm()
    ui.setupUi(editTestcaseForm)
    editTestcaseForm.show()
    sys.exit(app.exec_())

