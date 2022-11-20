FROM python:3.10-slim-buster
EXPOSE 7788

WORKDIR /opt/app

COPY lunch_backend ./lunch_backend
COPY gunicorn.conf.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn.conf.py", "lunch_backend.app:create_app()"]
# WORKDIR /opt/app/lunch_backend
# CMD ["python", "-m", "flask" , "run", "--port", "7788", "--host", "0.0.0.0"]
