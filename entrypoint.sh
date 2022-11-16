#!/bin/bash

service nginx start &
#gunicorn --config gunicorn-cfg.py core.wsgi
gunicorn core.wsgi --user www-data --bind 127.0.0.1:8010 --workers 2 & \
# nginx -g "daemon on;" &
#echo whoami

# update-rc.d -f nginx defaults

# systemctl start nginx.service
# systemctl enable nginx
