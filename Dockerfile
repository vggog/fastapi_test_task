FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
