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

def get_option_command(template, mode, option):
    config_file = open_option_config(template, mode)
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