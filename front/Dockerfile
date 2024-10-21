FROM node:21-alpine AS builder

WORKDIR /app

# Copiar arquivos de dependências
COPY package.json package-lock.json ./

# Instalar dependências
RUN npm install

# Copiar o restante dos arquivos
COPY . .

# Construir a aplicação
RUN npm run build

FROM nginx:alpine

# Copiar arquivos construídos para o Nginx
COPY --from=builder /app/dist/ /usr/share/nginx/html

# Adicionar a configuração do Nginx para ouvir na porta 5173
RUN echo 'server { \
    listen 5173; \
    listen [::]:5173; \
    server_name localhost; \
    location / { \
        root /usr/share/nginx/html; \
        index index.html index.htm; \
    } \
    error_page 500 502 503 504 /50x.html; \
    location = /50x.html { \
        root /usr/share/nginx/html; \
    } \
}' > /etc/nginx/conf.d/5173.conf

EXPOSE 80 5173

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
