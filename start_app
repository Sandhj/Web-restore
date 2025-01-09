#!/bin/bash

# Path absolut ke virtual environment
VENV_PATH="/root/user/restore-web/myenv"
# Path absolut ke aplikasi
APP_PATH="/root/user/restore-web/app.py"
# Menjalankan aplikasi menggunakan Python dari virtual environment dan mengalihkan output
$VENV_PATH/bin/python $APP_PATH > /root/user/restore-web/app.log 2>&1 &

echo -e " - Silahkan Lakukan Restore Melalui Browser -"
echo -e "Akses : http://<IP_VPS>:5001"
