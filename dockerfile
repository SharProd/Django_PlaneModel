FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD ./app /Django_PlaneModel
RUN pip install -r requirements.txt