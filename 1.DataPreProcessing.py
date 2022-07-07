import numpy as np
import pandas as pd
import tqdm


train_csv_path = "./train/train.csv"
test_csv_path = "./train/test.csv"

train_df = pd.read_csv(train_csv_path)
train_df.head(10)
