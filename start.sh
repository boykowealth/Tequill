#!/bin/bash

# Wait for X server to be available
echo "Waiting for X server..."
while ! xset q &>/dev/null; do
    sleep 1
done

echo "X server is ready"

# Set environment variables
export QT_X11_NO_MITSHM=1
export QT_QPA_PLATFORM=xcb
export QT_SCALE_FACTOR=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0

# Start your Python GUI application
cd /app
echo "Starting GUI application..."
python3 app/main.py