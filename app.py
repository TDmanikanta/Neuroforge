from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>NeuroForge 🌐</title></head>
        <body style='text-align: center; margin-top: 50px; font-family: sans-serif;'>
            <h1>🚀 NeuroForge 3000 A.D Z+ is Live!</h1>
            <p>Hosted from Termux with Ngrok public link 🔗</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
