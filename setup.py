from utils import *
import kaggle

if not os.path.exists(DATA_PATH):
    os.makedir(DATA_PATH)

if not os.path.exists(MODEL_PATH):
    os.makedir(MODEL_PATH)

if not os.path.exists(TEMP_PATH):
    os.makedir(TEMP_PATH)


def download_data(dataset_name :str = "") -> bool:
    
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, path=DATA_PATH, unzip=True)


if __name__ == "__main__":
    

