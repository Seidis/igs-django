# Desafio IGS - Django

Esse projeto foi desenvolvido para o desafio proposto pela IGS, como parte do seu processo de admissão. O desafio era sobre uma API em Django para listar, criar, deletar e atualizar os colaboradores e seus departamentos, além de também ser necessário uma pagina para exibir esses dados.

## Instalação

Para poder executar o código localmente, é preciso seguir esses passos antes:

1. Crie um ambiente virtual: `python3 -m venv venv`
2. Ative o ambiente virtual: `source venv/bin/activate`
3. Instale as dependências do backend: `pip install -r requirements.txt`
4. Crie o banco: `python manage.py migrate`

## Uso

Após os passos da [INSTALACAO](#instalação), você está pronto para executar os códigos a seguir:

1. Crie um super usuário: `python manage.py createsuperuser`
   - Siga os passos que aparecem no terminal.
2. (Opcional) Popule o banco de dados: `python populate_db.py`
   - Caso queira popular o banco automáticamente, basta rodar esse script.
3. Execute o código do Django: `python manage.py runserver`

Na página principal é possível filtrar e escolher qual a coluna ordenará a tabela.
Para ir ao painel administrativo do Django, basta clicar no botão no navbar.
