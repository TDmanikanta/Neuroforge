from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Load your OpenAI API key
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
        # Calling GPT-3.5 (works with free API access)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are NeuroForge AI Z+ — an ultra-intelligent assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        return jsonify({"answer": answer.strip()})
    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
