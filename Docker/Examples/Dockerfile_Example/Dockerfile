FROM python:3.9-slim
WORKDIR /example
COPY . /example
RUN apt-get update
RUN apt -y install build-essential
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]