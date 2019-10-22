import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN = os.environ.get("API_TOKEN")
APY = os.environ.get("API_KEY")
place_m = os.environ.get("place_m")
place_t = os.environ.get("place_t")
place_w = os.environ.get("place_w")
place_th = os.environ.get("place_th")
place_f = os.environ.get("place_f")