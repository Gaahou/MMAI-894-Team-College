import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential, Model
from keras.layers import Dense,BatchNormalization, Activation
from keras.layers.convolutional import Conv3D, MaxPooling3D, Conv2D, MaxPooling2D
from keras.utils import np_utils
from tensorflow.keras.utils import to_categorical
from matplotlib import image
from skimage.transform import resize
import tensorflow as tf
import numpy as np
import os

data_path = 'data/train'

def load_images(folder):
    loaded_images = []
    for img in os.listdir(f'./{data_path}/{folder}'):
        img_data = image.imread(f'./{data_path}/{folder}/{img}').astype(np.float32)
        image_resized=resize(img_data,(100, 100,3))
        loaded_images.append(image_resized)
    loaded_images = np.concatenate(loaded_images, axis=0 ).tolist()
    return loaded_images

def prepare_data(df):
    train_df = df.copy()
    train_df = train_df.drop([0, 1], axis=1)
    train_df = train_df.rename(columns={2: "label", 3: "data"})
#     Y = to_categorical(train_df['label'])
    Y = train_df['label']
    X = train_df['data']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
#     X_train = np.concatenate(X_train.values, axis=0)
#     X_test = np.concatenate(X_test.values, axis=0)
    return X_train, X_test, y_train, y_test

df = pd.read_csv("data/train.csv", header=None, sep=';')
df.head(3)
df =df[0:5]
df[3] = df[0].apply(lambda x: load_images(x))
X_train, X_test, y_train, y_test = prepare_data(df)
X_train = tf.convert_to_tensor(X_train.values)
