FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default to port 8000 if PORT isn't set
ENV PORT=8000

# EXPOSE is just documentation
EXPOSE $PORT

# Use the PORT environment variable
CMD gunicorn --bind 0.0.0.0:$PORT app:app