# -*- coding: iso-8859-1 -*-
from Tkinter import * 
from tkSimpleDialog import *

class run_testplan(Dialog):

	def body(self, master):
		buttons = []
		type = IntVar()
		buttons.append(Radiobutton(self, text="TestCase", variable=type, value="1", command=self.onTypeTestCaseSelection))
		buttons.append(Radiobutton(self, text="TestPlan", variable=type, value="2", command=self.onTypeTestPlanSelection))
		for i in range(len(buttons)):
			buttons[i].pack(side=TOP)
		buttons[0].select()
		return buttons[0]
		
	def onTypeTestCaseSelection(self):
		testcaseNumber = Entry(self)
		testcaseNumber.pack()

	def onTypeTestPlanSelection(self):
		pass


if __name__ == '__main__':
	root = Tk()
	root.wm_title("Run Testcase/Testplan")
	editor = run_testplan(root)
	root.mainloop()