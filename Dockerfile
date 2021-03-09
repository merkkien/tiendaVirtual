FROM python:3.8.4-alpine3.12
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
# Agrega librerias gcc para instalacion de dependencias
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
# Instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instala servidor WSGI para despliegue en produccion
RUN pip install waitress
COPY . /app
CMD ["python","waitress_server.py"]
