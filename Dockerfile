FROM python:3.9-slim
LABEL maintainer="samad.anjali.1402@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /trim_url
WORKDIR /trim_url
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
COPY ./ /trim_url/
RUN pip install -r requirements.txt

# Django service
EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000