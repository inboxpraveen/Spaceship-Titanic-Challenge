from utils import *

if not os.path.exists(DATA_PATH):
    os.makedir(DATA_PATH)

if not os.path.exists(MODEL_PATH):
    os.makedir(MODEL_PATH)

if not os.path.exists(TEMP_PATH):
    os.makedir(TEMP_PATH)

def download_data(dataset_name :str = "") -> bool:
    ...


