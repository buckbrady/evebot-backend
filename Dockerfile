FROM python:3.11-slim-buster

ARG ENV=development
ENV ENVIRONMENT=$ENV
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential curl \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ENV POETRY_HOME /opt/poetry

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH $POETRY_HOME/bin:$PATH

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$ENVIRONMENT" == production && echo "--no-dev") --no-interaction --no-ansi

COPY ./evebot /app/

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]

