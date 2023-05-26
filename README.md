# Diplomová práce - Webová aplikace pro správu veterinární ordinace

Webová aplikace pro správu veterinární ordinace, která vznikla v rámci diplomové práce na ÚAI FSI VUT. 


## Systémové požadavky:

 - Python 3.11
 - PostgreSQL

## Ubuntu 22.04
Pro spuštění aplikace na Ubuntu 22.04 je potřeba následovat tyto kroky:

**Instalace Pythonu 3.11 a venv:**

Přidání PPA:

    sudo add-apt-repository ppa:deadsnakes/ppa

Instalace Pythonu 3.11:

    sudo apt install python3.11

Instalace venv:

    sudo apt-get install python3.11-venv

**Naklonování repozitáře a instalace závislostí:**

Naklonování repozitáře:

    git clone https://github.com/jfoltan/VetSimplify.git

Vytvoření virtuálního prostředí:

    python3.11 -m venv venv

Instalace systémových závislostí pro projekt:

    sudo apt-get update
    sudo apt-get install libcairo2-dev pkg-config python3-dev


Aktivace virtuálního prostředí:

    source venv/bin/activate

Instalace závislostí:

    cd VetSimplify
    
    pip  install  -r  requirements.txt


**Instalace PostgreSQL:**

    sudo apt install postgresql postgresql-contrib

Kontrola stavu PostgreSQL:

    service postgresql status
Na výstupu by měl být zobrazen active stav


**Vytvoření databáze a připojení:**
Spuštění příkazové řádky pro Postgres

    sudo -i -u postgres
    
    psql
Vytvoření databáze:

    create database database_name;

V settings.py je potřeba nastavit připojení k databázi:

    DATABASES = {
	    "default": {
		    "ENGINE": "django.db.backends.postgresql",
		    "NAME": "database_name",
		    "USER": "postgres",
		    "PASSWORD": "postgres",
		    "HOST": "localhost",
		    "PORT": "5432",
		}
	}

Aplikování migrací: 

    python  manage.py  migrate


**Spuštění serveru:**
Nyní je možné spustit server pomocí:

    python manage.py runserver


## Windows 10/11
**Instalace Pythonu 3.11 a Git:**
Instalace Pythonu a Git pomocí winget:

    winget install Python.Python.3.11
    winget install Git.Git
Po zadání příkazu je nutné restartovat terminál.

**Naklonování repozitáře a instalace závislostí:**

Naklonování repozitáře:

    git clone https://github.com/jfoltan/VetSimplify.git

Vytvoření virtuálního prostředí:

    python -m venv venv

Aktivace virtuálního prostředí:

    venv\Scripts\activate

Instalace závislostí:

    cd VetSimplify
    
    pip  install  -r  requirements.txt

**Instalace PostgreSQL:**

    winget install PostgreSQL.PostgreSQL

Přidat cestu k adresáři bin PostgreSQL (výchozí: C:/ProgramFiles/PostgreSQL/bin)

Spustit SQL shell (výchozí uživatel: postgres, heslo: postgres):

    psql -U postgres

Vytvoření databáze:

    create database database_name;

V settings.py je potřeba nastavit připojení k databázi:

    DATABASES = {
	    "default": {
		    "ENGINE": "django.db.backends.postgresql",
		    "NAME": "database_name",
		    "USER": "postgres",
		    "PASSWORD": "postgres",
		    "HOST": "localhost",
		    "PORT": "5432",
		}
	}

Aplikování migrací: 

    python  manage.py  migrate


**Spuštění serveru:**
Nyní je možné spustit server pomocí:

    python manage.py runserver
    

