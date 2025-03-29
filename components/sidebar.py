import os
import dash
import json
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from datetime import datetime, date

import pdb
from dash_bootstrap_templates import ThemeChangerAIO

# ========= DataFrames ========= #
import numpy as np
import pandas as pd
from globals import *

#df_cat_receita = pd.read_csv("C:\Users\Patricia\OneDrive\Desktop\Coding\Finanz\MyBudget\projeto_completo\df_cat_receita.csv")
#cat_receita = df_cat_receita['Categoria'].tolist()

#df_cat_despesa = pd.read_csv("C:\Users\Patricia\OneDrive\Desktop\Coding\Finanz\MyBudget\projeto_completo\df_cat_despesa.csv")
#cat_despesa = df_cat_despesa['Categoria'].tolist()

# ========= Layout ========= #
layout = dbc.Card([
                html.H1("Finanz", className="text-primary"),
                html.Hr(),


    # Seção PERFIL ------------------------
                dbc.Button(id='botao_avatar',
                    children=[html.Img(src="/assets/img_hom.png", id="avatar_change", alt="Avatar", className='perfil_avatar'),
                ], style={'background-color': 'transparent', 'border-color': 'transparent'}),

                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Selecionar Perfil")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardImg(src="/assets/img_hom.png", className='perfil_avatar', top=True),
                                    dbc.CardBody([
                                        html.H4("Perfil Homem", className="card-title"),
                                        html.P(
                                            "Um Card com exemplo do perfil Homem. Texto para preencher o espaço",
                                            className="card-text",
                                        ),
                                        dbc.Button("Acessar", color="warning"),
                                    ]),
                                ]),
                            ], width=6),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardImg(src="/assets/img_fem2.png", top=True, className='perfil_avatar'),
                                    dbc.CardBody([
                                        html.H4("Perfil Mulher", className="card-title"),
                                        html.P(
                                            "Um Card com exemplo do perfil Mulher. Texto para preencher o espaço",
                                            className="card-text",
                                        ),
                                        dbc.Button("Acessar", color="warning"),
                                    ]),
                                ]),
                            ], width=6),
                        ], style={"padding": "5px"}),
                        dbc.Row([
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardImg(src="/assets/img_home.png", top=True, className='perfil_avatar'),
                                    dbc.CardBody([
                                        html.H4("Perfil Casa", className="card-title"),
                                        html.P(
                                            "Um Card com exemplo do perfil Casa. Texto para preencher o espaço",
                                            className="card-text",
                                        ),
                                        dbc.Button("Acessar",  color="warning"),
                                    ]),
                                ]),
                            ], width=6),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardImg(src="/assets/img_plus.png", top=True, className='perfil_avatar'),
                                    dbc.CardBody([
                                        html.H4("Adicionar Novo Perfil", className="card-title"),
                                        html.P(
                                            "Esse projeto é um protótipo, o botão de adicionar um novo perfil esta desativado momentaneamente!",
                                            className="card-text",
                                        ),
                                        dbc.Button("Adicionar", color="success"),
                                    ]),
                                ]),
                            ], width=6),
                        ], style={"padding": "5px"}),
                    ]),
                ],
                style={"background-color": "rgba(0, 0, 0, 0.5)"},
                id="modal-perfil",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True
                ),  

    # Seção + NOVO ------------------------
            dbc.Row([
                dbc.Col([
                    dbc.Button(color="success", id="open-novo-receita",
                            children=["+ Receita"]),
                ], width=6),

                dbc.Col([
                    dbc.Button(color="primary", id="open-novo-investimento",
                            children=["+ Invest."]),
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Button(color="danger", id="open-novo-despesa",
                            children=["+ Despes"]),
                ], width=6),

                dbc.Col([
                    dbc.Button(color="warning", id="open-novo-gasto",
                            children=["+ GasFut"]),
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Button(color="info", id="open-novo-entrada",
                            children=["+ EntFut"]),
                ], width=6)
            ]),


            # Modal Receita
            html.Div([
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Adicionar receita")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                    dbc.Label("Descrição: "),
                                    dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-receita"),
                            ], width=6), 
                            dbc.Col([
                                    dbc.Label("Valor: "),
                                    dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                            ], width=6)
                        ]),

                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Data: "),
                                dcc.DatePickerSingle(id='date-receitas',
                                    min_date_allowed=date(2020, 1, 1),
                                    max_date_allowed=date(2030, 12, 31),
                                    date=datetime.today(),
                                    style={"width": "100%"}
                                ),
                            ], width=4),

                            dbc.Col([
                                dbc.Label("Extras"),
                                dbc.Checklist(
                                    options=[{"label": "Foi recebida", "value": 1},
                                        {"label": "Receita Recorrente", "value": 2}],
                                    value=[1],
                                    id="switches-input-receita",
                                    switch=True),
                            ], width=4),

                            dbc.Col([
                                html.Label("Categoria da receita"),
                                dbc.Select(id="select_receita", options=[{"label": i, "value": i} for i in cat_receita], value=cat_receita[0])
                            ], width=4)
                        ], style={"margin-top": "25px"}),
                        
                        dbc.Row([
                            dbc.Accordion([
                                    dbc.AccordionItem(children=[
                                            dbc.Row([
                                                dbc.Col([
                                                    html.Legend("Adicionar categoria", style={'color': 'green'}),
                                                    dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita", value=""),
                                                    html.Br(),
                                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                                    html.Br(),
                                                    html.Div(id="category-div-add-receita", style={}),
                                                ], width=6),

                                                dbc.Col([
                                                    html.Legend("Excluir categorias", style={'color': 'red'}),
                                                    dbc.Checklist(
                                                        id="checklist-selected-style-receita",
                                                        options=[{"label": i, "value": i} for i in cat_receita],
                                                        value=[],
                                                        label_checked_style={"color": "red"},
                                                        input_checked_style={"backgroundColor": "#fa7268",
                                                            "borderColor": "#ea6258"},
                                                    ),                                                            
                                                    dbc.Button("Remover", color="warning", id="remove-category-receita", style={"margin-top": "20px"}),
                                                ], width=6)
                                            ]),
                                        ], title="Adicionar/Remover Categorias",
                                    ),
                                ], flush=True, start_collapsed=True, id='accordion-receita'),
                                    
                                    html.Div(id="id_teste_receita", style={"padding-top": "20px"}),
                                
                                    dbc.ModalFooter([
                                        dbc.Button("Adicionar Receita", id="salvar_receita", color="success"),
                                        dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                                        ])
                            ], style={"margin-top": "25px"}),
                        ])
                ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal-novo-receita",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True)
            ]),

            # Modal investimento
            html.Div([
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Adicionar investimento")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                    dbc.Label("Descrição: "),
                                    dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-investimento"),
                            ], width=6), 
                            dbc.Col([
                                    dbc.Label("Valor: "),
                                    dbc.Input(placeholder="$100.00", id="valor_investimento", value="")
                            ], width=6)
                        ]),

                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Data: "),
                                dcc.DatePickerSingle(id='date-investimentos',
                                    min_date_allowed=date(2020, 1, 1),
                                    max_date_allowed=date(2030, 12, 31),
                                    date=datetime.today(),
                                    style={"width": "100%"}
                                ),
                            ], width=4),

                            dbc.Col([
                                dbc.Label("Extras"),
                                dbc.Checklist(
                                    options=[{"label": "Foi recebida", "value": 1},
                                        {"label": "Investimento Recorrente", "value": 2}],
                                    value=[1],
                                    id="switches-input-investimento",
                                    switch=True),
                            ], width=4),

                            dbc.Col([
                                html.Label("Categoria da investimento"),
                                dbc.Select(id="select_investimento", options=[{"label": i, "value": i} for i in cat_investimento], value=cat_investimento[0])
                            ], width=4)
                        ], style={"margin-top": "25px"}),
                        
                        dbc.Row([
                            dbc.Accordion([
                                    dbc.AccordionItem(children=[
                                            dbc.Row([
                                                dbc.Col([
                                                    html.Legend("Adicionar categoria", style={'color': 'green'}),
                                                    dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-investimento", value=""),
                                                    html.Br(),
                                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-investimento", style={"margin-top": "20px"}),
                                                    html.Br(),
                                                    html.Div(id="category-div-add-investimento", style={}),
                                                ], width=6),

                                                dbc.Col([
                                                    html.Legend("Excluir categorias", style={'color': 'red'}),
                                                    dbc.Checklist(
                                                        id="checklist-selected-style-investimento",
                                                        options=[{"label": i, "value": i} for i in cat_investimento],
                                                        value=[],
                                                        label_checked_style={"color": "red"},
                                                        input_checked_style={"backgroundColor": "#fa7268",
                                                            "borderColor": "#ea6258"},
                                                    ),                                                            
                                                    dbc.Button("Remover", color="warning", id="remove-category-investimento", style={"margin-top": "20px"}),
                                                ], width=6)
                                            ]),
                                        ], title="Adicionar/Remover Categorias",
                                    ),
                                ], flush=True, start_collapsed=True, id='accordion-investimento'),
                                    
                                    html.Div(id="id_teste_investimento", style={"padding-top": "20px"}),
                                
                                    dbc.ModalFooter([
                                        dbc.Button("Adicionar Investimento", id="salvar_investimento", color="success"),
                                        dbc.Popover(dbc.PopoverBody("Investimento Salva"), target="salvar_investimento", placement="left", trigger="click"),
                                        ])
                            ], style={"margin-top": "25px"}),
                        ])
                ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal-novo-investimento",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True)
            ]),

            # Modal Entrada Futura
            html.Div([
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Adicionar entrada futura")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                    dbc.Label("Descrição: "),
                                    dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-entrada"),
                            ], width=6), 
                            dbc.Col([
                                    dbc.Label("Valor: "),
                                    dbc.Input(placeholder="$100.00", id="valor_entrada", value="")
                            ], width=6)
                        ]),

                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Data: "),
                                dcc.DatePickerSingle(id='date-entrada',
                                    min_date_allowed=date(2020, 1, 1),
                                    max_date_allowed=date(2030, 12, 31),
                                    date=datetime.today(),
                                    style={"width": "100%"}
                                ),
                            ], width=4),

                            dbc.Col([
                                dbc.Label("Extras"),
                                dbc.Checklist(
                                    options=[{"label": "Foi recebida", "value": 1},
                                        {"label": "Entrada Recorrente", "value": 2}],
                                    value=[1],
                                    id="switches-input-entrada",
                                    switch=True),
                            ], width=4),

                            dbc.Col([
                                html.Label("Categoria da entrada"),
                                dbc.Select(id="select_entrada", options=[{"label": i, "value": i} for i in cat_entrada], value=cat_entrada[0])
                            ], width=4)
                        ], style={"margin-top": "25px"}),
                        
                        dbc.Row([
                            dbc.Accordion([
                                    dbc.AccordionItem(children=[
                                            dbc.Row([
                                                dbc.Col([
                                                    html.Legend("Adicionar categoria", style={'color': 'green'}),
                                                    dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-entrada", value=""),
                                                    html.Br(),
                                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-entrada", style={"margin-top": "20px"}),
                                                    html.Br(),
                                                    html.Div(id="category-div-add-entrada", style={}),
                                                ], width=6),

                                                dbc.Col([
                                                    html.Legend("Excluir categorias", style={'color': 'red'}),
                                                    dbc.Checklist(
                                                        id="checklist-selected-style-entrada",
                                                        options=[{"label": i, "value": i} for i in cat_entrada],
                                                        value=[],
                                                        label_checked_style={"color": "red"},
                                                        input_checked_style={"backgroundColor": "#fa7268",
                                                            "borderColor": "#ea6258"},
                                                    ),                                                            
                                                    dbc.Button("Remover", color="warning", id="remove-category-entrada", style={"margin-top": "20px"}),
                                                ], width=6)
                                            ]),
                                        ], title="Adicionar/Remover Categorias",
                                    ),
                                ], flush=True, start_collapsed=True, id='accordion-entrada'),
                                    
                                    html.Div(id="id_teste_entrada", style={"padding-top": "20px"}),
                                
                                    dbc.ModalFooter([
                                        dbc.Button("Adicionar Entrada", id="salvar_entrada", color="success"),
                                        dbc.Popover(dbc.PopoverBody("Entrada Salva"), target="salvar_entrada", placement="left", trigger="click"),
                                        ])
                            ], style={"margin-top": "25px"}),
                        ])
                ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal-novo-entrada",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True)
            ]),

            # Modal Gasto Futuro
            html.Div([
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Adicionar gasto futuro")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                    dbc.Label("Descrição: "),
                                    dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-gasto"),
                            ], width=6), 
                            dbc.Col([
                                    dbc.Label("Valor: "),
                                    dbc.Input(placeholder="$100.00", id="valor_gasto", value="")
                            ], width=6)
                        ]),

                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Data: "),
                                dcc.DatePickerSingle(id='date-gasto',
                                    min_date_allowed=date(2020, 1, 1),
                                    max_date_allowed=date(2030, 12, 31),
                                    date=datetime.today(),
                                    style={"width": "100%"}
                                ),
                            ], width=4),

                            dbc.Col([
                                dbc.Label("Extras"),
                                dbc.Checklist(
                                    options=[{"label": "Foi recebida", "value": 1},
                                        {"label": "Gasto Recorrente", "value": 2}],
                                    value=[1],
                                    id="switches-input-gasto",
                                    switch=True),
                            ], width=4),

                            dbc.Col([
                                html.Label("Categoria do gasto"),
                                dbc.Select(id="select_gasto", options=[{"label": i, "value": i} for i in cat_gasto], value=cat_gasto[0])
                            ], width=4)
                        ], style={"margin-top": "25px"}),
                        
                        dbc.Row([
                            dbc.Accordion([
                                    dbc.AccordionItem(children=[
                                            dbc.Row([
                                                dbc.Col([
                                                    html.Legend("Adicionar categoria", style={'color': 'green'}),
                                                    dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-gasto", value=""),
                                                    html.Br(),
                                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-gasto", style={"margin-top": "20px"}),
                                                    html.Br(),
                                                    html.Div(id="category-div-add-gasto", style={}),
                                                ], width=6),

                                                dbc.Col([
                                                    html.Legend("Excluir categorias", style={'color': 'red'}),
                                                    dbc.Checklist(
                                                        id="checklist-selected-style-gasto",
                                                        options=[{"label": i, "value": i} for i in cat_gasto],
                                                        value=[],
                                                        label_checked_style={"color": "red"},
                                                        input_checked_style={"backgroundColor": "#fa7268",
                                                            "borderColor": "#ea6258"},
                                                    ),                                                            
                                                    dbc.Button("Remover", color="warning", id="remove-category-gasto", style={"margin-top": "20px"}),
                                                ], width=6)
                                            ]),
                                        ], title="Adicionar/Remover Categorias",
                                    ),
                                ], flush=True, start_collapsed=True, id='accordion-gasto'),
                                    
                                    html.Div(id="id_teste_gasto", style={"padding-top": "20px"}),
                                
                                    dbc.ModalFooter([
                                        dbc.Button("Adicionar Gasto", id="salvar_gasto", color="success"),
                                        dbc.Popover(dbc.PopoverBody("Gasto Salvo"), target="salvar_gasto", placement="left", trigger="click"),
                                        ])
                            ], style={"margin-top": "25px"}),
                        ])
                ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal-novo-gasto",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True)
            ]),

            ### Modal Despesa ###
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle("Adicionar despesa")),
                dbc.ModalBody([
                    dbc.Row([
                        dbc.Col([
                                dbc.Label("Descrição: "),
                                dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-despesa"),
                        ], width=6), 
                        dbc.Col([
                                dbc.Label("Valor: "),
                                dbc.Input(placeholder="$100.00", id="valor_despesa", value="")
                        ], width=6)
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Data: "),
                            dcc.DatePickerSingle(id='date-despesas',
                                min_date_allowed=date(2020, 1, 1),
                                max_date_allowed=date(2030, 12, 31),
                                date=datetime.today(),
                                style={"width": "100%"}
                            ),
                        ], width=4),

                        dbc.Col([
                            dbc.Label("Opções Extras"),
                            dbc.Checklist(
                                options=[{"label": "Foi recebida", "value": 1},
                                    {"label": "despesa Recorrente", "value": 2}],
                                value=[1],
                                id="switches-input-despesa",
                                switch=True),
                        ], width=4),

                        dbc.Col([
                            html.Label("Categoria da despesa"),
                            dbc.Select(id="select_despesa", options=[{"label": i, "value": i} for i in cat_despesa])
                        ], width=4)
                    ], style={"margin-top": "25px"}),
                    
                    dbc.Row([
                        dbc.Accordion([
                                dbc.AccordionItem(children=[
                                    dbc.Row([
                                        dbc.Col([
                                            html.Legend("Adicionar categoria", style={'color': 'green'}),
                                            dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-despesa", value=""),
                                            html.Br(),
                                            dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                                            html.Br(),
                                            html.Div(id="category-div-add-despesa", style={}),
                                        ], width=6),

                                        dbc.Col([
                                            html.Legend("Excluir categorias", style={'color': 'red'}),
                                            dbc.Checklist(
                                                id="checklist-selected-style-despesa",
                                                options=[{"label": i, "value": i} for i in cat_despesa],
                                                value=[],
                                                label_checked_style={"color": "red"},
                                                input_checked_style={"backgroundColor": "#fa7268",
                                                    "borderColor": "#ea6258"},
                                            ),                                                            
                                            dbc.Button("Remover", color="warning", id="remove-category-despesa", style={"margin-top": "20px"}),
                                        ], width=6)
                                    ]),
                                ], title="Adicionar/Remover Categorias",
                                ),
                            ], flush=True, start_collapsed=True, id='accordion-despesa'),
                                                    
                        dbc.ModalFooter([
                            dbc.Button("Adicionar despesa", color="error", id="salvar_despesa", value="despesa"),
                            dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_despesa", placement="left", trigger="click"),
                        ]
                        )
                    ], style={"margin-top": "25px"}),
                ])
            ],
            style={"background-color": "rgba(17, 140, 79, 0.05)"},
            id="modal-novo-despesa",
            size="lg",
            is_open=False,
            centered=True,
            backdrop=True),
        
# Seção NAV ------------------------
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
                    dbc.NavLink("Extratos", href="/extratos", active="exact"),
                    dbc.NavLink("Investimentos", href="/investimentos", active="exact"),
                    dbc.NavLink("Projeção", href="/projecao", active="exact"),
                ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"}),
            ThemeChangerAIO(aio_id="theme", radio_props={"value":dbc.themes.DARKLY})

        ], id='sidebar_completa'
    )




# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output("modal-novo-receita", "is_open"),
    Input("open-novo-receita", "n_clicks"),
    State("modal-novo-receita", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up investimento
@app.callback(
    Output("modal-novo-investimento", "is_open"),
    Input("open-novo-investimento", "n_clicks"),
    State("modal-novo-investimento", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up gasto futuro
@app.callback(
    Output("modal-novo-gasto", "is_open"),
    Input("open-novo-gasto", "n_clicks"),
    State("modal-novo-gasto", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    
# Pop-up entrada futura
@app.callback(
    Output("modal-novo-entrada", "is_open"),
    Input("open-novo-entrada", "n_clicks"),
    State("modal-novo-entrada", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    
# Pop-up despesa
@app.callback(
    Output("modal-novo-despesa", "is_open"),
    Input("open-novo-despesa", "n_clicks"),
    State("modal-novo-despesa", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# Pop-up perfis
@app.callback(
    Output("modal-perfil", "is_open"),
    Input("botao_avatar", "n_clicks"),
    State("modal-perfil", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Add/Remove categoria despesa
@app.callback(
    [Output("category-div-add-despesa", "children"),
    Output("category-div-add-despesa", "style"),
    Output("select_despesa", "options"),
    Output('checklist-selected-style-despesa', 'options'),
    Output('checklist-selected-style-despesa', 'value'),
    Output('stored-cat-despesas', 'data')],

    [Input("add-category-despesa", "n_clicks"),
    Input("remove-category-despesa", 'n_clicks')],

    [State("input-add-despesa", "value"),
    State('checklist-selected-style-despesa', 'value'),
    State('stored-cat-despesas', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_despesa = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt == None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

        else:
            cat_despesa = cat_despesa + [txt] if txt not in cat_despesa else cat_despesa
            txt1 = f'A categoria {txt} foi adicionada com sucesso!'
            style1 = {'color': 'green'}
    
    if n2:
        if len(check_delete) > 0:
            cat_despesa = [i for i in cat_despesa if i not in check_delete]  
    
    opt_despesa = [{"label": i, "value": i} for i in cat_despesa]
    df_cat_despesa = pd.DataFrame(cat_despesa, columns=['Categoria'])
    df_cat_despesa.to_csv("df_cat_despesa.csv")
    data_return = df_cat_despesa.to_dict()

    return [txt1, style1, opt_despesa, opt_despesa, [], data_return]

# Add/Remove categoria investimento
@app.callback(
    [Output("category-div-add-investimento", "children"),
    Output("category-div-add-investimento", "style"),
    Output("select_investimento", "options"),
    Output('checklist-selected-style-investimento', 'options'),
    Output('checklist-selected-style-investimento', 'value'),
    Output('stored-cat-investimentos', 'data')],

    [Input("add-category-investimento", "n_clicks"),
    Input("remove-category-investimento", 'n_clicks')],

    [State("input-add-investimento", "value"),
    State('checklist-selected-style-investimento', 'value'),
    State('stored-cat-investimentos', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_investimento = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt == None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

        else:
            cat_investimento = cat_investimento + [txt] if txt not in cat_investimento else cat_investimento
            txt1 = f'A categoria {txt} foi adicionada com sucesso!'
            style1 = {'color': 'green'}
    
    if n2:
        if len(check_delete) > 0:
            cat_investimento = [i for i in cat_investimento if i not in check_delete]  
    
    opt_investimento = [{"label": i, "value": i} for i in cat_investimento]
    df_cat_investimento = pd.DataFrame(cat_investimento, columns=['Categoria'])
    df_cat_investimento.to_csv("df_cat_investimento.csv")
    data_return = df_cat_investimento.to_dict()

    return [txt1, style1, opt_investimento, opt_investimento, [], data_return]

# Add/Remove categoria gasto futuro
@app.callback(
    [Output("category-div-add-gasto", "children"),
    Output("category-div-add-gasto", "style"),
    Output("select_gasto", "options"),
    Output('checklist-selected-style-gasto', 'options'),
    Output('checklist-selected-style-gasto', 'value'),
    Output('stored-cat-gasto', 'data')],

    [Input("add-category-gasto", "n_clicks"),
    Input("remove-category-gasto", 'n_clicks')],

    [State("input-add-gasto", "value"),
    State('checklist-selected-style-gasto', 'value'),
    State('stored-cat-gasto', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_gasto = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt == None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

        else:
            cat_gasto = cat_gasto + [txt] if txt not in cat_gasto else cat_gasto
            txt1 = f'A categoria {txt} foi adicionada com sucesso!'
            style1 = {'color': 'green'}
    
    if n2:
        if len(check_delete) > 0:
            cat_gasto = [i for i in cat_gasto if i not in check_delete]  
    
    opt_gasto = [{"label": i, "value": i} for i in cat_gasto]
    df_cat_gasto = pd.DataFrame(cat_gasto, columns=['Categoria'])
    df_cat_gasto.to_csv("df_cat_gasto.csv")
    data_return = df_cat_gasto.to_dict()

    return [txt1, style1, opt_gasto, opt_gasto, [], data_return]

# Add/Remove categoria entrada futura
@app.callback(
    [Output("category-div-add-entrada", "children"),
    Output("category-div-add-entrada", "style"),
    Output("select_entrada", "options"),
    Output('checklist-selected-style-entrada', 'options'),
    Output('checklist-selected-style-entrada', 'value'),
    Output('stored-cat-entrada', 'data')],

    [Input("add-category-entrada", "n_clicks"),
    Input("remove-category-entrada", 'n_clicks')],

    [State("input-add-entrada", "value"),
    State('checklist-selected-style-entrada', 'value'),
    State('stored-cat-entrada', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_entrada = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt == None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

        else:
            cat_entrada = cat_entrada + [txt] if txt not in cat_entrada else cat_entrada
            txt1 = f'A categoria {txt} foi adicionada com sucesso!'
            style1 = {'color': 'green'}
    
    if n2:
        if len(check_delete) > 0:
            cat_entrada = [i for i in cat_entrada if i not in check_delete]  
    
    opt_entrada = [{"label": i, "value": i} for i in cat_entrada]
    df_cat_entrada = pd.DataFrame(cat_entrada, columns=['Categoria'])
    df_cat_entrada.to_csv("df_cat_entrada.csv")
    data_return = df_cat_entrada.to_dict()

    return [txt1, style1, opt_entrada, opt_entrada, [], data_return]

# Add/Remove categoria receita
@app.callback(
    [Output("category-div-add-receita", "children"),
    Output("category-div-add-receita", "style"),
    Output("select_receita", "options"),
    Output('checklist-selected-style-receita', 'options'),
    Output('checklist-selected-style-receita', 'value'),
    Output('stored-cat-receitas', 'data')],

    [Input("add-category-receita", "n_clicks"),
    Input("remove-category-receita", 'n_clicks')],

    [State("input-add-receita", "value"),
    State('checklist-selected-style-receita', 'value'),
    State('stored-cat-receitas', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_receita = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt == None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

    if n and not(txt == "" or txt == None):
        cat_receita = cat_receita + [txt] if txt not in cat_receita else cat_receita
        txt1 = f'A categoria {txt} foi adicionada com sucesso!'
        style1 = {'color': 'green'}
    
    if n2:
        if check_delete == []:
            pass
        else:
            cat_receita = [i for i in cat_receita if i not in check_delete]  
    
    opt_receita = [{"label": i, "value": i} for i in cat_receita]
    df_cat_receita = pd.DataFrame(cat_receita, columns=['Categoria'])
    df_cat_receita.to_csv("df_cat_receita.csv")
    data_return = df_cat_receita.to_dict()

    return [txt1, style1, opt_receita, opt_receita, [], data_return]

# Enviar Form receita
@app.callback(
    Output('store-receitas', 'data'),

    Input("salvar_receita", "n_clicks"),

    [
        State("txt-receita", "value"),
        State("valor_receita", "value"),
        State("date-receitas", "date"),
        State("switches-input-receita", "value"),
        State("select_receita", "value"),
        State('store-receitas', 'data')
    ]
)
def salve_form_receita(n, descricao, valor, date, switches, categoria, dict_receitas):
    df_receitas = pd.DataFrame(dict_receitas)

    if n and not(valor == "" or valor== None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        df_receitas.loc[df_receitas.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_receitas.to_csv("df_receitas.csv")

    data_return = df_receitas.to_dict()
    return data_return

# Enviar Form investimento
@app.callback(
    Output('store-investimentos', 'data'),

    Input("salvar_investimento", "n_clicks"),

    [
        State("txt-investimento", "value"),
        State("valor_investimento", "value"),
        State("date-investimentos", "date"),
        State("switches-input-investimento", "value"),
        State("select_investimento", "value"),
        State('store-investimentos', 'data')
    ]
)
def salve_form_investimento(n, descricao, valor, date, switches, categoria, dict_investimento):
    df_investimentos = pd.DataFrame(dict_investimento)

    if n and not(valor == "" or valor== None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        df_investimentos.loc[df_investimentos.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_investimentos.to_csv("df_investimento.csv")

    data_return = df_investimentos.to_dict()
    return data_return

# Enviar Form gasto futuro
@app.callback(
    Output('store-gasto', 'data'),

    Input("salvar_gasto", "n_clicks"),

    [
        State("txt-gasto", "value"),
        State("valor_gasto", "value"),
        State("date-gasto", "date"),
        State("switches-input-gasto", "value"),
        State("select_gasto", "value"),
        State('store-gasto', 'data')
    ]
)
def salve_form_gasto(n, descricao, valor, date, switches, categoria, dict_gasto):
    df_gasto = pd.DataFrame(dict_gasto)

    if n and not(valor == "" or valor== None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        df_gasto.loc[df_gasto.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_gasto.to_csv("df_gasto.csv")

    data_return = df_gasto.to_dict()
    return data_return

# Enviar Form entrada futura
@app.callback(
    Output('store-entrada', 'data'),

    Input("salvar_entrada", "n_clicks"),

    [
        State("txt-entrada", "value"),
        State("valor_entrada", "value"),
        State("date-entrada", "date"),
        State("switches-input-entrada", "value"),
        State("select_entrada", "value"),
        State('store-entrada', 'data')
    ]
)
def salve_form_entrada(n, descricao, valor, date, switches, categoria, dict_entrada):
    df_entrada = pd.DataFrame(dict_entrada)

    if n and not(valor == "" or valor== None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        df_entrada.loc[df_entrada.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_entrada.to_csv("df_entrada.csv")

    data_return = df_entrada.to_dict()
    return data_return

# Enviar Form despesa
@app.callback(
    Output('store-despesas', 'data'),

    Input("salvar_despesa", "n_clicks"),

    [
        State("txt-despesa", "value"),
        State("valor_despesa", "value"),
        State("date-despesas", "date"),
        State("switches-input-despesa", "value"),
        State("select_despesa", "value"),
        State('store-despesas', 'data')
    ])
def salve_form_despesa(n, descricao, valor, date, switches, categoria, dict_despesas):
    df_despesas = pd.DataFrame(dict_despesas)

    if n and not(valor == "" or valor== None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        df_despesas.loc[df_despesas.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_despesas.to_csv("df_despesas.csv")

    data_return = df_despesas.to_dict()
    
    return data_return