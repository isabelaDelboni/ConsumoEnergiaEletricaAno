import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.read_csv('br_mme_consumo_energia_eletrica_uf (1).csv')
df['consumo'] = pd.to_numeric(df['consumo'], errors='coerce')
df['numero_consumidores'] = pd.to_numeric(df['numero_consumidores'], errors='coerce')
df['numero_consumidores'] = df['numero_consumidores'].fillna(0)
df['consumo'] = df['consumo'].fillna(0)
df['ano'] = pd.to_numeric(df['ano'], errors='coerce')

app = dash.Dash(__name__)

app.layout = html.Div(
    className='container',
    children=[
        html.H1(
            "Consumo de Energia Elétrica por Ano - Seleção por Estado",
            className='title'
        ),

        dcc.Dropdown(
            id='uf-dropdown',
            options=[{'label': uf, 'value': uf} for uf in sorted(df['sigla_uf'].unique())],
            value='SP',
            clearable=False,
            className='dropdown'
        ),

        html.Br(),

        html.Button(
            'Verificar Previsões',
            id='previsao-button',
            n_clicks=0,
            className='button'
        ),
        
        dcc.Graph(id='grafico')
    ]
    
)


@app.callback(
    Output('grafico', 'figure'),
    [Input('uf-dropdown', 'value'),
     Input('previsao-button', 'n_clicks')]
)
def atualizar_grafico(uf_selecionada, n_clicks):
    df_filtrado = df[df['sigla_uf'] == uf_selecionada]
    df_agrupado = df_filtrado.groupby('ano').agg({'consumo': 'sum'}).reset_index()
    fig = px.bar(df_agrupado,
                 x="ano",
                 y="consumo",
                 title=f"Consumo Total de Energia em {uf_selecionada} por Ano",
                 labels={"consumo": "Consumo de Energia (MWh)", "ano": "Ano"})

    if n_clicks % 2 > 0:
        X = df_agrupado['ano'].values.reshape(-1, 1)
        y = df_agrupado['consumo'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        modelo = Lasso(alpha=0.1)
        modelo.fit(X_train, y_train)

        previsoes = modelo.predict(X_test)

        mae = mean_absolute_error(y_test, previsoes)
        mse = mean_squared_error(y_test, previsoes)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, previsoes)

        anos_futuros = np.arange(df_agrupado['ano'].max() + 1, df_agrupado['ano'].max() + 6).reshape(-1, 1)
        previsao_futura = modelo.predict(anos_futuros)

        df_previsao = pd.DataFrame({
            'ano': anos_futuros.flatten(),
            'consumo': previsao_futura
        })

        fig.add_bar(x=df_previsao['ano'], y=df_previsao['consumo'], 
                    name='Previsão', 
                    marker=dict(color='rgba(255, 100, 0, 0.6)'),
                    opacity=0.6)

    fig.update_layout(
        yaxis_tickformat=".2s",
        title_x=0.5,
        template="simple_white",
        showlegend=True
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

