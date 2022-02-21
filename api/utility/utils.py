from pathlib import Path
from typing import List
from dotenv import load_dotenv
import logging


log = logging.getLogger(__name__)

def load_env():
    basedir = Path(__file__).resolve().parents[2]
    log.info(f"THE BASEDIR IS {basedir}")
    dotenv_path = Path.joinpath(basedir, "bard.env").resolve()
    load_dotenv(dotenv_path)