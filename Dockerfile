FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install nginx
RUN apt-get update && apt-get install nginx -y --no-install-recommends

COPY nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log



RUN mkdir -p /opt/app && \
    chown -R www-data:www-data /opt/app

WORKDIR /opt/app


COPY requirements.txt entrypoint.sh /opt/app/

RUN pip install --upgrade pip && \
	pip install -r requirements.txt


COPY . .

RUN chmod +x entrypoint.sh


# start server
EXPOSE 8020

CMD ["/bin/bash", "-c" "gunicorn --config gunicorn-cfg.py core.asgi:application -k uvicorn.workers.UvicornWorker; nginx -g 'daemon on;' &;"]

# ENTRYPOINT ["/opt/app/entrypoint.sh"]

# gunicorn core.wsgi --user www-data --bind 0.0.0.0:8050

# gunicorn --config gunicorn-cfg.py core.asgi:application -k uvicorn.workers.UvicornWorker

# CMD ["gunicorn", "--config", "--config gunicorn-cfg.py", "core.wsgi"]

# CMD ['bash', '-c', 'gunicorn core.wsgi --user www-data --bind 127.0.0.1:8010 --workers 1 ; nginx -g "daemon on;" & ;']
