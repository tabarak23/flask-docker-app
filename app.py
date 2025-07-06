from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello():
    return "hajaat rawa is only allah nafa and nuksaan's only muktaar is allah"


@app.route('/healthz')
def healthz():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
