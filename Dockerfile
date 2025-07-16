FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libx11-xcb1 libglu1-mesa libglib2.0-0 libsm6 libxrender1 \
    libxext6 libxcomposite1 libxdamage1 libxrandr2 \
    libgbm1 libasound2 libnss3 libxshmfence1 libxfixes3 \
    libxkbcommon-x11-0 libx11-dev libxcb1 libxcb-glx0 \
    libxcb-keysyms1 libxcb-image0 libxcb-shm0 libxcb-icccm4 \
    libxcb-sync1 libxcb-xfixes0 libxcb-shape0 libxcb-randr0 \
    libxcb-render-util0 libxcb-xinerama0 libxcursor1 \
    libxi6 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    wget x11-xserver-utils && \
    rm -rf /var/lib/apt/lists/*

ENV QT_QPA_PLATFORM=xcb

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir PySide6[webengine] markdown2

CMD ["python", "main.py"]
