from Tkinter import * 
from tkSimpleDialog import *
from tkFileDialog   import asksaveasfilename

from tkMessageBox import askokcancel

import interfaces
import paths
import devices

import os

class SendCLI_dialog(Dialog):

	def isCLI(self, s):
		if s.find(".cli") == -1:
			return False
		else:
			return True

	def body(self, master):
		self.CPE = StringVar()
		self.interface = StringVar()
		self.command = StringVar()
		self.arguments = StringVar()
		devices_list = devices.get_devices_list('SendCLI')
		devices_buttons = []
		interfaces_buttons = []
		Label(self, text='Device:').pack(anchor=NW)
		for dev in devices_list:
			devices_buttons.append(Radiobutton(self, text=dev , variable=self.CPE, value=devices.get_device_value('SendCLI', dev)))
		for button in devices_buttons:
			button.pack()
		devices_buttons[0].select()
		Label(self, text='Interface:').pack(anchor=NW)
		self.interfaces_list = interfaces.get_interfaces_list()
		for interface in self.interfaces_list:
			interfaces_buttons.append(Radiobutton(self, text=interface, variable=self.interface, value=interfaces.get_interface_value(interface), command=self.onInterfaceSelection))
		for button in interfaces_buttons:
			button.pack()
		interfaces_buttons[0].select()
		self.commandListbox = Listbox(self, selectmode=SINGLE, height=15)
		self.commandListbox.pack(anchor=W, side=LEFT)
		self.commandListbox.bind("<ButtonRelease-1>", self.onCommandSelection)
		self.command_label = Label(self, text="Teststep Description", height=15, justify=LEFT)
		self.command_label.pack()
		self.onInterfaceSelection()
		Label(self, text='Arguments:').pack(anchor=W)
		self.args = Entry(self)
		self.args.pack()
		return devices_buttons[0]

	def onInterfaceSelection(self):
		self.files_list = filter(self.isCLI, os.listdir("../../"+self.interface.get()))
		self.commandListbox.delete(0, END) # clear
		for item in self.files_list:
			self.commandListbox.insert(END, item)
	
	def onCommandSelection(self, event):
		self.command = self.files_list[int((self.commandListbox.curselection()[0]))]
		command_file = "../../"+self.interface.get()+self.command
		self.command_label.config(text= open(command_file, 'r').read())

	def apply(self):
		self.arguments = self.args.get()
		self.result = "SendCLI_v2.py " + self.CPE.get() + " -f " + self.interface.get() + self.command + " " + self.arguments + "\n"


class ScrolledText(Frame):
    def __init__(self, master=None, text='', file=None):
        Frame.__init__(self, master)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        self.settext(text, file)
    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)                  
        text.config(yscrollcommand=sbar.set)           
        sbar.pack(side=RIGHT, fill=Y)                   
        text.pack(side=LEFT, expand=YES, fill=BOTH)     
        self.text = text
    def settext(self, text='', file=None):
        if file: 
            text = open(file, 'r').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()
    def gettext(self):
        return self.text.get('1.0', END+'-1c')



class SimpleEditor(ScrolledText):
    def __init__(self, master=None, file=None): 
        frm = Frame(master)
        frm.pack(fill=X)

        menubar = Menu(master)      # Start - menu
        fileMenu = Menu(menubar, tearoff=0)
        editMenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="  File    ", menu=fileMenu)
        fileMenu.add_separator()
        fileMenu.add_command(label="  New", command=self.onNew)
        fileMenu.add_command(label="  Open", command=self.onOpen)
        fileMenu.add_separator()
        fileMenu.add_command(label="  Save As", command=self.onSave)
        fileMenu.add_separator()
        fileMenu.add_command(label="  Exit", command=self.onExit)
        master.config(menu=menubar)

        menubar.add_cascade(label="  Edit     ", menu=editMenu)
        editMenu.add_command(label='  Cut',   command=self.onCut)
        editMenu.add_command(label='  Paste', command=self.onPaste)
        editMenu.add_command(label='  Find',  command=self.onFind)
        master.config(menu=menubar)

        Button(frm, text='SendCLI_v2',   command=self.onSendCLI).pack(side=LEFT)
        Button(frm, text='TSWConfig', command=self.onTSWConfig).pack(side=LEFT)
        Button(frm, text='TSWStatus',  command=self.onTSWStatus).pack(side=LEFT)
        #Button(frm, text='Loop',  command=self.onLoop).pack(side=LEFT)
        #Button(frm, text='Time',  command=self.onTime).pack(side=LEFT)
        ScrolledText.__init__(self, master, file=file) 
        self.text.config(font=('courier', 9, 'normal'))
    def onNew(self):                # NEW - clear the text area
        self.text.delete(0.0, END)
    def onOpen(self):                   # OPEN - file
        fileName = askopenfilename()
        try:
            file = open(fileName, 'r')
            contents = file.read()

            self.text.delete(0.0, END)
            self.text.insert(0.0, contents)
        except:
            pass
    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()
            open(filename, 'w').write(alltext)
    def onCut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)
        self.text.delete(SEL_FIRST, SEL_LAST)
        self.clipboard_clear()
        self.clipboard_append(text)
    def onPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass
    def onFind(self):
        target = askstring('SimpleEditor', 'Search String?')
        if target:
            where = self.text.search(target, INSERT, END)  
            if where:
                print where
                pastit = where + ('+%dc' % len(target))
               #self.text.tag_remove(SEL, '1.0', END)
                self.text.tag_add(SEL, where, pastit)
                self.text.mark_set(INSERT, pastit)
                self.text.see(INSERT)
                self.text.focus()
    def onSendCLI(self):
        command = SendCLI_dialog(self.master)
        self.text.insert(INSERT, command.result)
    def onTSWStatus(self):
        text = "TSWConfig.py"
        self.text.insert(INSERT, text)
    def onTSWConfig(self):
        text = "TSWStatus.py"
        self.text.insert(INSERT, text)
    def onExit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)


if __name__ == '__main__':
    root = Tk()
    root.wm_title("Testcase Generator")
    try:
        editor = SimpleEditor(master=root, file=sys.argv[1])
	root.mainloop()
    except IndexError:
        editor = SimpleEditor(master=root)
	root.mainloop()

