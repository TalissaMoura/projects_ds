# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10.2
FROM python:${PYTHON_VERSION}-slim as base
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /newsAppBase

COPY ./news/model/save ./news/model/save
COPY ./news/static ./news/static
COPY ./news/templates ./news/templates
COPY ./news/__init__.py ./news
COPY ./news/models.py ./news
COPY ./news/routes.py ./news
COPY ./news/routes.py ./news
COPY ./run.py ./


FROM python:${PYTHON_VERSION}-slim as server

WORKDIR /newsApp

COPY --from=base ./newsAppBase/news/model/save ./news/model/save
COPY --from=base ./newsAppBase/news/static ./news/static
COPY --from=base ./newsAppBase/news/templates ./news/templates
COPY --from=base ./newsAppBase/news/__init__.py ./news
COPY --from=base ./newsAppBase/news/models.py ./news
COPY --from=base ./newsAppBase/news/routes.py ./news
COPY --from=base ./newsAppBase/news/routes.py ./news
COPY --from=base ./newsAppBase/run.py ./

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install --upgrade pip && python -m pip install -r requirements.txt

RUN --mount=type=bind,source=downloads_nltk.py,target=downloads_nltk.py \ 
     python ./downloads_nltk.py

ENV FLASK_APP='news'
EXPOSE 5000
CMD flask run --host=0.0.0.0
