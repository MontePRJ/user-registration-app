FROM python:3.10-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia tutto il contenuto della cartella app/ nel container
COPY app/ ./

# Installa i pacchetti Python richiesti
RUN pip install flask psycopg2-binary

# Comando per avviare l'app Flask
CMD ["python", "app.py"]