
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Analisador:

    def __init__(self, caminho):
        self.dados = pd.read_csv(caminho)
        self.dados = self.dados.dropna()

        self.dados["Date"] = pd.to_datetime(
            self.dados["Date"]
        )

    def visualizar_dados(self):
        print(self.dados.head())

    def estatisticas(self):
        print("\nESTATISTICAS GERAIS")
        print(self.dados.describe())

        print("\nFATURAMENTO TOTAL:")
        print(self.dados["Total Amount"].sum())

        print("\nMEDIA DAS VENDAS:")
        print(self.dados["Total Amount"].mean())

    def vendas_por_data(self):
        vendas = self.dados.groupby("Date")["Total Amount"].sum()

        vendas.plot(kind="line")
        plt.title("Vendas por Data")
        plt.xlabel("Data")
        plt.ylabel("Valor das Vendas")
        plt.tight_layout()
        plt.show()

    def vendas_por_categoria(self):
        vendas = self.dados.groupby("Product Category")["Total Amount"].sum()

        vendas.plot(kind="bar")
        plt.title("Vendas por Categoria")
        plt.xlabel("Categoria")
        plt.ylabel("Valor das Vendas")
        plt.tight_layout()
        plt.show()

    def histograma_vendas(self):
        sns.histplot(self.dados["Total Amount"], bins=10)

        plt.title("Distribuição dos Valores de Vendas")
        plt.xlabel("Valor das Vendas")
        plt.ylabel("Quantidade")
        plt.tight_layout()
        plt.show()
