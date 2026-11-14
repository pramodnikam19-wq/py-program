print("Sakshi Bhujade")
print()


import pandas as pd

def test_no_missing_values():
    df = pd.read_csv("data.csv")
    assert df.isnull().sum().sum() == 0


def test_no_duplicates():
    df = pd.read_csv("data.csv")
    assert df.duplicated().sum().sum() == 0