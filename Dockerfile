FROM python:3
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8001/udp
EXPOSE 8001/tcp
CMD [ "python", "manage.py runserver 0.0.0.0:8001" ]
