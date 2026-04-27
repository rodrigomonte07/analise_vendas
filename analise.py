import pandas as pd

try: 
    df = pd.read_csv("vendas.csv")
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
    exit()

print("Primeiras linhas do Dataset:")
print(df.head())

print("\n Informações da Estrutura dos dados:")
print(df.info())

print("\n Total de valores nulos por coluna:")
print(df.isnull().sum())

df['faturamento'] = df['quantidade'] * df['preco_unitario']

faturamento_total = df["faturamento"].sum()
print(f"\n O Faturamento total é de R$ {faturamento_total:,.2f}")

top_produtos = df.groupby("produto")['quantidade'].sum().sort_values(ascending=False).head(5)
print("\n Top 5 produtos mais vendidos:")
print(top_produtos)

faturamento_categoria = df.groupby("produto")['categoria'].sum().sort_values(ascending=False)
print("\n Faturamento por categoria:")
print(faturamento_categoria)