import os
import yaml


# Utility functions
def get_path():
    file_path = os.path.dirname(os.path.realpath(__file__))
    root_path = os.path.dirname(os.path.dirname(file_path))
    return root_path


def format_yaml(template, config):
    """Replace in ${ENV_VAR} in template with value"""
    formatted = template
    for k, v in config.items():
        formatted = formatted.replace('${%s}' % k, v)
    return formatted


def get_config(config):
    """Import config file as dictionary"""

    config += '.yaml'

    server_dir_path = get_path()
    if not os.path.isabs(config):
        config = os.path.join(server_dir_path, 'etc/config/', config)

    with open(config, 'r') as stream:
        config_dict = yaml.load(stream)

    return config_dict