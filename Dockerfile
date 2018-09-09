FROM python:2.7-alpine

WORKDIR /usr/src/app

COPY . .

RUN set -ex  \
&& echo "http://mirrors.ustc.edu.cn/alpine/v3.6/main/" > /etc/apk/repositories \
&& echo "http://mirrors.ustc.edu.cn/alpine/v3.6/community/" >> /etc/apk/repositories \
&& apk add --no-cache  --virtual .build-deps gcc autoconf g++ make libffi-dev openssl-dev python-dev\
&& pip install --no-cache-dir -i https://mirrors.ustc.edu.cn/pypi/web/simple -r requirements.txt \
&& python manage.py collectstatic --noinput \
&& apk del .build-deps \
&& mkdir /root/.netease-musicbox/ \
&& touch /root/.netease-musicbox/musicbox.log \
&& echo "#LWP-Cookies-2.0" > /root/.netease-musicbox/cookie
 
EXPOSE 8000

CMD cd /usr/src/app \
&& exec gunicorn nem_parser.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1