# Processamento de Arquivo Excel com Pandas

## Descrição

Este script realiza a leitura de um arquivo Excel, remove colunas específicas e salva o resultado em um novo arquivo Excel.

O objetivo é automatizar a limpeza de uma base de dados, permitindo que o usuário escolha quais colunas deseja remover antes de gerar o novo arquivo tratado.

## Tecnologias utilizadas

* Python
* Pandas
* OpenPyXL

## Como funciona

O script executa as seguintes etapas:

1. Lê um arquivo Excel de entrada.
2. Remove as colunas definidas pelo usuário no código.
3. Salva o resultado em um novo arquivo Excel.
4. Exibe uma mensagem informando que o processamento foi concluído.

## Código principal

```python
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
```

## Colunas removidas

As colunas removidas são definidas na lista dentro do método `drop()`:

```python
df = df.drop(columns=[
    "ID", 
    "Celular", 
    "Reset Senha", 
    "Senha Alterável", 
    "Idioma", 
    "IDs Funções", 
    "IDs Departamentos/Cargos"
])
```

Para remover outras colunas, basta editar essa lista, adicionando ou removendo os nomes das colunas desejadas.

Exemplo:

```python
df = df.drop(columns=[
    "Nome da Coluna 1",
    "Nome da Coluna 2",
    "Nome da Coluna 3"
])
```

## Arquivo de entrada

O arquivo de entrada utilizado no script é:

```text
C:\Users\thiago.betta\Documents\Python\teste1.xlsx
```

Caso o arquivo esteja em outro local, altere o caminho informado no `pd.read_excel()`.

## Arquivo de saída

Após o processamento, será gerado o arquivo:

```text
testesaida.xlsx
```

O nome do arquivo de saída pode ser alterado modificando o valor usado em `df.to_excel()`.

Exemplo:

```python
df.to_excel("arquivo_tratado.xlsx", index=False)
```

## Como executar

1. Instale as dependências necessárias:

```bash
pip install pandas openpyxl
```

2. Certifique-se de que o arquivo Excel de entrada existe no caminho informado.

3. Edite a lista de colunas que deseja remover, caso necessário.

4. Execute o script:

```bash
python main.py
```

5. Após a execução, o arquivo tratado será salvo com o nome definido no código.

## Observações

* As colunas a serem removidas podem ser escolhidas pelo usuário.
* Os nomes das colunas devem estar escritos exatamente como aparecem no arquivo Excel.
* Caso alguma coluna informada não exista no arquivo, o script poderá apresentar erro.
* O caminho do arquivo de entrada pode ser alterado conforme a localização do arquivo no computador.
* O nome do arquivo de saída também pode ser personalizado.

