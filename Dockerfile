# Imagen base 
FROM python:3.11-slim
 
# Directorio de trabajo dentro del contenedor
WORKDIR /app
 
# Copiar e instalar dependencias 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# Copiar el código fuente
COPY . .
 
# Puerto en uso
EXPOSE 5000
 
# Ejecutar aplicacion
CMD ["python", "app.py"]
