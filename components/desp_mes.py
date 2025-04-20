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
    dbc.Row([
        dbc.Col([
            html.Legend("Despesas por mês"),
            html.Div(id="tabela-desp-mes", className="dbc"),
            ], width=9),
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graph-desp-mes', style={"margin-right": "20px"}),
        ], width=9),
    ]),
], style={"padding": "10px"})

# =========  Callbacks  =========== #
# Tabela
@app.callback(
    Output('tabela-desp-mes', 'children'),
    Input('store-despesas', 'data')
)
def imprimir_tabela (data):
    df = pd.DataFrame(data)

    # Resume a tabela com os dados necessários
    df = df[['Data', 'Categoria', 'Valor']]
    df['Data'] = pd.to_datetime(df['Data'])
    df['Data'] = df['Data'].dt.strftime('%Y-%m')
    

    # Dados de cada mês
    meses = sorted(df['Data'].unique())
    categorias = list(df['Categoria'].unique())
    categorias.insert(0, 'Mês')
    categorias.insert(len(categorias), 'Total')
    categorias.remove('Ajuste saldo')
    categorias.remove('Fatura')
    df_meses = pd.DataFrame(columns=categorias)
    for mes in meses:
        df_mes = df[df['Data'] == mes].drop('Data', axis=1)
        df_mes = round(df_mes.groupby('Categoria').sum().T, 2)
        df_mes = df_mes.drop(columns='Fatura')
        if mes == '2025-04':
            df_mes = df_mes.drop(columns='Ajuste saldo')
        df_mes.insert(0, 'Mês', int(mes[-1]))
        df_mes['Total'] = round(df_mes.sum(axis=1) - df_mes['Mês'], 2)
        df_meses.loc[len(df_meses)] = df_mes.iloc[0]

    df_meses['Mês'] = df['Data'].unique()

    tabela = dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False, "hideable": True}
            if i == "Descrição" or i == "Fixo" or i == "Efetuado"
            else {"name": i, "id": i, "deletable": False, "selectable": False}
            for i in df_meses.columns
        ],

        data=df_meses.to_dict('records'),
        filter_action="native",    
        sort_action="native",       
        sort_mode="single",  
        selected_columns=[],        
        selected_rows=[],          
        page_action="native",      
        page_current=0,             
        page_size=10,                        
    ),

    return tabela

# Bar Graph            
@app.callback(
    Output('bar-graph-desp-mes', 'figure'),
    [Input('store-despesas', 'data'),
    Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def bar_chart(data, theme):
    df = pd.DataFrame(data)
    df_grouped = df.groupby("Categoria").sum()[["Valor"]].reset_index()
    df_grouped = df_grouped.drop([0,8])
    graph = px.bar(df_grouped, x='Categoria', y='Valor', title="Despesas Gerais")
    graph.update_layout(template=template_from_url(theme))
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return graph
