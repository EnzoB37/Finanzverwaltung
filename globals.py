<<<<<<< HEAD:projeto_completo/globals.py
import pandas as pd
import os

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()) and ("df_gasto.csv" in os.listdir()) and ("df_investimento.csv" in os.listdir()) and ("df_entrada.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
    df_investimentos = pd.read_csv("df_investimento.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
    df_gasto = pd.read_csv("df_gasto.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
    df_entrada = pd.read_csv("df_entrada.csv", index_col=0, parse_dates=True, date_format="%Y/%m/%d")
    df_despesas["Data"] = pd.to_datetime(df_despesas["Data"])
    df_receitas["Data"] = pd.to_datetime(df_receitas["Data"])
    df_investimentos["Data"] = pd.to_datetime(df_investimentos["Data"])
    df_gasto["Data"] = pd.to_datetime(df_gasto["Data"])
    df_entrada["Data"] = pd.to_datetime(df_entrada["Data"])
    df_despesas["Data"] = df_despesas["Data"].apply(lambda x: x.date())
    df_receitas["Data"] = df_receitas["Data"].apply(lambda x: x.date())
    df_investimentos["Data"] = df_investimentos["Data"].apply(lambda x: x.date())
    df_gasto["Data"] = df_gasto["Data"].apply(lambda x: x.date())
    df_entrada["Data"] = df_entrada["Data"].apply(lambda x: x.date())

else:
    data_structure = {'Valor':[],
        'Efetuado':[],
        'Fixo':[],
        'Data':[],
        'Categoria':[],
        'Descrição':[],}

    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_investimentos = pd.DataFrame(data_structure)
    df_gasto = pd.DataFrame(data_structure)
    df_entrada = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv")
    df_receitas.to_csv("df_receitas.csv")
    df_investimentos.to_csv("df_investimento.csv")
    df_gasto.to_csv("df_gasto.csv")
    df_entrada.to_csv("df_entrada.csv")


if ("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()) and ("df_cat_gasto.csv" in os.listdir()) and ("df_cat_investimento.csv" in os.listdir()) and ("df_cat_entrada.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0)
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0)
    df_cat_investimento = pd.read_csv("df_cat_investimento.csv", index_col=0)
    df_cat_gasto = pd.read_csv("df_cat_gasto.csv", index_col=0)
    df_cat_entrada = pd.read_csv("df_cat_entrada.csv", index_col=0)
    cat_receita = df_cat_receita.values.tolist()
    cat_despesa = df_cat_despesa.values.tolist()
    cat_investimento = df_cat_investimento.values.tolist()
    cat_gasto = df_cat_gasto.values.tolist()
    cat_entrada = df_cat_entrada.values.tolist()

else:    
    cat_receita = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
    cat_despesa = {'Categoria': ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer"]}
    cat_investimento = {'Categoria': ["Caixinha", "Dólares", "Ações"]}
    cat_gasto = {'Categoria': ["Comissão", "Fardamento"]}
    cat_entrada = {'Categoria': ["Soldo", "Carona", "Presente"]}
    
    df_cat_receita = pd.DataFrame(cat_receita, columns=['Categoria'])
    df_cat_despesa = pd.DataFrame(cat_despesa, columns=['Categoria'])
    df_cat_investimento = pd.DataFrame(cat_investimento, columns=['Categoria'])
    df_cat_gasto = pd.DataFrame(cat_gasto, columns=['Categoria'])
    df_cat_entrada = pd.DataFrame(cat_entrada, columns=['Categoria'])
    df_cat_receita.to_csv("df_cat_receita.csv")
    df_cat_despesa.to_csv("df_cat_despesa.csv")
    df_cat_investimento.to_csv("df_cat_investimento.csv")
    df_cat_gasto.to_csv("df_cat_gasto.csv")
    df_cat_entrada.to_csv("df_cat_entrada.csv")
=======
import pandas as pd
import os

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()) and ("df_investimento.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
    df_investimentos = pd.read_csv("df_investimento.csv", index_col=0, parse_dates=True)
    df_despesas["Data"] = pd.to_datetime(df_despesas["Data"])
    df_receitas["Data"] = pd.to_datetime(df_receitas["Data"])
    df_investimentos["Data"] = pd.to_datetime(df_investimentos["Data"])
    df_despesas["Data"] = df_despesas["Data"].apply(lambda x: x.date())
    df_receitas["Data"] = df_receitas["Data"].apply(lambda x: x.date())
    df_investimentos["Data"] = df_investimentos["Data"].apply(lambda x: x.date())

else:
    data_structure = {'Valor':[],
        'Efetuado':[],
        'Fixo':[],
        'Data':[],
        'Categoria':[],
        'Descrição':[],}

    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_investimentos = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv")
    df_receitas.to_csv("df_receitas.csv")
    df_investimentos.to_csv("df_investimento.csv")


if ("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()) and ("df_cat_investimento.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0)
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0)
    df_cat_investimento = pd.read_csv("df_cat_investimento.csv", index_col=0)
    cat_receita = df_cat_receita.values.tolist()
    cat_despesa = df_cat_despesa.values.tolist()
    cat_investimento = df_cat_investimento.values.tolist()

else:    
    cat_receita = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
    cat_despesa = {'Categoria': ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer"]}
    cat_investimento = {'Categoria': ["Caixinha", "Dólares", "Ações"]}
    
    df_cat_receita = pd.DataFrame(cat_receita, columns=['Categoria'])
    df_cat_despesa = pd.DataFrame(cat_despesa, columns=['Categoria'])
    df_cat_investimento = pd.DataFrame(cat_investimento, columns=['Categoria'])
    df_cat_receita.to_csv("df_cat_receita.csv")
    df_cat_despesa.to_csv("df_cat_despesa.csv")
    df_cat_investimento.to_csv("df_cat_investimento.csv")
>>>>>>> 23caa3f101c976c15d75672143eb8a5bdcd9fb77:globals.py
