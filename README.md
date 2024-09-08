# Estrutura basica de um projeto em flask utilizando clean architecture


## Tecnologias utilizadas 💻
<ul>
  <li>Python</li>
  <li>Flask-Sqlalchemy</li>
  <li>Pydantic</li>
  <li>Flask-Migrate</li>
  <li>Swagger</li>
  <li>SQLite></li>
</ul>

## Para criar um ambiente virtual digite:
```
python -m venv venv
```

## Para acessar o ambiente virtual digite :
### No Windows
```
.\venv\Scripts\activate
```
### No Linux
```
python3 source/bin/activate
```

## Para instalar as depencias vá até a pasta do projeto e digite :
```
pip install -r requirements.txt
```

## Depois de instalado as dependencias , caso fala uma alteração no model digite:
```
flask db init
```
```
flask db migrate -m "Initial migration"
```
```
flask db upgrade
```

## Verificar o status da migração
```
flask db status
```

## Reverter a migração
```
flask db downgrade
```

## Para rodar o app digite :
```
flask run
```

## Para acessar o swagger digite no browser :
```
http://127.0.0.1:5000/swagger
```
