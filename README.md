# Sistema-consulta-de-arquivo
Sistema de Controle de Estoque - Eletrocasas Cuiabá
Descrição
Este projeto é um sistema de controle de estoque simples desenvolvido para a gestão de produtos de uma loja fictícia chamada Eletrocasas Cuiabá. O sistema permite cadastrar produtos, consultar estoque, realizar vendas, calcular faturamento e gerenciar o estoque (aumentar e diminuir quantidades).

O sistema armazena os dados em um arquivo JSON chamado estoque.json e oferece um menu interativo para que o usuário possa realizar diversas operações.

Funcionalidades
O sistema oferece as seguintes funcionalidades:

Cadastrar Produto: Permite o cadastro de novos produtos no estoque, incluindo nome, ano de fabricação, preço, quantidade em estoque e quantidade vendida.
Consultar Produto: Exibe as informações detalhadas de um produto a partir do código do produto.
Consultar Estoque: Exibe uma lista de todos os produtos cadastrados no estoque, incluindo o código, nome, ano, preço, quantidade em estoque e quantidade vendida.
Realizar Vendas: Permite registrar a venda de um produto, alterando a quantidade em estoque e a quantidade vendida.
Calcular Faturamento Total: Calcula o faturamento total com base nas vendas realizadas.
Aumentar Estoque: Permite aumentar a quantidade de um produto no estoque.
Diminuir Estoque: Permite diminuir a quantidade de um produto no estoque (caso haja estoque suficiente).
Tecnologias Utilizadas
Python 3
JSON (para persistência de dados)
Como Usar
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/eletrocasas-cuiaba.git
Navegue até o diretório do projeto:

bash
Copiar código
cd eletrocasas-cuiaba
Execute o script Python:

bash
Copiar código
python estoque.py
O menu de opções será exibido, e você poderá interagir com o sistema.

Estrutura do Arquivo estoque.json
O arquivo estoque.json é usado para armazenar os dados do estoque e deve ter a seguinte estrutura:

json
Copiar código
{
    "1": ["Produto 1", "2023", 50.0, 100, 30],
    "2": ["Produto 2", "2022", 100.0, 200, 50]
}
Cada produto é identificado por um código numérico, e os detalhes de cada produto são armazenados em uma lista com os seguintes campos:

Nome
Ano de Fabricação
Preço
Quantidade em Estoque
Quantidade Vendida
Contribuições
Este projeto é mantido por Khawan Silva, Kamila Antonia, Lucas Galileu e Joelson Junior.

Se desejar contribuir, envie um pull request ou crie uma issue para sugerir melhorias ou correções.
