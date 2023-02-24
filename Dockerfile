# syntax=docker/dockerfile:1

FROM registry.access.redhat.com/ubi8/ubi:8.1

WORKDIR /ibtech

RUN dnf -y update
RUN dnf -y install curl \
&& dnf -y install net-tools \
&& dnf -y install python38
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py", "--host=0.0.0.0"]
