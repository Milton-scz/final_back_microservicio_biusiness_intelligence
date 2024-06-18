# Utilizar la imagen base oficial de Python para Flask
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Instalar Flask y las dependencias necesarias
RUN pip install --no-cache-dir Flask Flask-CORS requests plotly

# Exponer el puerto en el que corre tu aplicación Flask
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
