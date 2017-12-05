# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df("data/ipl_dataset.csv")
import pandas as pd
import numpy as np
# Solution
def get_match_innings_runs():
    df=pd.DataFrame(ipl_df[['match_code','inning','runs']])
    new_df=df.pivot_table(['runs'],index=['match_code','inning'],aggfunc=np.sum)
    return new_df
