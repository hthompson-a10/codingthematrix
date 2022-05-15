import string
import numpy as np
import pandas as pd



def build_patient_df(file_name: str) -> None:
    labels = ["radius", "texture", "perimeter", "area",
              "smoothness", "compactness", "concavity",
              "concave points", "symmetry", "fractal dimension"]
    label_mods = ["(mean)", "(stderr)", "(worst)"]

    # Yields [..., radius means, radius stderr, ...]
    labels = [i + j for i in labels for j in label_mods]
    labels.insert(0, "malignancy")
    labels.insert(0, "id")

    patient_df = pd.read_csv(file_name, delimiter=',', header=0, names=labels, index_col=0)
    return patient_df


def signum(u: pd.DataFrame) -> pd.DataFrame:
    pass


def fraction_wrong(A: pd.DataFrame, b: pd.DataFrame, w: pd.DataFrame) -> float:
    pass


def main():
    FILENAME = 'train.csv'
    
    patient_df = build_patient_df(FILENAME)
    
    target_df = patient_df['malignancy']
    target_df[:].mask(target_df[:] == 'B', 1, inplace=True)
    target_df[:].mask(target_df[:] == 'M', -1, inplace=True)

    patient_df.drop('malignancy', axis=1, inplace=True)

    

main()