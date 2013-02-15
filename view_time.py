# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/time.ui'
#
# Created: Thu Feb 14 19:39:19 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_timeDialog(object):

    def acceptTime(self):
        result = "___TIME___.py " + self.secondsLineEdit.text()
        return result

    def setupUi(self, timeDialog, parentUi):
        timeDialog.setObjectName(_fromUtf8("timeDialog"))
        timeDialog.resize(400, 108)
        self.verticalLayout = QtGui.QVBoxLayout(timeDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.timeLabel = QtGui.QLabel(timeDialog)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.horizontalLayout.addWidget(self.timeLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.secondsLabel = QtGui.QLabel(timeDialog)
        self.secondsLabel.setObjectName(_fromUtf8("secondsLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.secondsLabel)
        self.secondsLineEdit = QtGui.QLineEdit(timeDialog)
        self.secondsLineEdit.setObjectName(_fromUtf8("secondsLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.secondsLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(timeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(timeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), lambda : parentUi.acceptSendCLI(self.acceptTime()))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), timeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), timeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(timeDialog)

    def retranslateUi(self, timeDialog):
        timeDialog.setWindowTitle(QtGui.QApplication.translate("timeDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLabel.setText(QtGui.QApplication.translate("timeDialog", "___TIME___", None, QtGui.QApplication.UnicodeUTF8))
        self.secondsLabel.setText(QtGui.QApplication.translate("timeDialog", "Seconds:", None, QtGui.QApplication.UnicodeUTF8))
