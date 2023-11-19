import os
import pandas as pd
import numpy as np

FILE_PATH = './data/Umsatzanzeige_DE70500105175419596903_20220606.csv'

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df



