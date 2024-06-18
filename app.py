from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests
from queries import get_All_alquileres
from operaciones import *
import plotly.graph_objs as go

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_all_alquileres', methods=['GET'])
def obtener_alquileres():
    graphql_url = 'https://finalbackactivoscz.fly.dev/graphql'

    try:
        response = requests.post(graphql_url, json={'query': get_All_alquileres}, verify=False)  # Ignorar SSL

        if response.status_code == 200:
            alquileres = response.json()['data']['getAlquilers']

            # Realizar operaciones
            activos_fijos = clasificar_activos(alquileres)
            total_ingresos = calcular_total_ingresos(alquileres)
            categoria_mas_frecuente = determinar_categoria_mas_frecuente(alquileres)
            duracion_alquileres = calcular_duracion_alquileres(alquileres)
            adquisiciones_por_mes = calcular_adquisiciones_por_mes(alquileres)
            ingresos_por_mes = calcular_ingresos_por_mes(alquileres)  # Agregar esta función

            # Generar gráfico de barras para activos fijos
            fig_activos_fijos = go.Figure(data=[go.Bar(x=list(activos_fijos.keys()), y=list(activos_fijos.values()))])
            fig_activos_fijos.update_layout(title='Activos Fijos por Categoría', xaxis_title='Categorías', yaxis_title='Número de Activos')

            # Generar gráfico de torta para adquisiciones por mes
            fig_adquisiciones_por_mes = go.Figure(data=[go.Pie(labels=list(adquisiciones_por_mes.keys()), values=list(adquisiciones_por_mes.values()))])
            fig_adquisiciones_por_mes.update_layout(title='Adquisiciones por Mes')

            # Generar gráfico de barras para ingresos por mes
            fig_ingresos_por_mes = go.Figure(data=[go.Bar(x=list(ingresos_por_mes.keys()), y=list(ingresos_por_mes.values()))])
            fig_ingresos_por_mes.update_layout(title='Ingresos por Mes', xaxis_title='Mes', yaxis_title='Ingresos')

            dataset = {
                "grafico_barras": fig_activos_fijos.to_json(),
                "grafico_torta": fig_adquisiciones_por_mes.to_json(),
                "grafico_ingresos_por_mes": fig_ingresos_por_mes.to_json(),
                "total_ingresos": total_ingresos,
                "categoria_mas_frecuente": categoria_mas_frecuente,
                "duracion_alquileres": duracion_alquileres
            }

            return jsonify(dataset)
        else:
             return jsonify({"error": "Error al obtener alquileres del servidor GraphQL"}), response.status_code
    except requests.exceptions.SSLError as e:
        return jsonify({"error": f"SSL Error: {str(e)}"}), 500

    
    
if __name__ == '__main__':
    app.run(debug=True)
