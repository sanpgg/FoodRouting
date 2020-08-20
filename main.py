from flask import Flask, request, Response
from opt.clustering_functions import asigna_entregas
from opt.rutas import crea_rutas
from opt.formater import df_to_json
import pandas as pd
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "API working"


@app.route('/get_best_routes', methods=['POST'])
def get_routes():
    hogares_df = pd.DataFrame(request.json['hogares'])
    centros_df = pd.DataFrame(request.json['centros'])
    labs_casas, labs_centros, labs_cuadrilla = asigna_entregas(
        hogares_df, centros_df)
    df_input = pd.DataFrame({
        'labs_casas': labs_casas,
        'labs_centros': labs_centros,
        'labs_cuadrilla': labs_cuadrilla
    })
    df_final = crea_rutas(hogares_df, df_input, centros_df)
    return Response(
       df_final.to_csv(),
       mimetype="text/csv",
       headers={"Content-disposition":
       "attachment; filename=filename.csv"})
    
    
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
