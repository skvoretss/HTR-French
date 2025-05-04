import os
from PIL import Image
from zipfile import ZipFile
from urllib.request import urlretrieve

def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assets....", end="")
    urlretrieve(url, save_path)

    try:
        with ZipFile(save_path) as z:
            z.extractall(os.path.split(save_path)[0])
        print("Done")
    except Exception as e:
        print("\nInvalid file.", e)

def format_RIMES_line():

    URL = r"https://storage.teklia.com/public/rimes2011/RIMES-2011-Lines.zip"
    asset_zip_path = os.path.join(os.getcwd(), "Datasets/RIMES-2011-Lines.zip")

    if not os.path.exists(asset_zip_path):
        download_and_unzip(URL, asset_zip_path)