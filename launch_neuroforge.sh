#!/data/data/com.termux/files/usr/bin/bash
cd ~/neuroforge
pip install flask > /dev/null
export FLASK_APP=app
flask run --host=0.0.0.0 --port=8080
