<p>
Django test task for What. AG
</br>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
<img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</p>

# Features
1. Setup project
2. Login with backend without validation
3. Product model, API, prefilled migration
4. Add search to product API on name and description
5. Add alphabetical search to product API
6. Select product and save to cart by user and product

# Tech Stack

* python 3.11
* Django 4.X
* djangrestframework --> Using as our API

# Getting started
What-backend can be run locally and via docker.

The first thing to do is to clone the repository:

```bash
git clone https://github.com/KCuppens/what.-backend
cd 
```

## Install via docker

You need [docker](https://docs.docker.com/get-docker/) to be installed, then simply run:

```bash
docker compose build api
docker compose up api
```

## Manual local installation

### System requirements
- Python 3.8+
- virtualenv
- PostgreSQL 11+

### Instructions

1. Create a virtual environment. If you plan on working with many django projects, you should consider installing [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
2. Install the local dependencies in the virtual environment: `pip install -r requirements/local.txt`
3. Set up a new Postgres DB (we generally name it `whatbackend`)
4. Copy the `env.example` file to `.env`
6. Fill `DATABASE_URL` if your DB is not named `whatbackend` or not hosted on localhost
7. Run database tables creation `python manage.py migrate`
8. Create a superuser `python manage.py createsuperuser`
10. Run the dev server `python manage.py runserver`
11. Open your browser on `http://127.0.0.1:8000`

