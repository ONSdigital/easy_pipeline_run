# Core imports
import argparse
from configparser import ConfigParser

###########################
# Configuration and Setup #
###########################

# Choose the config file via a command line argument
parser = argparse.ArgumentParser(description='Choose the config file')
parser.add_argument('--config-file', dest="conf_file", nargs='?', default="default_config.ini",
                    help='Choose the config file. Either default or other')
args = parser.parse_args()

# Take the config to use from the command line arguments
conf_file = args.conf_file
# Config files must be saved in the config folder
if conf_file != "":
    config_file_path = f"config/{conf_file}"
# If a config isn't specified use the default
else:
    config_file_path = "config/default_config.ini"

# Import settings from the specified config file
cfg = ConfigParser()
cfg.read_file(open(config_file_path))
global_config = cfg["global"]

print(global_config)

# Some code to do something complex