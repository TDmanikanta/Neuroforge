from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question")
    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are NeuroForge AI Assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"answer": answer.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port, debug=True)

