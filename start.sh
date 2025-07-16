#!/bin/bash

Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1

export QTWEBENGINE_DISABLE_SANDBOX=1
export QTWEBENGINE_DISABLE_GPU=1
export QT_QUICK_BACKEND=software
export QTWEBENGINE_CHROMIUM_FLAGS="--no-sandbox --disable-gpu --disable-software-rasterizer"
export NO_AT_BRIDGE=1

sleep 2

x11vnc -display :1 -nopw -forever -shared &

/opt/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 8080 &

python3 /app/app/main.py
