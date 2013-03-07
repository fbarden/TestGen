# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/tsw_config.ui'
#
# Created: Thu Feb 14 15:15:11 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import devices

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TSWConfigDialog(object):

    def createDeviceList(self, comboBox=None):
        if (comboBox==None) :
            comboBox = self.deviceComboBox
        device_list = devices.get_list()
        for device in device_list :
            if devices.has_method(device, "TSWConfig") :
                comboBox.addItem(_fromUtf8(device))

    def acceptTSWConfig(self):
        stream_param = ""
        rate_param = ""
        frame_size_param = ""
        link_param = ""
        type_param = ""
        negotiate_flag = ""
        flow_controle_flag = ""
        device = str(self.deviceComboBox.currentText())
        device_params = " " + devices.get_device_value(device, "TSWConfig")
        if (self.streamLineEdit.text() != "") :
            stream_param = " -s " + str(self.streamLineEdit.text())
        if (self.rateLineEdit.text() != "") :
            rate_param = " -r " + str(self.rateLineEdit.text())
        if (self.frameSizeLineEdit.text() != "") :
            frame_size_param = " -f " + str(self.frameSizeLineEdit.text())
        if (self.linkComboBox.currentText() != "") :
            link_param = " -l " + str(self.linkComboBox.currentText())
        if (self.typeComboBox.currentText() != "") :
            type_param = " -t " + str(self.typeComboBox.currentText())
        if (self.negotiateCheckBox.isChecked()) :
            negotiate_flag = " -n yes"
        else :
            negotiate_flag = " -n no"
        if (self.flowControlCheckBox.isChecked()) :
            flow_controle_flag = " -c yes"
        else :
            flow_controle_flag = " -c no"
        result = "TSWConfig.py" + device_params + stream_param + rate_param + frame_size_param + link_param + type_param + negotiate_flag + flow_controle_flag + "\n"
        return result

    def setupUi(self, TSWConfigDialog, parentUi):
        TSWConfigDialog.setObjectName("TSWConfigDialog")
        TSWConfigDialog.resize(562, 247)
        self.verticalLayout_5 = QtGui.QVBoxLayout(TSWConfigDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.TSWConfigLabel = QtGui.QLabel(TSWConfigDialog)
        self.TSWConfigLabel.setObjectName("TSWConfigLabel")
        self.horizontalLayout_2.addWidget(self.TSWConfigLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.deviceLabel = QtGui.QLabel(TSWConfigDialog)
        self.deviceLabel.setObjectName("deviceLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.deviceLabel)
        self.deviceComboBox = QtGui.QComboBox(TSWConfigDialog)
        self.deviceComboBox.setObjectName("deviceComboBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.deviceComboBox)
        self.createDeviceList(self.deviceComboBox)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.streamLabel = QtGui.QLabel(TSWConfigDialog)
        self.streamLabel.setObjectName("streamLabel")
        self.verticalLayout_2.addWidget(self.streamLabel)
        self.rateLabel = QtGui.QLabel(TSWConfigDialog)
        self.rateLabel.setObjectName("rateLabel")
        self.verticalLayout_2.addWidget(self.rateLabel)
        self.frameSizeLabel = QtGui.QLabel(TSWConfigDialog)
        self.frameSizeLabel.setObjectName("frameSizeLabel")
        self.verticalLayout_2.addWidget(self.frameSizeLabel)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.streamLineEdit = QtGui.QLineEdit(TSWConfigDialog)
        self.streamLineEdit.setObjectName("streamLineEdit")
        self.verticalLayout.addWidget(self.streamLineEdit)
        self.rateLineEdit = QtGui.QLineEdit(TSWConfigDialog)
        self.rateLineEdit.setObjectName("rateLineEdit")
        self.verticalLayout.addWidget(self.rateLineEdit)
        self.frameSizeLineEdit = QtGui.QLineEdit(TSWConfigDialog)
        self.frameSizeLineEdit.setObjectName("frameSizeLineEdit")
        self.verticalLayout.addWidget(self.frameSizeLineEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.linkLabel = QtGui.QLabel(TSWConfigDialog)
        self.linkLabel.setObjectName("linkLabel")
        self.verticalLayout_4.addWidget(self.linkLabel)
        self.typeLabel = QtGui.QLabel(TSWConfigDialog)
        self.typeLabel.setObjectName("typeLabel")
        self.verticalLayout_4.addWidget(self.typeLabel)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.linkComboBox = QtGui.QComboBox(TSWConfigDialog)
        self.linkComboBox.setObjectName("linkComboBox")
        self.linkComboBox.addItem("")
        self.linkComboBox.addItem("")
        self.linkComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.linkComboBox)
        self.typeComboBox = QtGui.QComboBox(TSWConfigDialog)
        self.typeComboBox.setObjectName("typeComboBox")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.typeComboBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.negotiateCheckBox = QtGui.QCheckBox(TSWConfigDialog)
        self.negotiateCheckBox.setObjectName("negotiateCheckBox")
        self.horizontalLayout.addWidget(self.negotiateCheckBox)
        self.flowControlCheckBox = QtGui.QCheckBox(TSWConfigDialog)
        self.flowControlCheckBox.setObjectName("flowControlCheckBox")
        self.horizontalLayout.addWidget(self.flowControlCheckBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(TSWConfigDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(TSWConfigDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), lambda : parentUi.acceptTeststep(self.acceptTSWConfig()))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TSWConfigDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TSWConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TSWConfigDialog)

    def retranslateUi(self, TSWConfigDialog):
        TSWConfigDialog.setWindowTitle(QtGui.QApplication.translate("TSWConfigDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.TSWConfigLabel.setText(QtGui.QApplication.translate("TSWConfigDialog", "TSWConfig", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceLabel.setText(QtGui.QApplication.translate("TSWConfigDialog", "Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.streamLabel.setText(QtGui.QApplication.translate("TSWConfigDialog", "streams: -s", None, QtGui.QApplication.UnicodeUTF8))
        self.rateLabel.setText(QtGui.QApplication.translate("TSWConfigDialog", "rate: -r", None, QtGui.QApplication.UnicodeUTF8))
        self.frameSizeLabel.setText(QtGui.QApplication.translate("TSWConfigDialog", "frame size: -f", None, QtGui.QApplication.UnicodeUTF8))
        self.linkLabel.setText(QtGui.QApplication.translate("TSWConfigDialog", "link: -l", None, QtGui.QApplication.UnicodeUTF8))
        self.typeLabel.setText(QtGui.QApplication.translate("TSWConfigDialog", "type: -t", None, QtGui.QApplication.UnicodeUTF8))
        self.linkComboBox.setItemText(0, QtGui.QApplication.translate("TSWConfigDialog", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.linkComboBox.setItemText(1, QtGui.QApplication.translate("TSWConfigDialog", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.linkComboBox.setItemText(2, QtGui.QApplication.translate("TSWConfigDialog", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.typeComboBox.setItemText(0, QtGui.QApplication.translate("TSWConfigDialog", "factory", None, QtGui.QApplication.UnicodeUTF8))
        self.typeComboBox.setItemText(1, QtGui.QApplication.translate("TSWConfigDialog", "storm_broad", None, QtGui.QApplication.UnicodeUTF8))
        self.typeComboBox.setItemText(2, QtGui.QApplication.translate("TSWConfigDialog", "default", None, QtGui.QApplication.UnicodeUTF8))
        self.typeComboBox.setItemText(3, QtGui.QApplication.translate("TSWConfigDialog", "ipv4", None, QtGui.QApplication.UnicodeUTF8))
        self.negotiateCheckBox.setText(QtGui.QApplication.translate("TSWConfigDialog", "negotiate (-n)", None, QtGui.QApplication.UnicodeUTF8))
        self.flowControlCheckBox.setText(QtGui.QApplication.translate("TSWConfigDialog", "flow control (-c)", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TSWConfigDialog = QtGui.QDialog()
    ui = Ui_TSWConfigDialog()
    ui.setupUi(TSWConfigDialog)
    TSWConfigDialog.show()
    sys.exit(app.exec_())

