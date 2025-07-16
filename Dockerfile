FROM dorowu/ubuntu-desktop-lxde-vnc:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 python3-pip libgl1 libegl1 libxcb1 libx11-xcb1 libxcb-glx0 \
    libxcomposite1 libxdamage1 libxrandr2 libgbm1 libnss3 libasound2 \
    libxshmfence1 libxfixes3 libxkbcommon0 libxkbcommon-x11-0 \
    libatk1.0-0 libatk-bridge2.0-0 libfontconfig1 libcups2 \
    libsm6 libxrender1 libxext6 libglu1-mesa libglib2.0-0 \
    && pip3 install --no-cache-dir PySide6[webengine] markdown2

WORKDIR /app

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
