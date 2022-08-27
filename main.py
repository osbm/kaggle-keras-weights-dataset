#import keras
from tensorflow import keras
import tensorflow as tf
from scrape_filenames import get_filenames
import os

BASE_WEIGHT_URL = ('https://github.com/fchollet/deep-learning-models/releases/download/')

os.system('mkdir -p dataset')  


files = get_filenames()
for file in files:
    os.system('wget -P ./dataset/ ' + BASE_WEIGHT_URL + file)
    print(file)
