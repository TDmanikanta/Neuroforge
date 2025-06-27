#!/data/data/com.termux/files/usr/bin/bash

echo "🚀 Launching NeuroForge (Auto-Update + HTTPS Ready)"

cd ~/neuroforge || exit
echo "🔁 Pulling from GitHub..."
git pull origin main

echo "⚙️ Starting Flask server..."

cat <<EOF > app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🌐 NeuroForge is Live!</h1><p>Secure. Auto-Updating. Future-Ready.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
EOF

python app.py


