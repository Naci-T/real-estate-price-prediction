FROM python:3.10

WORKDIR /test-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

#create a copy of all the folders you want to make an image