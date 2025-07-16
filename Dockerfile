FROM dorowu/ubuntu-desktop-lxde-vnc:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install --no-cache-dir "PySide6[webengine]==6.5.2" markdown2

WORKDIR /app

COPY . /app

RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
