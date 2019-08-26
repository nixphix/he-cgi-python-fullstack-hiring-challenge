FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# create a group and user for running worker process
RUN addgroup -S appserver \
  && adduser -S -G appserver appserver \
  && apk update \
  # psycopg2 dependencies
  && apk add gcc musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi \
  # install proxy server
  && apk add nginx \
  # create dir for nginx pid
  && mkdir -p /run/nginx \
  # create client body tmp dir
  && mkdir -p /tmp/nginx/client_body \
  # clean up nginx default static files
  && rm -rf /var/lib/nginx/html/* \
  # grant access to static files
  && chown -R appserver /var/lib/nginx/html/ \
  # create app directory
  && mkdir /app

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/dev.txt \
    && rm -rf /requirements

COPY ./compose/dev/django/entrypoint.sh /entrypoint.sh
COPY ./compose/dev/django/start.sh /start.sh

COPY ./compose/dev/django/nginx.conf /etc/nginx
COPY ./compose/dev/django/games.conf /etc/nginx/conf.d

RUN chown -R appserver /app

RUN sed -i 's/\r//' /*.sh \
    && chmod +x /*.sh \
    && chown appserver /*.sh

WORKDIR /app

EXPOSE 8080
EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
