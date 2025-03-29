import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO

# =========  Layout  =========== #
layout = dbc.Col([
    # Linha e Colunas para o card de saldo futuro
    dbc.Row([
        dbc.Card(
                dbc.CardBody([
                    html.H4("Saldo Futuro"),
                    html.Legend("R$ -", id="valor_fut_card", style={'font-size': '60px'}),
                ], style={'text-align': 'center', 'padding-top': '30px'}))
    ]),
    
    # Linha e Colunas para o gráfico e o card de gastos futuros
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='barra-graph', style={"margin-right": "20px"}),
        ], width=9),
        
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Gastos Futuros"),
                    html.Legend("R$ -", id="valor_gasto_card", style={'font-size': '60px'}),
                ], style={'text-align': 'center', 'padding-top': '30px'}))
        ], width=3),
    ]),

    # Linha e Colunas para o gráfico e o card de entradas futuras
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='barras-graph', style={"margin-right": "20px"}),
        ], width=9),
        
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Entradas Futuras"),
                    html.Legend("R$ -", id="valor_entrada_card", style={'font-size': '60px'}),
                ], style={'text-align': 'center', 'padding-top': '30px'}))
        ], width=3),
    ]),
], style={"padding": "10px"})

# =========  Callbacks  =========== #
# Bar Graph Gasto           
@app.callback(
    Output('barra-graph', 'figure'),
    [Input('store-gasto', 'data'),
    Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def bar_chart(data, theme):
    df = pd.DataFrame(data)   
    df_grouped = df.groupby("Categoria").sum()[["Valor"]].reset_index()
    graph = px.bar(df_grouped, x='Categoria', y='Valor', title="Gastos Futuros")
    graph.update_layout(template=template_from_url(theme))
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return graph

# Simple card gasto
@app.callback(
    Output('valor_gasto_card', 'children'),
    Input('store-gasto', 'data')
)
def display_desp(data):
    df = pd.DataFrame(data)
    valor = round(df['Valor'].sum(), 2)
    
    return f"R$ {valor}"

# Bar Graph Entrada         
@app.callback(
    Output('barras-graph', 'figure'),
    [Input('store-entrada', 'data'),
    Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def bar_chart(data, theme):
    df = pd.DataFrame(data)   
    df_grouped = df.groupby("Categoria").sum()[["Valor"]].reset_index()
    graph = px.bar(df_grouped, x='Categoria', y='Valor', title="Entradas Futuras")
    graph.update_layout(template=template_from_url(theme))
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return graph

# Simple card entrada
@app.callback(
    Output('valor_entrada_card', 'children'),
    Input('store-entrada', 'data')
)
def display_desp(data):
    df = pd.DataFrame(data)
    valor = round(df['Valor'].sum(), 2)
    
    return f"R$ {valor}"

# Simple card saldo
@app.callback(
    Output('valor_fut_card', 'children'),
    Input('store-gasto', 'data'),
    Input('store-entrada', 'data'),
    Input("store-despesas", "data"),
    Input("store-receitas", "data"),
    Input("store-investimentos", "data")
    )

def display_desp(gasto, entrada, despesas, receitas, investimentos):
    df_despesas = pd.DataFrame(despesas)
    df_receitas = pd.DataFrame(receitas)
    df_investimentos = pd.DataFrame(investimentos)

    saldo_atual = round(df_receitas['Valor'].sum() - df_despesas[df_despesas['Efetuado']==1]['Valor'].sum() - df_investimentos['Valor'].sum(), 2)

    df_gasto = pd.DataFrame(gasto)
    df_entrada = pd.DataFrame(entrada)

    valor = round(saldo_atual + df_entrada['Valor'].sum() - df_gasto['Valor'].sum(), 2)
    
    return f"R$ {valor}"
