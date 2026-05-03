from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# ⚠️ 这里以后你要放你的API KEY
openai.api_key = "YOUR_API_KEY"

@app.route("/")
def home():
    return "AI Job Assistant Running"

@app.route("/optimize", methods=["POST"])
def optimize_resume():
    data = request.json
    text = data.get("text", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional resume optimizer."},
            {"role": "user", "content": f"Improve this resume bullet point: {text}"}
        ]
    )

    return jsonify({"result": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
