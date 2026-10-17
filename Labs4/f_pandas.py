import pandas as pd

def make_dataframe(names, ages):
    return pd.DataFrame({"name": names, "age": ages})