# -*- coding: iso-8859-1 -*-
import ConfigParser
import sys

if (len(sys.argv) == 2):
	filename = sys.argv[1]
else:
	filename = 'pd26_XXX.txt'

config = ConfigParser.RawConfigParser()
config.optionxform=str
config.read('parserConfig.conf')

method_list = config.options('Methods')
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
		sys.stdout.write('<span style=" color:#949494;">' + line.strip() + '</span>')
	else :
		line_words = line.split()
		for word in line_words :
			if word in method_list :
				sys.stdout.write('<span style="font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:italic;">' + word + '</span>')
			elif word.startswith('@@CPE_1') :
				sys.stdout.write('<span style=" font-style:italic; color:#0000ff;">' + word + '</span>')
			elif word.startswith('@@CPE_2') :
				sys.stdout.write('<span style=" font-style:italic; color:#ff0000;">' + word + '</span>')
			else :
				sys.stdout.write(word);
				
			sys.stdout.write(' ');
	print("</p>")
