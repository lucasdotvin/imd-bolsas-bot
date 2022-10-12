<h1 align="center">IMD Bolsas Bot</h1>

<p align="center">
<a href="https://www.python.org/"><img alt="Made With Python Badge" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a> <a href="blob/master/LICENSE"><img alt="MIT License Badge" src="http://img.shields.io/badge/license-MIT-blue.svg?style=flat"></a> <a href="https://github.styleci.io/repos/239562591?branch=develop"><img src="https://github.styleci.io/repos/239562591/shield?branch=develop" alt="StyleCI"></a>
</p>

Bot de alimentação do canal [IMD Bolsas](https://t.me/imdbolsas) no Telegram e do perfil [IMD Bolsas](https://twitter.com/imdbolsas) no Twitter. Seu objetivo é alertar estudantes do instituto sobre bolsas e vagas de estágio.

## Iniciando

Essas instruções lhe darão uma cópia do projeto e um caminho para executá-lo localmente para fins de desenvolvimento e teste. Vide as notas de deployment para entender como fazer deploy.

### Pré-Requisitos

Você precisará basicamente do Python 3.8 ou superior instalado na sua máquina.

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

Para rodar, execute o arquivo `main.py`:

```bash
python main.py
```

## Construído Com

* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Uma moderna e simples biblioteca de templating para Python.
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot/) - Um wrapper irrecusável para a construção de bots para o Telegram.
* [SQLAlchemy](https://www.sqlalchemy.org/) - Um kit de ferramentas SQL que fornece flexibilidade e poder a aplicações.

## Contribuições

Sinta-se absolutamente à vontade para contribuir.

## Licença

Esse projeto é distribuído sob a Licença MIT. Leia o arquivo [LICENSE](LICENSE) para ter mais detalhes.
