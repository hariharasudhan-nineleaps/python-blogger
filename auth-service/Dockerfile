############
#  BUILDER #
############

# pull official base image
FROM python:3.11.0-alpine as builder

# update packages
RUN apk update && apk add libc-dev musl-dev libffi-dev gcc

# set env for python and poetry
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# install poetry
RUN pip install poetry

# set workdir
WORKDIR /usr/app

# copy dependency manager related files
COPY pyproject.toml poetry.lock ./

# install deps
RUN poetry install --no-root

#########
# Final #
#########
FROM python:3.11.0-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/usr/app/.venv \
    PATH="/usr/app/.venv/bin:$PATH"

RUN addgroup -S app && adduser -S app -G app

COPY --from=builder --chown=app:app ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /usr/app

COPY --chown=app:app . .

ARG PORT=3001

ENV PORT ${PORT}

EXPOSE ${PORT}

USER app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3001"]



