FROM python:2.7-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt \
&& python manage.py collectstatic --noinput
 

EXPOSE 8000

CMD cd /usr/src/app \
&& python manage.py runserver 8000