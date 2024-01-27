FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app






# FROM python:3.11-slim

# # Set a default value for the PORT build argument
# ARG PORT=8080

# COPY . /app
# WORKDIR /app

# RUN pip install -r requirements.txt

# EXPOSE $PORT
# CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
