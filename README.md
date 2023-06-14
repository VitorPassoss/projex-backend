## Projex

## Tecnologias utilizadas
- Django 
- Python 
- Django-Rest-Framework
- Docker
- PostgreSQL
- Simple-JWT


## Metodologias e Padrões
- PEP 8 Guideline para o código Python.


## Instalação

> Antes de começar no windows, você deve ter o [WSL2](https://docs.microsoft.com/pt-br/windows/wsl/install-win10) instalado e configurado em seu computador.
> E também deve habilitar o [Docker Desktop](https://docs.docker.com/docker-for-windows/wsl/) para o WSL2.

### Requisitos

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/) (Linux)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows e Mac)
- [Docker Compose](https://docs.docker.com/compose/) (Linux, Windows e Mac)

### Linux

```bash
# Clone o repositório
git clone git@github.com:VitorPassoss/projex-backend.git

# Entre na pasta do projeto
cd projex-backend

# Suba os containers
docker-compose up -d --build

# Execute as migrações
docker exec -it app python manage.py migrate

# Crie um super usuário
docker exec -it app python manage.py createsuperuser
```


### Windows (PowerShell)

```powershell
# Clone o repositório
git clone git@github.com:VitorPassoss/projex-backend.git

# Entre na pasta do projeto
cd projex-backend

# Suba os containers
docker-compose up -d --build

# Execute as migrações
docker exec -it app python manage.py migrate

# Crie um super usuário
docker exec -it app python manage.py createsuperuser
```

