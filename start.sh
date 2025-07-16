#!/bin/bash

Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1
export QTWEBENGINE_DISABLE_SANDBOX=1
export QTWEBENGINE_CHROMIUM_FLAGS=--no-sandbox
sleep 2

python3 /app/app/main.py
