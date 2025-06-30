FROM python

EXPOSE 5000

COPY app.py /app/app.py

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD flask run --port=8003
