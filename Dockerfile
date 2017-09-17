FROM nyanim/nginx-unit
ENV UNIT_VERSION 0.1

WORKDIR /www

COPY . .

RUN apt update \
&& apt install -y python-pip nginx-light \
&& pip install -r requirements.txt \
&& python manage.py collectstatic --noinput \
&& cp ngx.conf /etc/nginx/sites-enabled/ \
&& service nginx restart \
&& service unitd start \
&& curl -X PUT -d @/www/unit.json --unix-socket /var/run/control.unit.sock http://localhost/ \
&& service unitd dumpconfig 

EXPOSE 8092

CMD service nginx restart \
&& service unitd stop \
&& rm /var/run/control.unit.sock \
&& service unitd start \
&& curl -X PUT -d @/www/unit.json --unix-socket /var/run/control.unit.sock http://localhost/ \
&& tail -F -n0 /etc/hosts \