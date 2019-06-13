FROM python:2.7-slim

WORKDIR /usr/src/app

COPY . .

RUN set -ex  \
&& apt update \
&& apt install -y build-essential python-dev\
&& pip install --no-cache-dir -i https://mirrors.ustc.edu.cn/pypi/web/simple -r requirements.txt \
&& python manage.py collectstatic --noinput \
&& apt remove build-essential -y \
&& apt autoremove -y \ 
&& mkdir /root/.netease-musicbox/ \
&& touch /root/.netease-musicbox/musicbox.log \
&& echo "#LWP-Cookies-2.0" > /root/.netease-musicbox/cookie
 
EXPOSE 80

CMD cd /usr/src/app \
&& exec gunicorn nem_parser.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 2
