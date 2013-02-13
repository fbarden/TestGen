# -*- coding: iso-8859-1 -*-
import ConfigParser
import sys

def stringDevice(device, parameter) :
	return '<span style=" font-style:italic; color:' + config.get('Devices', device) + ';">' + parameter + '</span>'

def stringComment(line) :
	return '<span style=" color:#949494;">' + line.strip() + '</span>'

def stringMethod(method) :
	return '<span style="font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:italic;">' + method + '</span>'

if (len(sys.argv) == 2):
	filename = sys.argv[1]
else:
	filename = 'pd26_XXX.txt'

config = ConfigParser.RawConfigParser()
config.optionxform=str
config.read('parserConfig.conf')

method_list = config.options('Methods')
device_list = config.options('Devices')
#for method in method_list :
	#method = method.split()
	
#for method in method_list :
	#print method

testcase = open('pd26_XXX.txt', 'r').read()
testcase_lines = testcase.splitlines(True)

for line in testcase_lines :
	sys.stdout.write("<p>")
	if line.startswith('\n') :
		sys.stdout.write("<br />")
	if line.startswith('#') :
		sys.stdout.write(stringComment(line))
	else :
		line_words = line.split()
		for word in line_words :
			flag_match = False
			if word in method_list :
				sys.stdout.write(stringMethod(word))
				flag_match = True
			elif word.startswith('@@') :
				for device in device_list :
					if word.strip('@').startswith(device) :
						sys.stdout.write(stringDevice(device, word))
						flag_match = True
			if (not flag_match) :
				sys.stdout.write(word);
				
			sys.stdout.write(' ');
	print("</p>")
