FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV APP_PORT=8080
EXPOSE ${APP_PORT}

COPY . .

CMD ["python", "main.py"]
