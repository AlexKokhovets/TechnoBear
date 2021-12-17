FROM python:3
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000/udp
EXPOSE 8000/tcp
CMD [ "python", "manage.py runserver" ]
