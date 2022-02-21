FROM python:3.8-buster

COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /usr/src/app
#COPY . .

ADD . .
RUN pip install .

ENV FLASK_APP=
ENV FLASK_DEBUG=1
CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]