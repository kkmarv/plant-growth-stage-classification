import os
import threading

import requests
from pandas import DataFrame, Series


def download_image(url, filename):
    """Download a file from the given URL to the given filename."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb+") as f:
                f.write(response.content)
                print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")

    except FileExistsError:
        print(f"File {filename} already exists")
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")


def download_images_to_yolo(df: DataFrame, label: Series, root_dir: str):
    """Download images from the given dataframe to the given directory in the format required for YOLO training."""
    threads = []

    df = df.reset_index(drop=True)
    for index, row in df.iterrows():
        assert type(index) == int
        stage = label.iloc[index]
        species = row["Pflanze"]
        url = row["BildUrl"]

        dir_path = os.path.join(root_dir, stage)
        os.makedirs(dir_path, exist_ok=True)

        filename = url.split("/")[-1]
        filepath = os.path.join(dir_path, f"{species}_{filename}")

        if not os.path.exists(filepath):
            thread = threading.Thread(target=download_image, args=(url, filepath))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
