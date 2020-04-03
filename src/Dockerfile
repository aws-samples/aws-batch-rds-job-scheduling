# INSTALL PYTHON IMAGE
FROM python:3.6

# INSTALL TOOLS
RUN apt-get update \
    && apt-get -y install unzip \
    && apt-get -y install libaio-dev \
    && mkdir -p /opt/data/api

ADD ./requirements.txt /opt/data
ADD ./runjob.py /opt/data/runjob.py

WORKDIR /opt/data

RUN pip install -r /opt/data/requirements.txt

CMD ["python3","/opt/data/runjob.py"]
