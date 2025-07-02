# 1. Usa imagem oficial do Python
FROM python:3.11-slim

# 2. Define o diretório de trabalho no container
WORKDIR /app

# 3. Copia o arquivo de dependências e instala os pacotes
COPY requirements.txt .
RUN apt-get update && apt-get install -y netcat-openbsd && \
    pip install --no-cache-dir -r requirements.txt

# 4. Copia todos os arquivos do projeto
COPY . .

# 5. Dá permissão de execução ao script
RUN chmod +x entrypoint.sh

# 6. Define variáveis de ambiente básicas para o Flask
ENV FLASK_APP="app:create_app()"
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# 7. Expõe a porta usada pela aplicação
EXPOSE 5000

COPY entrypoint.sh .

# 8. Comando para iniciar o servidor Flask
ENTRYPOINT ["./entrypoint.sh"]
