FROM python:3.9.7
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]