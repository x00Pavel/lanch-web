FROM python:3.10-slim-buster
EXPOSE 8080
ENV LUNCH_LOG_LEVEL=debug
ENV LUNCH_PORT=8080
ENV PORT=8080

WORKDIR /opt/app

COPY poetry.lock pyproject.toml /opt/app/
COPY lunch_web /opt/app/lunch_web
RUN pip install poetry
RUN poetry install --only main
CMD ["poetry", "run", "rest-api"]
