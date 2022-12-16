FROM python:3.10-slim-buster
EXPOSE 8080
ENV LUNCH_LOG_LEVEL=debug
ENV PORT=8080

WORKDIR /opt/app

COPY poetry.lock pyproject.toml /opt/app/
COPY lunch_web /opt/app/lunch_web
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main
CMD ["gunicorn", "--config", "./lunch_web/wsgi/gunicorn_conf.py", "lunch_web.wsgi.app:create_app()"]
