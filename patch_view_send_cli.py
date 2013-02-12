import devices
import interfaces
import os

    def isCLI(self, s):
        if s.find(".cli") == -1:
            return False
        else:
            return True

    def createInterfaceList(self, comboBox=None):
        if (comboBox==None) :
        comboBox = self.interfaceComboBox
        interface_list = interfaces.get_list()
        for interface in interface_list :
        comboBox.addItem(_fromUtf8(interface[0]))

    def createDeviceList(self, comboBox=None):
        if (comboBox==None) :
        comboBox = self.deviceComboBox
        device_list = devices.get_list()
        for device in device_list :
            comboBox.addItem(_fromUtf8(device))

    def updateMethodList(self, interfaceSelection, listBox=None):
        if (listBox==None) :
        listBox = self.methodList
        listBox.clear()
        interface_dir = interfaces.get_interface_value(interfaceSelection)
        files_list = filter(self.isCLI, os.listdir(interface_dir))
        for file_name in files_list:
            item = QtGui.QListWidgetItem()
            item.setText(_fromUtf8(file_name))
            font = QtGui.QFont()
            font.setBold(False)
            font.setWeight(50)
            item.setFont(font)
            self.methodList.addItem(item)

    def updatePreview(self, commandSelection, interfaceSelection=None, previewBox=None):
        if (interfaceSelection==None) :
            interfaceSelection = self.interfaceComboBox.currentText()
        if (previewBox==None) :
            previewBox = self.previewTextEdit
        previewBox.clear()
        if (commandSelection=="") :
            return
        interface_dir = interfaces.get_interface_value(interfaceSelection)
        command_file = interface_dir+commandSelection
        command_preview = open(command_file, 'r').read()
        previewBox.setText(command_preview)


    def setupUi(self, Form):
        self.createDeviceList(self.deviceComboBox)
        self.createInterfaceList(self.interfaceComboBox)
        self.updateMethodList(self.interfaceComboBox.currentText(), self.methodList)

        QtCore.QObject.connect(self.interfaceComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.updateMethodList)
        QtCore.QObject.connect(self.methodList, QtCore.SIGNAL(_fromUtf8("currentTextChanged(QString)")), self.updatePreview)