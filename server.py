from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


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


app.run(debug=True)

