# get_dataset.py

import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

DATA_DIR = "data/raw"
DATASET = "yasserh/instacart-online-grocery-basket-analysis-dataset"

def download_instacart_dataset():
    os.makedirs(DATA_DIR, exist_ok=True)

    print("[INFO] Authenticating with Kaggle API...")
    api = KaggleApi()
    api.authenticate()

    print(f"[INFO] Downloading dataset: {DATASET}")
    api.dataset_download_files(DATASET, path=DATA_DIR, unzip=True)

    print(f"[SUCCESS] Dataset ready in '{DATA_DIR}'")

if __name__ == "__main__":
    download_instacart_dataset()
