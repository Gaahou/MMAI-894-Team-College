import pandas as pd
import numpy as np
from matplotlib import image
from skimage.transform import resize
import os

class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path
    def load_data(path):
        df = pd.read_csv(path, header=None, sep=';')
        print(df.head(3))
        return df

    def load_images(self, folder):
        loaded_images = []
        for img in os.listdir(f'./{self.data_path}/{folder}'):
            img_data = image.imread(f'./{self. data_path}/{folder}/{img}').astype(np.float32)
            image_resized=resize(img_data,(100, 100))
            loaded_images.append(image_resized)
    #     loaded_images = np.concatenate(loaded_images, axis=0 )
        loaded_images = np.stack(loaded_images, axis=0)
        return loaded_images
