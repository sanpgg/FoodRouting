import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


def asigna_medias(X, medias):
    # INPUT
    # X.- DataFrame
    #  labs_x.- Etiquetas de los datos
    #  lon.- Longitud
    #  lat.- Latitud
    # medias.- DataFrame
    #  labs_meds.- Etiquetas de las medias
    #  lon.- Longitud
    #  lat.- Latitud
    # OUTPUT
    # labs_x
    # labs_c.- array de tamaño labs_x.shape
    #          con asignaciones de labs_meds
    km = KMeans(
        n_clusters=medias.shape[0],
        init=medias[['lat', 'lon']].values)
    km.fit(X[['lat', 'lon']].values)
    return X.labs_x.values, medias.labs_meds[km.labels_]


def asigna_entregas(casas_df, centros_df):
    # INPUT
    # casas_df.- DataFrame
    #  labs_casas.- Etiquetas de los datos
    #  lon.- Longitud
    #  lat.- Latitud
    # centro_df.- DataFrame
    #  labs_centros.- Etiquetas de los centros
    #  lon.- Longitud
    #  lat.- Latitud
    #  n.- número de vehiculos en la flotilla
    # OUTPUT
    # labs_casas
    # labs_centros.- array de tamaño labs_x.shape
    #                con asignaciones de labs_meds
    # labs_flotilla.- Consecutivo por centro
    casas, centros = asigna_medias(
        casas_df.rename(columns={'labs_casas': 'labs_x'}),
        centros_df.rename(columns={'labs_centros': 'labs_meds'}))
    asignaciones = pd.DataFrame({
        'labs_casas': casas,
        'labs_centros': centros,
        'lon': casas_df.lon.tolist(),
        'lat': casas_df.lat.tolist()
    })
    labs_casas = []
    labs_flotilla = []
    labs_centros = []
    for c in asignaciones.labs_centros.unique():
        centro = (
                centros_df
                .query('labs_centros=={}'.format(c)))
        n = centro.n.iloc[0]
        X = (asignaciones.
             query('labs_centros=={}'.format(c)).
             assign(labs_x=lambda x: x.labs_casas.tolist()))
        medias = pd.DataFrame({
            'labs_meds': range(n),
            'lat': centro.lat.iloc[0]+np.random.rand(n)*X.lat.std(),
            'lon': centro.lon.iloc[0]+np.random.rand(n)*X.lon.std()})
        x, y = asigna_medias(X, medias)
        labs_casas = labs_casas + x.tolist()
        labs_flotilla = labs_flotilla + y.tolist()
        labs_centros = labs_centros + X.labs_centros.tolist()
    return labs_casas, labs_centros, labs_flotilla


if __name__ == '__main__':
    casas_df = pd.DataFrame({
        'labs_casas': list(range(100)),
        'lon': np.random.rand(100),
        'lat': np.random.rand(100)})

    centros_df = pd.DataFrame({
        'labs_centros': list(range(5)),
        'lon': np.random.rand(5),
        'lat': np.random.rand(5),
        'n': [5, 2, 6, 3, 2]})

    labs_casas, labs_centros, labs_flotilla = asigna_entregas(
        casas_df, centros_df)
    df_final = pd.DataFrame({
        'labs_casas': labs_casas,
        'labs_centros': labs_centros,
        'labs_flotilla': labs_flotilla
        })

