import os.path

COURSEBASE_DIR = os.path.dirname(__file__)
CACHE_DIR = os.path.expanduser("~/.cache/coursebase")
CONFIG_DIR = os.path.expanduser("~/.config/coursebase")

URL_ROOT = "http://kayit.etu.edu.tr/rapor/web/index.php/Program2020guz"
URL_COURSEBASE = "{0}/coursebase".format(URL_ROOT)

CONFIG_FILE = "config.json"
CACHE_FILE = "data.json"

from coursebase.core.main import main
