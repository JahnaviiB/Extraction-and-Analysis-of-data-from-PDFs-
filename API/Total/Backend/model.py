import librosa
import pandas as pd
import numpy as np
import os
import librosa.display
import pickle
import warnings
import IPython.display as ipd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras import optimizers
from keras.models import Sequential, load_model
from keras import layers
from keras.layers import *
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import accuracy_score
import math
import json
import pprint
import pdfplumber
import pypdf
import PyPDF2


class PDF_file():
    def __int__(self):
        pass

    def extract_text(self):
        # decide between pdf modules (pypdf, pdfplumber, pypdf2)
        pass

    def preprocess_extracted_text(self):
        pass

    def plot_graphs(self):
        pass

    def perform_analysis(self):
        # compare new data point with existing model results(mean, median)
        pass

