from pathlib import Path

COURSEBASE_DIR = Path(__file__)
CACHE_DIR = Path("~/.cache/coursebase").expanduser()
CONFIG_DIR = Path("~/.config/coursebase").expanduser()

URL_ROOT = "http://kayit.etu.edu.tr/rapor/web/index.php/Program2020guz"
URL_COURSEBASE = "{0}/coursebase".format(URL_ROOT)

CONFIG_FILE = CONFIG_DIR / "config.json"
CACHE_FILE = CACHE_DIR / "data.json"

from coursebase.core.main import main
