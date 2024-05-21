# Projeto Técnico

## Visão Geral

Este é um projeto técnico que consiste em um pipeline de dados dividido em três partes principais: extração, transformação e testes. O objetivo deste projeto é fornecer uma solução para capturar, processar e validar dados de indices do site CompassFT de forma eficiente e salvar em um dataframe pandas.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:


### `src/`

Contém os módulos de extração e transformação de dados.

- `extract/`: Contém o script `crawler.py` responsável pela extração dos dados.
- `transform/`: Contém o script `transform_dataframe.py` responsável pela transformação dos dados.

### `tests/`

Contém os testes unitários para verificar a funcionalidade dos scripts de extração e transformação.


### `main.py`

Contém a lógica principal para execução do projeto.


## Requisitos

Para executar este projeto, você precisará dos seguintes requisitos:

- Python 3.10 ou superior
- Bibliotecas listadas no arquivo `requirements.txt`

## Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/wesleyolvr/Crawler_CompassFT.git
```
2. Navegue até o diretório do projeto:
```bash
cd teste_tecnico
```
3. Crie um ambiente virtual e ative-o:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```
4. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

## Uso

Voce pode executar o arquivo principal que fará a execução do pipeline:

```bash
python main.py
```