from src.analisador import Analisador

def menu():
    try:
        analisador = Analisador("data/retail_sales_dataset.csv")

        while True:
            print("\n===== SISTEMA DE ANÁLISE DE DADOS =====")
            print("1 - Visualizar dados")
            print("2 - Estatísticas gerais")
            print("3 - Gráfico de vendas por data")
            print("4 - Gráfico de vendas por categoria")
            print("5 - Histograma de vendas")
            print("6 - Sair")

            try:
                opcao = int(input("\nEscolha uma opção: "))

                if opcao == 1:
                    analisador.visualizar_dados()
                elif opcao == 2:
                    analisador.estatisticas()
                elif opcao == 3:
                    analisador.vendas_por_data()
                elif opcao == 4:
                    analisador.vendas_por_categoria()
                elif opcao == 5:
                    analisador.histograma_vendas()
                elif opcao == 6:
                    print("Encerrando o sistema...")
                    break
                else:
                    print("Opção inválida!")

            except ValueError:
                print("Digite apenas números!")

    except FileNotFoundError:
        print("Arquivo CSV não encontrado!")
    except Exception as erro:
        print("Erro:", erro)


if __name__ == "__main__":
    menu()