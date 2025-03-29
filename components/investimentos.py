<<<<<<< HEAD:projeto_completo/components/investimentos.py
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
        html.Legend("Tabela de investimentos"),
        html.Div(id="tabela-investimentos", className="dbc"),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graphs', style={"margin-right": "20px"}),
        ], width=9),
            
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Investimentos"),
                    html.Legend("R$ -", id="valor_investimento_card", style={'font-size': '60px'}),
                    html.H6("Total de investimentos"),
                ], style={'text-align': 'center', 'padding-top': '30px'}))
        ], width=3),
    ]),
], style={"padding": "10px"})

# =========  Callbacks  =========== #
# Tabela
@app.callback(
    Output('tabela-investimentos', 'children'),
    Input('store-investimentos', 'data')
)
def imprimir_tabela (data):
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data']).dt.date

    df.loc[df['Efetuado'] == 0, 'Efetuado'] = 'Não'
    df.loc[df['Efetuado'] == 1, 'Efetuado'] = 'Sim'

    df.loc[df['Fixo'] == 0, 'Fixo'] = 'Não'
    df.loc[df['Fixo'] == 1, 'Fixo'] = 'Sim'

    df = df.fillna('-')

    df.sort_values(by='Data', ascending=False)

    tabela = dash_table.DataTable(
        id='data-table-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False, "hideable": True}
            if i == "Descrição" or i == "Fixo" or i == "Efetuado"
            else {"name": i, "id": i, "deletable": False, "selectable": False}
            for i in df.columns
        ],

        data=df.to_dict('records'),
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
    Output('bar-graphs', 'figure'),
    [Input('store-investimentos', 'data'),
    Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def bar_chart(data, theme):
    df = pd.DataFrame(data)   
    df_grouped = df.groupby("Categoria").sum()[["Valor"]].reset_index()
    graph = px.bar(df_grouped, x='Categoria', y='Valor', title="Investimentos")
    graph.update_layout(template=template_from_url(theme))
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return graph

# Simple card
@app.callback(
    Output('valor_investimento_card', 'children'),
    Input('store-investimentos', 'data')
)
def display_invest(data):
    df = pd.DataFrame(data)
    valor = df['Valor'].sum()
    
=======
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
        html.Legend("Tabela de investimentos"),
        html.Div(id="tabela-investimentos", className="dbc"),
    ]),

    dbc.Row([
            dbc.Col([
                dcc.Graph(id='bar-graphs', style={"margin-right": "20px"}),
            ], width=9),
            
            dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Investimentos"),
                        html.Legend("R$ -", id="valor_investimento_card", style={'font-size': '60px'}),
                        html.H6("Total de investimentos"),
                    ], style={'text-align': 'center', 'padding-top': '30px'}))
            ], width=3),
        ]),
    ], style={"padding": "10px"})

# =========  Callbacks  =========== #
# Tabela
@app.callback(
    Output('tabela-investimentos', 'children'),
    Input('store-investimentoss', 'data')
)
def imprimir_tabela (data):
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data']).dt.date

    df.loc[df['Efetuado'] == 0, 'Efetuado'] = 'Não'
    df.loc[df['Efetuado'] == 1, 'Efetuado'] = 'Sim'

    df.loc[df['Fixo'] == 0, 'Fixo'] = 'Não'
    df.loc[df['Fixo'] == 1, 'Fixo'] = 'Sim'

    df = df.fillna('-')

    df.sort_values(by='Data', ascending=False)

    tabela = dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False, "hideable": True}
            if i == "Descrição" or i == "Fixo" or i == "Efetuado"
            else {"name": i, "id": i, "deletable": False, "selectable": False}
            for i in df.columns
        ],

        data=df.to_dict('records'),
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
    Output('bar-graphs', 'figure'),
    [Input('store-investimentos', 'data'),
    Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def bar_chart(data, theme):
    df = pd.DataFrame(data)   
    df_grouped = df.groupby("Categoria").sum()[["Valor"]].reset_index()
    graph = px.bar(df_grouped, x='Categoria', y='Valor', title="Investimentos")
    graph.update_layout(template=template_from_url(theme))
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return graph

# Simple card
@app.callback(
    Output('valor_investimento_card', 'children'),
    Input('store-investimentos', 'data')
)
def display_invest(data):
    df = pd.DataFrame(data)
    valor = df['Valor'].sum()
    
>>>>>>> 23caa3f101c976c15d75672143eb8a5bdcd9fb77:components/investimentos.py
    return f"R$ {valor}"