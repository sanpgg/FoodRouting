import pandas as pd
import numpy as np


def json_to_df(json_text):
    # TODO función que transforme de json a df
    return pd.read_json(json_text)


def df_to_json(df):
    # función que transforma de df a json
    return df.to_json(orient='records')


if __name__ == '__main__':
    n_casas = 1000
    casas_df = pd.DataFrame({
        'labs_casas': list(range(n_casas)),
        'lon': np.random.rand(n_casas),
        'lat': np.random.rand(n_casas)})
    json_data = df_to_json(casas_df)
    df_renewed = json_to_df(json_data)
    print(json_data)
    print(df_renewed)
