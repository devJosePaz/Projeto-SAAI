# Imagem base com Python
FROM python:3.11-slim

# Define a pasta de trabalho no container
WORKDIR /app

# Copia o arquivo de dependências da raiz para o container
COPY ../requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo do backend para dentro do container
COPY . .

# Expõe a porta do FastAPI
EXPOSE 8000

# Comando para rodar o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
