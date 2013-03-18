import ConfigParser

templates_file = 'config/templates.conf'

def open_template_config():
    config_file = ConfigParser.SafeConfigParser()
    config_file.optionxform=str
    config_file.read(templates_file)
    return config_file

def open_option_config(template, mode):
    mode_path = get_mode_value(template, mode)
    config_file = ConfigParser.SafeConfigParser()
    config_file.optionxform=str
    config_file.read(mode_path)
    return config_file

def get_templates_list():
    config_file = open_template_config()
    return config_file.sections()

def get_modes_list(template):
    config_file = open_template_config()
    return config_file.options(template)

def get_mode_value(template, mode):
    config_file = open_template_config()
    return config_file.get(template, mode)

def has_mode(template, mode):
    config_file = open_template_config()
    return config_file.has_option(template, mode)

def get_options_list(template, mode):
    config_file = open_option_config(template, mode)
    options = config_file.sections()
    return options

def get_variables_list(template, mode):
    config_file = open_option_config(template, mode)
    if not(config_file.has_option('DEFAULT', 'variables')) :
		return None
    variables_string = config_file.get('DEFAULT', 'variables')
    variable_list = variables_string.split(',')
    for var in variable_list :
        index = variable_list.index(var)
        variable_list[index] = var.strip()
    return variable_list

def get_option_command(template, mode, option, variables = {}):
    config_file = open_option_config(template, mode)
    if variables != {} :
        for var in variables :
            config_file.set('DEFAULT', var, variables[var])
    return config_file.get(option, 'command')

def get_option_name(template, mode, option):
    config_file = open_option_config(template, mode)
    return config_file.get(option, 'name')

def get_option_enable(template, mode, option):
    config_file = open_option_config(template, mode)
    return config_file.getboolean(option, 'enable')

def get_option_index(template, mode, option):
    config_file = open_option_config(template, mode)
    return config_file.getint(option, 'index')

def get_variable_value(template, mode, variable):
    config_file = open_option_config(template, mode)
    return config_file.get('DEFAULT', variable)