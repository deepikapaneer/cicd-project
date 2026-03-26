from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from CI/CD!"})

@app.route('/users')
def users():
    return jsonify({"message": "CI/CD Project - users page"})

@app.route('/about')
def about():
    return jsonify({
        "name": "Deepika Paneer Selvam",
        "role": "DevOps Engineer",
        "skills": ["Linux", "Docker", "AWS", "Kubernetes"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)