# SQLAlchemy-Primer 
An intro to using SQLAlchemy, Alembic and Postgres for implementing relational databases in python. 

## Table of contents
* [Built With](#built-with)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Authors](#authors)

## Built With
* [Python 3.8](https://www.python.org/) - The programming language used.
* [SQLAlchemy](https://www.sqlalchemy.org/) - The python SQL toolkit and Object Relational Mapper used. 
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) - The database migration tool used. 
* [PostgreSQL](https://www.postgresql.org/) - The relational database used.

## Prerequisites

What things you need to install the software and how to install them

* **python 3**

Linux:
```
sudo apt-get install python3.8
```

Windows:

Download from [python.org](https://www.python.org/downloads/windows/) 

Mac OS:
```
brew install python3
```

* **pip**

Linux and Mac OS:
```
pip install -U pip
```

Windows:
```
python -m pip install -U pip
```

## Installation

Clone this repository:
```
git clone https://github.com/SpencerOfwiti/SQLAlchemy-Primer.git
```

To set up virtual environment and install dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run alembic migrations:
```
alembic upgrade head
```

To run python scripts:
```
python3 main.py
```

To remove alembic migrations:
```
alembic downgrade base
```

## Authors

* **[Spencer Ofwiti](https://github.com/SpencerOfwiti)** - *Initial work* 
    
[![github follow](https://img.shields.io/github/followers/SpencerOfwiti?label=Follow_on_GitHub)](https://github.com/SpencerOfwiti)
[![twitter follow](https://img.shields.io/twitter/follow/SpencerOfwiti?style=social)](https://twitter.com/SpencerOfwiti)

