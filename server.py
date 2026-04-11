from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/api/convert')
def convert():
    value = float(request.args.get("kg"))
    metrikYangDiberikan = str(request.args.get("metric"))
    hasil = 0
    if metrikYangDiberikan == "kg":
        hasil = value * 2.2
    else:
        hasil = value * 0.45
    return jsonify({"lbs": hasil})

if __name__ == '__main__':
    app.run()
