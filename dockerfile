FROM python:3.10-slim-bullseye

WORKDIR /usr/connect

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --without dev

COPY src/ /usr/connect/src/

RUN find /usr/connect/src -type d -name '__pycache__' -exec rm -r {} + && \
    find /usr/connect/src -type f \( -name '*.pyc' -o -name '*.pyo' \) -exec rm -f {} +

ENV PYTHONPATH=/usr/connect/src
WORKDIR /usr/connect/src

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

