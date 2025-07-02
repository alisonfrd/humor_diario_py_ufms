#!/bin/bash

# Verifica se as variáveis estão definidas
: "${DB_HOST:?DB_HOST não definida}"
: "${DB_PORT:?DB_PORT não definida}"

echo "Aguardando o MySQL em $DB_HOST:$DB_PORT..."

# Aguarda o banco de dados iniciar
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  echo "MySQL ainda não está pronto..."
  sleep 2
done

echo "MySQL está pronto! Aplicando migrações..."

flask db upgrade

echo "Iniciando o servidor Flask..."
exec flask run
