<<<<<<< HEAD:projeto_completo/myindex.py
from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# import from folders
from app import *
from components import sidebar, dashboards, extratos, investimentos, projecao
from globals import *

# DataFrames and Dcc.Store

df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
df_receitas_aux = df_receitas.to_dict()

df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
df_despesas_aux = df_despesas.to_dict()

df_investimentos = pd.read_csv("df_investimento.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
df_investimentos_aux = df_investimentos.to_dict()

df_gasto = pd.read_csv("df_gasto.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
df_gasto_aux = df_gasto.to_dict()

df_entrada = pd.read_csv("df_entrada.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
df_entrada_aux = df_entrada.to_dict()

list_receitas = pd.read_csv('df_cat_receita.csv', index_col=0)
list_receitas_aux = list_receitas.to_dict()

list_despesas = pd.read_csv('df_cat_despesa.csv', index_col=0)
list_despesas_aux = list_despesas.to_dict()

list_investimentos = pd.read_csv('df_cat_investimento.csv', index_col=0)
list_investimentos_aux = list_investimentos.to_dict()

list_gasto = pd.read_csv('df_cat_gasto.csv', index_col=0)
list_gasto_aux = list_gasto.to_dict()

list_entrada = pd.read_csv('df_cat_entrada.csv', index_col=0)
list_entrada_aux = list_entrada.to_dict()


# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dcc.Store(id='store-receitas', data=df_receitas_aux),
    dcc.Store(id="store-despesas", data=df_despesas_aux),
    dcc.Store(id="store-investimentos", data=df_investimentos_aux),
    dcc.Store(id="store-gasto", data=df_gasto_aux),
    dcc.Store(id="store-entrada", data=df_entrada_aux),
    dcc.Store(id='stored-cat-receitas', data=list_receitas_aux),
    dcc.Store(id='stored-cat-despesas', data=list_despesas_aux),
    dcc.Store(id='stored-cat-investimentos', data=list_investimentos_aux),
    dcc.Store(id='stored-cat-gasto', data=list_gasto_aux),
    dcc.Store(id='stored-cat-entrada', data=list_entrada_aux),
    
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),

        dbc.Col([
            html.Div(id="page-content")
        ], md=10),
    ])

], fluid=True, style={"padding": "0px"}, className="dbc")


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.layout

    if pathname == "/extratos":
        return extratos.layout
    
    if pathname == "/investimentos":
        return investimentos.layout
    
    if pathname == "/projecao":
        return projecao.layout
        

if __name__ == '__main__':
=======
from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# import from folders
from app import *
from components import sidebar, dashboards, extratos, investimentos
from globals import *

# DataFrames and Dcc.Store

df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
df_receitas_aux = df_receitas.to_dict()

df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
df_despesas_aux = df_despesas.to_dict()

df_investimentos = pd.read_csv("df_investimento.csv", index_col=0, parse_dates=True)
df_investimentos_aux = df_investimentos.to_dict()

list_receitas = pd.read_csv('df_cat_receita.csv', index_col=0)
list_receitas_aux = list_receitas.to_dict()

list_despesas = pd.read_csv('df_cat_despesa.csv', index_col=0)
list_despesas_aux = list_despesas.to_dict()

list_investimentos = pd.read_csv('df_cat_investimento.csv', index_col=0)
list_investimentos_aux = list_investimentos.to_dict()


# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dcc.Store(id='store-receitas', data=df_receitas_aux),
    dcc.Store(id="store-despesas", data=df_despesas_aux),
    dcc.Store(id="store-investimentos", data=df_investimentos_aux),
    dcc.Store(id='stored-cat-receitas', data=list_receitas_aux),
    dcc.Store(id='stored-cat-despesas', data=list_despesas_aux),
    dcc.Store(id='stored-cat-investimentos', data=list_investimentos_aux),
    
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),

        dbc.Col([
            html.Div(id="page-content")
        ], md=10),
    ])

], fluid=True, style={"padding": "0px"}, className="dbc")


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.layout

    if pathname == "/extratos":
        return extratos.layout
    
    if pathname == "/investimentos":
        return investimentos.layout
        

if __name__ == '__main__':
>>>>>>> 23caa3f101c976c15d75672143eb8a5bdcd9fb77:myindex.py
    app.run_server(debug=True)