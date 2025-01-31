# Gunakan base image Python
FROM python:3.12.4

# Set working directory
WORKDIR /app

# Copy file ke dalam container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port flask
EXPOSE 5000 8080

# Jalankan server Flask
CMD mlflow server --host 0.0.0.0 --port 8080 & python server.py

