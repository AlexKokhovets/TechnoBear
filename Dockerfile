FROM alpine:3.5
RUN apk add --update python py-pip
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
CMD python manage.py runserver
