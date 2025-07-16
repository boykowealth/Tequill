FROM dorowu/ubuntu-desktop-lxde-vnc:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libgl1-mesa-glx \
    libegl1-mesa \
    libxcb1 \
    libx11-xcb1 \
    libxcb-glx0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libnss3 \
    libasound2 \
    libxshmfence1 \
    libxfixes3 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libfontconfig1 \
    libcups2 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libglu1-mesa \
    libglib2.0-0 \
    libqt5gui5 \
    libqt5core5a \
    libqt5dbus5 \
    libqt5network5 \
    libqt5widgets5 \
    qt5-gtk-platformtheme \
    fonts-dejavu-core \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir "PySide6==6.5.2" markdown2

ENV QT_X11_NO_MITSHM=1
ENV QT_SCALE_FACTOR=1
ENV QT_AUTO_SCREEN_SCALE_FACTOR=0
ENV QT_SCREEN_SCALE_FACTORS=1
ENV QT_QPA_PLATFORM=xcb

WORKDIR /app

COPY . /app

RUN chmod +x /app/start.sh

EXPOSE 80 5901

CMD ["/app/start.sh"]