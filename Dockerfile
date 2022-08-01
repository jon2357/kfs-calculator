# 
FROM python:3.10

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT}