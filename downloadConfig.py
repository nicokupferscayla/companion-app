import pathlib

DOWNLOAD_DIR = str(pathlib.Path.home()) + "/.cache/companion/tmp"  # temp dir for downloading files
CONFIG_DIR = str(pathlib.Path.home()) + "/.config/companion"  # config/settings dir
ALLOWED_FILE = CONFIG_DIR + "/" + "allowed"  # file for allowed sites

FILES = []  # temp storage for downloaded file metadata
ALLOWED_SITES = []  # stores allowed site names
