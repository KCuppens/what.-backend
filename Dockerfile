FROM python:3.11-bullseye

ARG BUILD_INFO=unknown
ENV BUILD_INFO=$BUILD_INFO

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE whatdot.settings.production

WORKDIR /app

COPY requirements/ requirements/
RUN pip install -r requirements/production.txt
RUN echo "deb http://apt.postgresql.org/pub/repos/apt bullseye-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt update && \
    apt install -y postgresql-client

COPY . .

# Statics are build directly in the image and served by whitenoise
RUN python manage.py collectstatic --noinput
EXPOSE 80
CMD gunicorn --bind=0.0.0.0:80 --forwarded-allow-ips="*" whatdot.wsgi:application
