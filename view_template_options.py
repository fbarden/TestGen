# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/template_options.ui'
#
# Created: Wed Feb 27 13:16:08 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import templates
import math

class Ui_templateOptionsDialog(object):

    def createOptionButtons(self, parent, template, mode) :
        optionList = templates.get_options_list(template, mode)
        gridPosition = 0
        gridColumns = 1 #int(math.sqrt(len(optionList)))
        self.optionCheckBox = [0]*len(optionList)
        for option in optionList :
            optionIndex = templates.get_option_index(template, mode, option) - 1
            self.optionCheckBox[optionIndex] = QtGui.QCheckBox(parent)
            self.optionCheckBox[optionIndex].setObjectName(option + "CheckBox")
            self.optionCheckBox[optionIndex].setText(templates.get_option_name(template, mode, option))
            self.optionCheckBox[optionIndex].setChecked(templates.get_option_enable(template, mode, option))
        for checkBox in self.optionCheckBox :
            self.gridLayout.addWidget(checkBox, gridPosition/gridColumns, gridPosition%gridColumns, 1, 1)
            gridPosition += 1

    def createVariablesEdit(self, parent, template, mode) :
        variablesList = templates.get_variables_list(template, mode)
        gridPosition = 0
        gridColumns = 1 #int(math.sqrt(len(variablesList)))
        self.variablesLabel = [0]*len(variablesList)
        self.variablesLineEdit = [0]*len(variablesList)
        for variable in variablesList :
            variableIndex = variablesList.index(variable)
            self.variablesLabel[variableIndex] = QtGui.QLabel(parent)
            self.variablesLineEdit[variableIndex] = QtGui.QLineEdit(parent)
            self.variablesLabel[variableIndex].setObjectName(variable + "Label")
            self.variablesLineEdit[variableIndex].setObjectName(variable)
            self.variablesLabel[variableIndex].setText(templates.get_variable_value(template, mode, variable))
        for index in range(len(variablesList)) :
            self.gridLayout.addWidget(self.variablesLabel[index], gridPosition, 1, 1, 1)
            self.gridLayout.addWidget(self.variablesLineEdit[index], gridPosition, 2, 1, 1)
            gridPosition += 1

    def acceptTemplateOption(self, template, mode):
        result = ""
        optionList = templates.get_options_list(template, mode)
        orderedOptionList= [0]*len(optionList)
        variables = {}
        for variableEdit in self.variablesLineEdit :
            variables[variableEdit.objectName()] = str(variableEdit.text())
        for option in optionList :
            optionIndex = templates.get_option_index(template, mode, option) - 1
            orderedOptionList[optionIndex] = option
        for option in orderedOptionList :
            if self.optionCheckBox[orderedOptionList.index(option)].isChecked() :
				result += "#" + templates.get_option_name(template, mode, option) + "\n"
				result += templates.get_option_command(template, mode, option, variables) + "\n"
        return result

    def setupUi(self, templateOptionsDialog, return_address, template, mode):
        templateOptionsDialog.setObjectName("templateOptionsDialog")
        templateOptionsDialog.resize(400, 78)
        self.horizontalLayout = QtGui.QHBoxLayout(templateOptionsDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.createOptionButtons(templateOptionsDialog, template, mode)
        self.createVariablesEdit(templateOptionsDialog, template, mode)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(templateOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(templateOptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), lambda template = template, mode = mode : return_address.acceptTemplateOption(self.acceptTemplateOption(template, mode)))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), templateOptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), templateOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(templateOptionsDialog)

    def retranslateUi(self, templateOptionsDialog):
        templateOptionsDialog.setWindowTitle(QtGui.QApplication.translate("templateOptionsDialog", "Template Options", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    templateOptionsDialog = QtGui.QDialog()
    ui = Ui_templateOptionsDialog()
    ui.setupUi(templateOptionsDialog, None, 'Initialization', 'CPE')
    templateOptionsDialog.show()
    sys.exit(app.exec_())

