# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/template_modes.ui'
#
# Created: Wed Feb 27 13:16:07 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import view_template_options as templateOptions

import templates
import math

class Ui_templateModesDialog(object):

    def createModeButtons(self, parent, template) :
        modeList = templates.get_modes_list(template)
        gridPosition = 0
        gridColumns = int(math.sqrt(len(modeList)))+1
        self.modeLinkButton = [0]*len(modeList)
        for mode in modeList :
            modeIndex = modeList.index(mode)
            self.modeLinkButton[modeIndex] = QtGui.QCommandLinkButton(parent)
            self.modeLinkButton[modeIndex].setObjectName(mode + "LinkButton")
            self.modeLinkButton[modeIndex].setText(mode)
            self.gridLayout.addWidget(self.modeLinkButton[modeIndex], gridPosition/gridColumns, gridPosition%gridColumns, 1, 1)
            gridPosition += 1

    def openTemplateOptions(self, parent, return_address, template, mode) :
        templateOptionsDialog = QtGui.QDialog(parent)
        ui = templateOptions.Ui_templateOptionsDialog()
        ui.setupUi(templateOptionsDialog, return_address, template, mode)
        templateOptionsDialog.show()

    def acceptTemplateOption(self, result):
        self.parent.acceptTeststep(result)
        self.widget.accept()
        

    def setupUi(self, templateModesDialog, return_address, template):
        templateModesDialog.setObjectName("templateModesDialog")
        templateModesDialog.resize(589, 120)
        self.verticalLayout = QtGui.QVBoxLayout(templateModesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.createModeButtons(templateModesDialog, template)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 55, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.parent = return_address
        self.widget = templateModesDialog

        self.retranslateUi(templateModesDialog)
        for button in self.modeLinkButton :
            QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), lambda parent=templateModesDialog, return_address=self, template = template, mode=str(button.text()) : self.openTemplateOptions(parent, return_address, template, mode))
        QtCore.QMetaObject.connectSlotsByName(templateModesDialog)

    def retranslateUi(self, templateModesDialog):
        templateModesDialog.setWindowTitle(QtGui.QApplication.translate("templateModesDialog", "Template Mode", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    templateModesDialog = QtGui.QDialog()
    ui = Ui_templateModesDialog()
    ui.setupUi(templateModesDialog, None, 'Initialization')
    templateModesDialog.show()
    sys.exit(app.exec_())

