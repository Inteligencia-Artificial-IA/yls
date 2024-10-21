# app.py

import pandas as pd
from flask import Flask, render_template, request
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar el dataset
DATASET_PATH = 'ferreteria_dataset_large.csv'

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar PCA
@app.route('/perform_pca', methods=['POST'])
def perform_pca():
    # Cargar datos
    df = pd.read_csv(DATASET_PATH)
    
    # Seleccionar características para PCA
    features = ['Edad', 'Precio', 'Cantidad', 'Dias_Desde_Ultima_Compra', 'Total_Compras', 'Descuento_Aplicado']
    x = df[features].values

    # Aplicar PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(x)
    
    # Crear DataFrame para resultados
    pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    
    # Guardar el gráfico
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df)
    plt.title('PCA de Compras en Ferretería')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.grid()
    plt.savefig('static/pca_plot.png')
    plt.close()

    return render_template('index.html', pca_plot='static/pca_plot.png')

if __name__ == '__main__':
    app.run(debug=True)
