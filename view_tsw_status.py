# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/tsw_status.ui'
#
# Created: Thu Feb 14 10:14:21 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import devices

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TSWStatusDialog(object):
    
    def createDeviceList(self, comboBox=None):
        if (comboBox==None) :
            comboBox = self.deviceComboBox
        device_list = devices.get_list()
        for device in device_list :
            if devices.has_method(device, "TSWStatus") :
                comboBox.addItem(_fromUtf8(device))

    def acceptTSWStatus(self):
        stream_param = ""
        direction_param = ""
        wait_param = ""
        end_param = ""
        reverse_flag = ""
        device = str(self.deviceComboBox.currentText())
        device_params = " " + devices.get_device_value(device, "TSWStatus", "1")
        if (self.streamLineEdit.text() != "") :
            stream_param = " -s " + str(self.streamLineEdit.text())
        direction_param = " -d " + str(self.directionComboBox.currentIndex() + 1)
        if (self.waitLineEdit.text() != "") :
            wait_param = " -w " + str(self.waitLineEdit.text())
        if (self.endLineEdit.text() != "") :
            end_param = " -e " + str(self.endLineEdit.text())
        if (self.reverseCheckBox.isChecked()) :
            reverse_flag = " -r 1"

        result = "TSWStatus.py" + device_params + stream_param + direction_param + wait_param + end_param + reverse_flag + "\n"
        return result

    def setupUi(self, TSWStatusDialog, parentUi):
        TSWStatusDialog.setObjectName(_fromUtf8("TSWStatusDialog"))
        TSWStatusDialog.resize(552, 246)
        self.verticalLayout = QtGui.QVBoxLayout(TSWStatusDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.TSWStatusLabel = QtGui.QLabel(TSWStatusDialog)
        self.TSWStatusLabel.setObjectName(_fromUtf8("TSWStatusLabel"))
        self.horizontalLayout_2.addWidget(self.TSWStatusLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.deviceLabel = QtGui.QLabel(TSWStatusDialog)
        self.deviceLabel.setObjectName(_fromUtf8("deviceLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.deviceLabel)
        self.deviceComboBox = QtGui.QComboBox(TSWStatusDialog)
        self.deviceComboBox.setObjectName(_fromUtf8("deviceComboBox"))
        self.createDeviceList(self.deviceComboBox)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.deviceComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.streamLabel = QtGui.QLabel(TSWStatusDialog)
        self.streamLabel.setObjectName(_fromUtf8("streamLabel"))
        self.gridLayout.addWidget(self.streamLabel, 0, 0, 1, 1)
        self.streamLineEdit = QtGui.QLineEdit(TSWStatusDialog)
        self.streamLineEdit.setObjectName(_fromUtf8("streamLineEdit"))
        self.gridLayout.addWidget(self.streamLineEdit, 0, 1, 1, 1)
        self.waitLabel = QtGui.QLabel(TSWStatusDialog)
        self.waitLabel.setObjectName(_fromUtf8("waitLabel"))
        self.gridLayout.addWidget(self.waitLabel, 0, 2, 1, 1)
        self.waitLineEdit = QtGui.QLineEdit(TSWStatusDialog)
        self.waitLineEdit.setObjectName(_fromUtf8("waitLineEdit"))
        self.gridLayout.addWidget(self.waitLineEdit, 0, 3, 1, 1)
        self.directionLabel = QtGui.QLabel(TSWStatusDialog)
        self.directionLabel.setObjectName(_fromUtf8("directionLabel"))
        self.gridLayout.addWidget(self.directionLabel, 1, 0, 1, 1)
        self.directionComboBox = QtGui.QComboBox(TSWStatusDialog)
        self.directionComboBox.setObjectName(_fromUtf8("directionComboBox"))
        self.directionComboBox.addItem(_fromUtf8(""))
        self.directionComboBox.addItem(_fromUtf8(""))
        self.directionComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.directionComboBox, 1, 1, 1, 1)
        self.endLabel = QtGui.QLabel(TSWStatusDialog)
        self.endLabel.setObjectName(_fromUtf8("endLabel"))
        self.gridLayout.addWidget(self.endLabel, 1, 2, 1, 1)
        self.endLineEdit = QtGui.QLineEdit(TSWStatusDialog)
        self.endLineEdit.setObjectName(_fromUtf8("endLineEdit"))
        self.gridLayout.addWidget(self.endLineEdit, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.reverseCheckBox = QtGui.QCheckBox(TSWStatusDialog)
        self.reverseCheckBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.reverseCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(TSWStatusDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TSWStatusDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), lambda : parentUi.acceptTeststep(self.acceptTSWStatus()))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TSWStatusDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TSWStatusDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TSWStatusDialog)

    def retranslateUi(self, TSWStatusDialog):
        TSWStatusDialog.setWindowTitle(QtGui.QApplication.translate("TSWStatusDialog", "TSWStatusDialog", None, QtGui.QApplication.UnicodeUTF8))
        self.TSWStatusLabel.setText(QtGui.QApplication.translate("TSWStatusDialog", "TSWStatus", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceLabel.setText(QtGui.QApplication.translate("TSWStatusDialog", "Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.streamLabel.setText(QtGui.QApplication.translate("TSWStatusDialog", "streams: -s", None, QtGui.QApplication.UnicodeUTF8))
        self.waitLabel.setText(QtGui.QApplication.translate("TSWStatusDialog", "wait: -w", None, QtGui.QApplication.UnicodeUTF8))
        self.directionLabel.setText(QtGui.QApplication.translate("TSWStatusDialog", "direction: -d", None, QtGui.QApplication.UnicodeUTF8))
        self.directionComboBox.setItemText(0, QtGui.QApplication.translate("TSWStatusDialog", "Port 1 (Unidirectional)", None, QtGui.QApplication.UnicodeUTF8))
        self.directionComboBox.setItemText(1, QtGui.QApplication.translate("TSWStatusDialog", "Port 2 (Unidirectional)", None, QtGui.QApplication.UnicodeUTF8))
        self.directionComboBox.setItemText(2, QtGui.QApplication.translate("TSWStatusDialog", "Bidirectional", None, QtGui.QApplication.UnicodeUTF8))
        self.endLabel.setText(QtGui.QApplication.translate("TSWStatusDialog", "end: -e", None, QtGui.QApplication.UnicodeUTF8))
        self.reverseCheckBox.setText(QtGui.QApplication.translate("TSWStatusDialog", "reverse (-r)", None, QtGui.QApplication.UnicodeUTF8))
