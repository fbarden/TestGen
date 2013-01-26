# -*- coding: iso-8859-1 -*-
import ConfigParser

import sys

if (len(sys.argv) == 2):
	config_file = sys.argv[1]
else:
	config_file = 'my_cpe.conf'

print config_file
new_config = ConfigParser.RawConfigParser()
old_config = ConfigParser.RawConfigParser()
new_config.read(config_file)
old_config.read('database/PD2600/cpe.conf')

sections = new_config.sections()

for thisSection in sections:
	options = new_config.options(thisSection)
	for thisOption in options:
		old_config.set(thisSection, thisOption, new_config.get(thisSection, thisOption))

if (new_config.has_option('PC 1', 'ethernet')):
	cpe_config = ConfigParser.RawConfigParser()
	cpe_config.read('cpe.conf')
	cpe_config.set('CPE 0', 'ethernet', new_config.get('PC 1', 'ethernet'))
	with open('cpe.conf', 'wb') as configfile:
	    cpe_config.write(configfile)

with open('database/PD2600/cpe.conf', 'wb') as configfile:
    old_config.write(configfile)

