From python:latest
COPY . /app
WORKDIR /app
EXPOSE 8000
EXPOSE 80
#ENV PORT=8080
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
#CMD ["python3", "app.py"]
CMD gunicorn --workers=4 --bind 0.0.0.0:8080 app:app
