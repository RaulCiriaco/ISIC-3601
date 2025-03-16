# Usa una imagen base de Python
FROM python:3.10
# Define el directorio
WORKDIR /app
# Copia los archivos de la app al contenedor
COPY . /app
# Instala las dependencias
RUN pip install -r requirements.txt
# Expone el Puerto
EXPOSE 5000
# Define el comando para correr la app
CMD ["python","app.py"]
