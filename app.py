from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello():
    return "making my hands dirty on cicd with docker and k8s"


@app.route('/healthz')
def healthz():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
