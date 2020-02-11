# IMDBolsasBot

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](blob/master/LICENSE)

Bot de alimentação do canal [IMD Bolsas](https://t.me/imdbolsas) no Telegram. Seu objetivo é alertar estudantes do instituto sobre bolsas e vagas de estágio.

## Iniciando

Essas instruções lhe darão uma cópia do projeto e um caminho para executá-lo localmente para fins de desenvolvimento e teste. Vide as notas de deployment para entender como fazer deploy.

### Pré-Requisitos

Você precisará basicamente do Python 3.7 ou superior instalado na sua máquina.

### Ambiente Virtual

Recomendo fortemente que você utilize um ambiente virtual para rodar esse projeto, de modo a isolar os pacotes externos instalados e manter seu escopo global limpo.
Caso não esteja familizarizado com esse conceito, recomendo esta excelente leitura rápida: "[Gerenciamento de Ambientes Python com pyenv](https://medium.com/operacionalti/gerenciamento-de-ambientes-python-com-pyenv-3ce71eb1a2c3)".

### Variáveis de Ambiente

O arquivo .env.example contém a relação das variáveis de ambiente que o bot precisa para funcionar. Defina-as antes de executar o projeto.

### Instalação

Clone esse repositório via Git ou baixe-o em um arquivo .zip aqui mesmo no GitHub. Em seguia, instale as dependências:

```bash
pip -r requirements.txt
```

Para rodar somente a spider, execute o seguinte comando:

```bash
python -m scrapy crawl news -o news.json
```

> O argumento "-o" define um arquivo para salvamento dos dados coletados.

Para ativar o bot, simplesmente execute o arquivo ```script.py```:

```bash
python script.py
```

## Deployment

O deploy desse projeto deve ser realizado conforme as instruções presentes [neste guia](https://github.com/michaelkrukov/heroku-python-script).

## Construído Com

* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Uma moderna e simples biblioteca de templating para Python.
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot/) - Um wrapper irrecusável para a construção de bots para o Telegram.
* [Scrapy](https://scrapy.org/) - Um framework rápido e poderoso de web crawling.
* [SQLAlchemy](https://www.sqlalchemy.org/) - Um kit de ferramentas SQL que fornece flexibilidade e poder a aplicações.

## Contribuições

Sinta-se absolutamente à vontade para contribuir.

## Licença

Esse projeto é distribuído sob a Licença MIT. Leia o arquivo [LICENCE](LICENCE) para ter mais detalhes.
