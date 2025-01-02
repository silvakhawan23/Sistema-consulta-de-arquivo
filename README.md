# Sistema de Gestão de Estoque

Este repositório contém um sistema de gestão de estoque desenvolvido em Python. O sistema permite o cadastro de produtos, controle de estoque, registro de vendas e cálculo do faturamento. Ele utiliza um arquivo JSON para armazenar as informações do estoque de forma persistente.

## Autor
- **Khawan Silva**

## Data
- **09/Nov/2023**

## Email
- **kfkhawan@gmail.com**

## Funcionalidades

- Cadastro de novos produtos no estoque.
- Consulta de produtos individuais no estoque.
- Visualização de todo o estoque com detalhes.
- Realização de vendas com atualização do estoque.
- Aumento ou diminuição da quantidade de produtos em estoque.
- Cálculo do faturamento total com base nas vendas realizadas.

## Estrutura de Dados

O sistema armazena os dados de produtos no arquivo `estoque.json` no formato JSON. Cada produto possui os seguintes atributos:

- **Código**: Identificador único do produto.
- **Nome**: Nome do produto.
- **Ano**: Ano de fabricação do produto.
- **Preço**: Preço do produto.
- **Quantidade em Estoque**: Quantidade disponível do produto.
- **Quantidade Vendida**: Quantidade do produto já vendida.

## Funções do Sistema

### 1. `carregar_json()`

Carrega a estrutura do arquivo `estoque.json` e retorna um dicionário com os dados do estoque.

### 2. `salvar_json()`

Salva as alterações feitas no estoque de volta no arquivo `estoque.json`.

### 3. `inserir_produto()`

Permite o cadastro de novos produtos no estoque, atribuindo um código único a cada produto.

### 4. `aumentar_estoque()`

Permite aumentar a quantidade de um produto específico no estoque.

### 5. `diminuir_estoque()`

Permite diminuir a quantidade de um produto específico no estoque, com a verificação de que o estoque não ficará negativo.

### 6. `consultar_produto()`

Consulta e exibe os detalhes de um produto específico a partir de seu código.

### 7. `calcular_faturamento()`

Calcula e exibe o faturamento total das vendas realizadas até o momento.

### 8. `registrar_venda()`

Registra uma venda, subtraindo uma unidade do produto do estoque e somando à quantidade de vendas realizadas.

### 9. `consulta_estoque()`

Exibe todos os produtos no estoque com seus respectivos detalhes.

### 10. `Menu()`

Exibe o menu de opções para o usuário interagir com o sistema.

## Exemplo de Uso

O sistema é executado via terminal, onde o usuário pode escolher entre as opções de cadastrar produto, consultar produtos, registrar vendas, aumentar/diminuir estoque, calcular faturamento ou sair.

Exemplo de execução do menu:

```bash
*****Eletrocasas Cuiaba*****
1 - Cadastrar produto
2 - Consultar produto
3 - Consultar Estoque
4 - Realizar Vendas
5 - Calcular Faturamento total
6 - Aumentar Estoque
7 - Diminuir Estoque
8 - Sair
Digite sua opção: 
