from utils import *
import kaggle

if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)

if not os.path.exists(MODEL_PATH):
    os.mkdir(MODEL_PATH)

if not os.path.exists(TEMP_PATH):
    os.mkdir(TEMP_PATH)

def download_data(dataset_name :str = "") -> bool:
    try:
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(dataset_name, path=DATA_PATH, unzip=True)
        return True
    except Exception as e:
        print(f"Unable to download dataset due to: {e}")
        return False


if __name__ == "__main__":
    input_dataset = input(f"Enter dataset name from kaggle: ")
    is_downloaded = download_data(input_dataset)
    if is_downloaded:
        print(f"Successfully downloaded dataset.")
    else:
        print(f"Download failed. Please check if the you are authenticated properly or you typed dataset name correctly.")

