CMD python manage.py runserver
FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./manage.py runserver" ]
