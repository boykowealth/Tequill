#!/bin/bash

Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1
sleep 2

python3 /app/app/main.py
