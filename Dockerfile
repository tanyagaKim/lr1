From python:latest
COPY . /app
WORKDIR /app
EXPOSE 8080
#ENV PORT=8080
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD ["python3", "app.py"]
#CMD gunicorn --workers=4 --bind 127.0.0.1:8080 app:app
