#!/bin/bash

# Path absolut ke virtual environment
VENV_PATH="/root/user/w/myenv"

# Path absolut ke aplikasi
APP_PATH="/root/myproject/app.py"

# Menjalankan aplikasi menggunakan Python dari virtual environment dan mengalihkan output
$VENV_PATH/bin/python $APP_PATH > /root/myproject/app.log 2>&1 &
