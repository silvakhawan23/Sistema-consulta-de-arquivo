#Autor: Khawan Silva,Kamila Antonia,Lucas Galileu,Joelson Junior
#Data: 09/Nov/2023
#Email: kha@mail.com

import json
import os

def carregar_json():

    """
    Função para carregar a estrutura no arquivo estoque.json.
    
    Retorno:
        (list) - Estrutura carregada
    """
    if not os.path.exists('estoque.json'):
        return dict()
    with open("estoque.json", "r") as arq:
        estoque = json.load(arq)
    return estoque
     
estoque_produtos = carregar_json()

def salvar_json():
    """ Aqui e escreve um novo arquivo caso ele sofra alguam alteração ele ira
        salvar com as novas alteraçoes
    """
    try:
        with open('estoque.json', 'w') as f:
            f.write(json.dumps(estoque_produtos))
            return estoque_produtos
    except Exception as e:
        print(f"Erro ao salvar o arquivo JSON: {e}")
        

def inserir_produto():
    """  Função para inserir novos produtos no estoque
    """
    nome = input('Nome do Produto: ')
    ano = input('Ano: ')
    preco = float(input('Preço do Produto: '))
    qtde_estoque = int(input('Quantidade em estoque: '))
    qtde_vendas = int(input('Quantidade vendida: '))
    if estoque_produtos == dict():
        codigo = 1
    else:
        codigo = 1 + max([int(key) for key in estoque_produtos.keys()])
    estoque_produtos[str(codigo)] = [nome, ano, preco, qtde_estoque, qtde_vendas]
    salvar_json()
    
    
def aumentar_estoque():
    """
       Função Para aumentar a qauntidade de produtos no estoque

    """
    codigo = input('Digite um código: ')
    qtd=int(input("digite a quantidade a ser Adicionada"))
    if codigo in estoque_produtos:
        _, _, _, qtde_estoque, _ = estoque_produtos[codigo]
        estoque_produtos[codigo][3] = qtde_estoque + qtd
        salvar_json() 
        print(f'Estoque do produto {codigo} aumentado em {qtd} unidades.')
    else:
        print('Produto inexistente.')
        
def diminuir_estoque():
    """ Função para subtrair a quantidade de algum produto"""
    codigo = input('Digite um código: ')
    if codigo in estoque_produtos:
        qtd = int(input("Digite a quantidade a ser subtraída: "))
        if qtd > estoque_produtos[codigo][3]:
            print("Seu estoque ficará negativo. Digite um valor igual ou menor que o estoque atual.")
        else:
            _, _, _, qtde_estoque, _ = estoque_produtos[codigo]
            estoque_produtos[codigo][3] = qtde_estoque - qtd
            salvar_json() 
            print(f'Estoque do produto {codigo} diminuído em {qtd} unidades.')
    else:
        print('Produto inexistente.')

def consultar_produto():
    """Função responsavel por mostrar as informações de um produto especifico"""

    codigo = input('Digite um código: ')
    if codigo in estoque_produtos.keys():
        nome, ano, preco, qtde_estoque, qtde_vendas = estoque_produtos[codigo]
        print('Nome: ', nome)
        print('Ano: ', ano)
        print('Preço: ', preco)
        print('Quantidade em estoque: ', qtde_estoque)
        print('Quantidade vendida: ', qtde_vendas)
    else:
        print('Produto Inexistente')
        
def calcular_faturamento():
    """ Função responsavel por pegar as vendas realizadas no estoque e calcular o faturamento"""
    faturamento_total = 0
    for codigo, detalhes in estoque_produtos.items():
        _, _, preco, _, qtde_vendas = detalhes
        faturamento_total += preco * qtde_vendas
    return print(f'''Seu Faturamento atual é de : R${faturamento_total:.2f}''')

    
def registrar_venda():
    """ Função responsavel por realizar as vendas e alterar a quantidade de vendas no estoque"""
    if not estoque_produtos:
        print('Sem produtos cadastrados.')
        return
    codigo = input('Código do produto: ')
    if codigo in estoque_produtos.keys():
        if estoque_produtos[codigo][3] > 0:
            estoque_produtos[codigo][3] -= 1
            estoque_produtos[codigo][4] += 1
            salvar_json()
            print('Venda registrada!')
        else:
            print('Sem estoque')
    else:
        print('Produto inexistente')

def consulta_estoque():
    """ Função responsavel por mostrar todo o estoque """
    print('')
    if not estoque_produtos:
        print("Sem estoque")
    else:
        print(f'|{"Código":<8}|{"Nome":<45}|{"Ano":<6}|{"Preço":<10}|{"Estoque":<7} |{"Vendas":<3}|')
        for codigo, detalhes in estoque_produtos.items():
            if len(detalhes) == 5:
                nome, ano, preco, qtde_estoque, qtde_vendas = detalhes
                print(f'|{codigo:<8}|{nome:<45}|{ano:<6}|{preco:<10.2f}|{qtde_estoque:<8}|{qtde_vendas:<3}|')
            else:
                print(f'Erro nos dados do produto {codigo}: {detalhes}')
        print('')
def Menu():
    """Função responsavel por mostar o menu de escolhas a ser realizadas pelo codigo """
    while True:
        opcao = input('*****Eletrocasas cuiaba*****\n'
                      '1 - Cadastrar produto\n'
                      '2 - Consultar produto\n'
                      '3 - Consultar Estoque\n'
                      '4 - Realizar Vendas\n'
                      '5 - Calcular Faturamento total\n'
                      '6 - Aumentar Estoque\n'
                      '7 - Diminuir Estoque\n'
                      '8 - Sair\n'
                      'Digite sua opção: ')

        if opcao == '1':
            inserir_produto()
        elif opcao == '2':
            consultar_produto()
        elif opcao == '3':
            consulta_estoque()
        elif opcao == '4':
            registrar_venda()
        elif opcao == '5':
            calcular_faturamento()
        elif opcao == '6':
            aumentar_estoque()
        elif opcao == '7':
            diminuir_estoque()
        elif opcao == '8':
            print('Muito Obrigado')
            break  
        else:
            print('Opção inválida. Tente novamente.')
    

if __name__ == '__main__':
        Menu()
       