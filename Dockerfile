FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
ENV API_KEY="a54f5e809d19b466ea9473efa696d098"
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]

