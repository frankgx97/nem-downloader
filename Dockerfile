FROM python:2.7-slim

WORKDIR /usr/src/app

COPY . .

RUN set -ex  \
&& apt update \
&& apt install -y build-essential python-dev\
&& pip install --no-cache-dir -r requirements.txt \
&& python manage.py collectstatic --noinput \
&& apt remove build-essential -y \
&& apt autoremove -y \ 
&& mkdir /root/.netease-musicbox/ \
&& touch /root/.netease-musicbox/musicbox.log \
&& mkdir /usr/src/app/.netease-musicbox/ \
&& touch /usr/src/app/.netease-musicbox/musicbox.log \
&& echo "#LWP-Cookies-2.0" > /root/.netease-musicbox/cookie \
&& echo "#LWP-Cookies-2.0" > /usr/src/app/.netease-musicbox/cookie
 
EXPOSE 80

CMD cd /usr/src/app \
&& exec gunicorn nem_parser.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 2
