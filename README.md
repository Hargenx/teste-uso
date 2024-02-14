# Experimento Flask com IDE idx da Google

Este é um pequeno experimento usando o Flask, um framework web em Python, juntamente com a IDE idx da Google para criar um aplicativo simples de cadastro. O objetivo é demonstrar como criar uma aplicação web básica e realizar um cadastro simples de nome, telefone e email e testar a funcionalidade da IDE.

## Requisitos

Certifique-se de ter Python instalado em seu ambiente de desenvolvimento. Além disso, é recomendável criar um ambiente virtual para isolar as dependências do projeto.

```bash
# Criar um ambiente virtual
python -m venv venv
```
# Ativar o ambiente virtual (no Windows)
```bash
venv\Scripts\activate
```

# Ativar o ambiente virtual (no macOS/Linux)
```bash
source venv/bin/activate
```

# Instale as dependências usando o arquivo requirements.txt:
```bash
pip install -r requirements.txt
```

## Executando o Aplicativo

Para iniciar o aplicativo, execute o seguinte comando no terminal:
```bash
python main.py
```
Isso iniciará o servidor Flask na porta 80 (ou na porta especificada pela variável de ambiente PORT). Acesse http://localhost:80/ no seu navegador para visualizar o formulário de cadastro.

## Funcionalidades
- *Cadastro Simples*: Preencha o formulário com nome, telefone e email e clique no botão "Cadastrar".

- *Ações com os Dados*: Os dados do cadastro são processados pela rota /cadastro no arquivo main.py. Você pode personalizar essa rota para realizar ações específicas com os dados, como salvá-los em um banco de dados.

## Nota
Este é um experimento básico e não deve ser utilizado em ambientes de produção.

Esse código foi desenvolvido como parte de um pequeno teste de uso da IDE idx da Google para experimentação com aplicativos web em Python. Certifique-se de revisar e adaptar o código conforme necessário para atender aos requisitos específicos do seu projeto.

Autor: Raphael Mauricio Sanches de Jesus

Data: 2024