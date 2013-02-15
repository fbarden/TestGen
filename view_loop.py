# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/loop.ui'
#
# Created: Thu Feb 14 19:20:20 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_loopDialog(object):
    def acceptLoop(self):
        variable = ""
        if (str(self.variableLineEdit.text()).startswith("@")) :
            variable = self.variableLineEdit.text()
        else :
            variable = "@" + self.variableLineEdit.text()
        from_value = str(self.fromLineEdit.text())
        to_value = str(self.toLineEdit.text())
        step_value = str(self.stepLineEdit.text())
        if (int(from_value) > int(to_value)) :
            relative_signal = ">="
            if (not step_value.startswith('-')) :
                step_value = " - "+step_value
        else :
            relative_signal = "<="
            if (not step_value.startswith('+')) :
                step_value = " + "+step_value

        result = "___BEGIN_LOOP___.py " + variable + "=" + from_value + "; " + variable + relative_signal + to_value + "; " + variable + "=" + variable + step_value + "\n\n" + "___END_LOOP___.py"
        return result

    def setupUi(self, loopDialog, parentUi):
        loopDialog.setObjectName(_fromUtf8("loopDialog"))
        loopDialog.resize(397, 192)
        self.verticalLayout = QtGui.QVBoxLayout(loopDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.loopLabel = QtGui.QLabel(loopDialog)
        self.loopLabel.setObjectName(_fromUtf8("loopLabel"))
        self.horizontalLayout.addWidget(self.loopLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.variableLabel = QtGui.QLabel(loopDialog)
        self.variableLabel.setObjectName(_fromUtf8("variableLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.variableLabel)
        self.variableLineEdit = QtGui.QLineEdit(loopDialog)
        self.variableLineEdit.setObjectName(_fromUtf8("variableLineEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.variableLineEdit)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.fromLabel = QtGui.QLabel(loopDialog)
        self.fromLabel.setObjectName(_fromUtf8("fromLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.fromLabel)
        self.fromLineEdit = QtGui.QLineEdit(loopDialog)
        self.fromLineEdit.setObjectName(_fromUtf8("fromLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.fromLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.toLabel = QtGui.QLabel(loopDialog)
        self.toLabel.setObjectName(_fromUtf8("toLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.toLabel)
        self.toLineEdit = QtGui.QLineEdit(loopDialog)
        self.toLineEdit.setObjectName(_fromUtf8("toLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.toLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.stepLabel = QtGui.QLabel(loopDialog)
        self.stepLabel.setObjectName(_fromUtf8("stepLabel"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.stepLabel)
        self.stepLineEdit = QtGui.QLineEdit(loopDialog)
        self.stepLineEdit.setObjectName(_fromUtf8("stepLineEdit"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.stepLineEdit)
        self.horizontalLayout_3.addLayout(self.formLayout_4)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(loopDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(loopDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), lambda : parentUi.acceptSendCLI(self.acceptLoop()))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), loopDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), loopDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(loopDialog)

    def retranslateUi(self, loopDialog):
        loopDialog.setWindowTitle(QtGui.QApplication.translate("loopDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.loopLabel.setText(QtGui.QApplication.translate("loopDialog", "___LOOP___", None, QtGui.QApplication.UnicodeUTF8))
        self.variableLabel.setText(QtGui.QApplication.translate("loopDialog", "Variable:", None, QtGui.QApplication.UnicodeUTF8))
        self.fromLabel.setText(QtGui.QApplication.translate("loopDialog", "From:", None, QtGui.QApplication.UnicodeUTF8))
        self.toLabel.setText(QtGui.QApplication.translate("loopDialog", "To:", None, QtGui.QApplication.UnicodeUTF8))
        self.stepLabel.setText(QtGui.QApplication.translate("loopDialog", "Step:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    loopDialog = QtGui.QDialog()
    ui = Ui_loopDialog()
    ui.setupUi(loopDialog)
    loopDialog.show()
    sys.exit(app.exec_())

