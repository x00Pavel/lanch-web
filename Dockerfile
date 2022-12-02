FROM python:3.10-slim-buster
EXPOSE 8080
ENV LUNCH_LOG_LEVEL=debug
ENV LUNCH_PORT=8080
ENV PORT=8080

WORKDIR /opt/app

COPY lunch_backend ./lunch_backend
COPY gunicorn.conf.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["gunicorn", "-c", "gunicorn.conf.py", "lunch_backend.app:create_app()"]
