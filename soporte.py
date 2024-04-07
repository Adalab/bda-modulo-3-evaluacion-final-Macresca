#%%
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import ttest_ind, norm, chi2_contingency, f_oneway, shapiro, kstest
from sklearn.linear_model import LinearRegression
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames
import warnings
warnings.filterwarnings("ignore")
# %%

def open_file(ruta):
    csv_apertura= pd.read_csv(ruta, index_col=0)
    csv_apertura.reset_index(inplace = True)
    display(csv_apertura.sample(5))
    return csv_apertura
# %%

def data_exploring(csv):
    forma = csv.shape
    print(f"La forma es {forma}")
    print("_______________")
    columnas = csv.columns
    print(f"Las columnas son {columnas}")
    print("_______________")
    nulos = csv.isna().sum().reset_index()
    print(f"Los nulos son:")
    display(nulos)
    print("_______________")
    duplicados = csv.duplicated().sum()
    print(f"Hay {duplicados} duplicados")
    print("_______________")
    tipo_dato = csv.dtypes.reset_index()
    print(f"Los datos son de tipo:")
    display(tipo_dato)


# %%
def drop_duplicates(df):
    df.drop_duplicates(inplace=True)
# %%
def rename_columns(df, new_column_names):
    df.columns = new_column_names
# %%

def process_columns(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')

def merge_dataframes(df1, df2, on_column):
    
    merged_df = df1.merge(df2, on=on_column)
    return merged_df

# %%
