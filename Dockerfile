FROM python:3.12.3-alpine
WORKDIR /code
COPY . /code
RUN pip install nltk
CMD [ "python","CLOUD.py"]