import pandas as pd
import os.path


def process(file):
    ext = os.path.splitext(file.filename)[1][1:].lower()

    if ext == 'csv':
        data = pd.read_csv(file.stream)
    else:
        data = pd.read_excel(file.stream)
    return list(data.keys())
