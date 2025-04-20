import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import date

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
    Input('store-gasto', 'data'),
    Input("store-despesas", "data")
)
def display_desp(gastos, credito):
    df_gasto = pd.DataFrame(gastos)
    df_despesas = pd.DataFrame(credito)

    df_despesas['Data'] = pd.to_datetime(df_despesas['Data'])
    df_despesas = df_despesas[df_despesas['Data'].dt.strftime('%Y-%m') == date.today().strftime("%Y-%m")]
    credito = round(df_despesas[df_despesas['Efetuado']==0]['Valor'].sum(), 2)

    valor = round(df_gasto['Valor'].sum() + credito, 2)
    
    return f"R$ {valor}"

# Bar Graph Entrada         
@app.callback(
    Output('barras-graph', 'figure'),
    [Input('store-entrada', 'data'),
    Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def bar_chart(data, theme):
    df = pd.DataFrame(data)   
    df['Data'] = pd.to_datetime(df['Data'])
    df['Month'] = 0
    df = df.reset_index()
    for i in range(len(df['Data'])):
        df.loc[i, 'Month'] = df['Data'][i].month
    df = df[df['Month'] == date.today().month + 1]
    df['Data']=df.iloc[0]['Data'].strftime('%Y-%m-%d')

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
    df['Data'] = pd.to_datetime(df['Data'])
    df['Month'] = 0
    df = df.reset_index()
    for i in range(len(df['Data'])):
        df.loc[i, 'Month'] = df['Data'][i].month
    df = df[df['Month'] == date.today().month + 1]

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

    # Saldo atual
    saldo_atual = round(df_receitas['Valor'].sum() - df_despesas[df_despesas['Efetuado']==1]['Valor'].sum() - df_investimentos['Valor'].sum(), 2)

    df_gasto = pd.DataFrame(gasto)
    df_entrada = pd.DataFrame(entrada)

    # Valor no crédito
    df_despesas['Data'] = pd.to_datetime(df_despesas['Data'])
    df_despesas = df_despesas[df_despesas['Data'].dt.strftime('%Y-%m') == date.today().strftime("%Y-%m")]
    credito = round(df_despesas[df_despesas['Efetuado']==0]['Valor'].sum(), 2)

    # Entradas futuras
    df_entrada['Data'] = pd.to_datetime(df_entrada['Data'])
    df_entrada['Month'] = 0
    df_entrada = df_entrada.reset_index()
    for i in range(len(df_entrada['Data'])):
        df_entrada.loc[i, 'Month'] = df_entrada['Data'][i].month
    df_entrada = df_entrada[df_entrada['Month'] == date.today().month + 1]

    # Saldo futuro
    valor = round(saldo_atual + df_entrada['Valor'].sum() - df_gasto['Valor'].sum() - credito, 2)
    
    return f"R$ {valor}"
