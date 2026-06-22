import pandas as pd

# Lê o arquivo Excel
df = pd.read_excel(r"C:\Users\thiago.betta\Documents\Python\teste1.xlsx")

# Remove as colunas desejadas
df = df.drop(columns=[
    "ID", 
    "Celular", 
    "Reset Senha", 
    "Senha Alterável", 
    "Idioma", 
    "IDs Funções", 
    "IDs Departamentos/Cargos"
])

# Salva o resultado em um novo arquivo
df.to_excel("testesaida.xlsx", index=False)

print("Arquivo processado com sucesso!")