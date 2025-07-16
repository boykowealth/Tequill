FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:1

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    xvfb \
    x11vnc \
    novnc \
    fluxbox \
    supervisor \
    net-tools \
    wget \
    curl \
    libgl1 \
    libegl1 \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libegl1-mesa \
    libosmesa6 \
    libglib2.0-0 \
    libxkbcommon0 \
    libx11-xcb1 \
    libxcb1 \
    libxcb-glx0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-xkb1 \
    libxkbcommon-x11-0 \
    libxcb-cursor0 \
    libnss3 \
    libasound2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
    markdown2 \
    PySide6

ENV QTWEBENGINE_DISABLE_SANDBOX=1
ENV QTWEBENGINE_DISABLE_GPU=1
ENV QT_QUICK_BACKEND=software
ENV QTWEBENGINE_CHROMIUM_FLAGS="--no-sandbox --disable-gpu --disable-software-rasterizer"

WORKDIR /app
COPY . /app/

RUN sed -i 's/\r$//' /app/start.sh
RUN chmod +x /app/start.sh

RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix

EXPOSE 8080

CMD ["./start.sh"]
