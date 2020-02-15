<h1 align="center">IMDBolsasBot</h1>

<p align="center">
    <a href="https://www.python.org/">
        <img alt="Made With Python Badge" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg">
    </a>
    <a href="blob/master/LICENSE">
        <img alt="MIT License Badge" src="http://img.shields.io/badge/license-MIT-blue.svg?style=flat">
    </a>
</p>

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
Caso prefira carregar essas variáveis localmente, copie o arquivo ```.env.example``` para um arquivo ```.env```:

```bash
cp .env.example .env
```

Em seguida, edite o novo arquivo, inserindo os valores das variáveis.

### Instalação

Clone esse repositório via Git ou baixe-o em um arquivo .zip aqui mesmo no GitHub. Em seguida, instale as dependências:

```bash
pip -r requirements.txt
```

Para rodar somente a spider, execute o seguinte comando:

```bash
python -m scrapy crawl imdnews -o news.json
```

> O argumento "-o" define um arquivo para salvamento dos dados retornados pela spider.

Para ativar o bot, simplesmente execute o arquivo ```bot.py```:

```bash
python bot.py
```

## Deployment

Atualmente, esse projeto tem seu deploy realizado no Heroku. Para replicar isso, siga as instruções presentes [neste guia](https://github.com/michaelkrukov/heroku-python-script).

## Construído Com

* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Uma moderna e simples biblioteca de templating para Python.
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot/) - Um wrapper irrecusável para a construção de bots para o Telegram.
* [Scrapy](https://scrapy.org/) - Um framework rápido e poderoso de web crawling.
* [SQLAlchemy](https://www.sqlalchemy.org/) - Um kit de ferramentas SQL que fornece flexibilidade e poder a aplicações.

## Contribuições

Sinta-se absolutamente à vontade para contribuir.

## Licença

Esse projeto é distribuído sob a Licença MIT. Leia o arquivo [LICENSE](LICENSE) para ter mais detalhes.
