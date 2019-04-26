FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN apt-get update -y --fix-missing \
    && apt-get install -y --no-install-recommends \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    git \
    make \
    curl \
    xz-utils \
    file \
    patch \
    locales

ENV DEBIAN_FRONTEND noninteractive

RUN echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen ja_JP.UTF-8 \
    && dpkg-reconfigure locales \
    && /usr/sbin/update-locale LANG=ja_JP.UTF-8

ENV LC_ALL=ja_JP.UTF-8
ENV LANG=ja_JP.UTF8

RUN cd /tmp \
    && git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && ./bin/install-mecab-ipadic-neologd -n -u -y \
    && cd / \
    && rm -rf /tmp/mecab-ipadic-neologd \
    && ldconfig

ENV MECAB_DICDIR=/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd

WORKDIR /usr/src/source

ENV PIPENV_VENV_IN_PROJECT=1

COPY ./source/Pipfile ./

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --skip-lock --system
