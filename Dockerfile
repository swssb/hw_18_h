FROM python:3.9-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY config.py .
COPY constants.py .
COPY implemented.py .
COPY movies.db .
COPY setup_db.py .
COPY dao dao
COPY instance instance
COPY service service
COPY views views

CMD flask run -h 0.0.0.0 -p 80
#RUN python3 app.py
