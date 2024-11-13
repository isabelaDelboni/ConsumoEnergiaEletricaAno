import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('br_mme_consumo_energia_eletrica_uf (1).csv')
df['consumo'] = pd.to_numeric(df['consumo'], errors='coerce')
df['numero_consumidores'] = pd.to_numeric(df['numero_consumidores'], errors='coerce')
df['numero_consumidores'] = df['numero_consumidores'].fillna(0)
df['consumo'] = df['consumo'].fillna(0)
df['ano'] = pd.to_numeric(df['ano'], errors='coerce')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Consumo de Energia Elétrica por Ano - Seleção por Estado"),
    dcc.Dropdown(
        id='uf-dropdown',
        options=[{'label': uf, 'value': uf} for uf in df['sigla_uf'].unique()],
        value='SP',
        clearable=False,
        style={'width': '50%'}
    ),
    dcc.Graph(id='grafico')
])

@app.callback(
    Output('grafico', 'figure'),
    [Input('uf-dropdown', 'value')]
)
def atualizar_grafico(uf_selecionada):
    df_filtrado = df[df['sigla_uf'] == uf_selecionada]
    df_agrupado = df_filtrado.groupby('ano').agg({'consumo': 'sum'}).reset_index()
    
    fig = px.bar(df_agrupado, 
                 x="ano", 
                 y="consumo", 
                 title=f"Consumo Total de Energia em {uf_selecionada} por Ano",
                 labels={"consumo": "Consumo de Energia (MWh)", "ano": "Ano"})
    
    fig.update_layout(
        yaxis_tickformat=".2s",
        title_x=0.5,
        template="simple_white"
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
