FROM python:3.12
COPY . /workdir
WORKDIR /workdir
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut==2.5 \
    pylint \
    pylint-fail-under \
    pytest-cov \
    pytest
RUN pip install \
    git+https://github.com/IslasGECI/geci_cli.git \
    giotto-tda \
    matplotlib \
    pandas

CMD make
