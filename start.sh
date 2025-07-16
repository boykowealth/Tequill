#!/bin/bash

# 1. Start a 1920×1080 virtual display
Xvfb :1 -screen 0 1920x1080x24 &
export DISPLAY=:1

# 2. Qt soft-rendering flags
export QTWEBENGINE_DISABLE_SANDBOX=1
export QTWEBENGINE_DISABLE_GPU=1
export QT_QUICK_BACKEND=software
export QTWEBENGINE_CHROMIUM_FLAGS="--no-sandbox --disable-gpu --disable-software-rasterizer"
export NO_AT_BRIDGE=1

sleep 2

# 3. Serve on port 5900 so noVNC proxy can reach it
x11vnc -display :1 -rfbport 5900 -nopw -forever -shared &

# 4. Launch noVNC on HTTP port 8080
/opt/novnc/utils/novnc_proxy \
  --vnc localhost:5900 \
  --listen 8080 \
  --web /opt/novnc &

# 5. Start your Qt application
python3 /app/app/main.py