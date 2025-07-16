FROM dorowu/ubuntu-desktop-lxde-vnc

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    && pip3 install PySide6[webengine] markdown2

CMD ["sh", "-c", "python3 /app/main.py"]
