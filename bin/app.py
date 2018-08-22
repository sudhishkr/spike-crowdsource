import sys
from flask import Flask, render_template, request, jsonify
from flask_restful import Api
from dbhelper import save_review, get_review

app = Flask(__name__)
api = Api(app)


@app.route("/")
@app.route("/crowdsource")
@app.route("/crowdsource/ping")
def home():
    out_map = {"status": "healthy", "app": "spike-scraper"}
    return jsonify(out_map)


@app.route("/crowdsource/review", methods=['GET', 'POST'])
def data_comment():
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        save_review(json_data=json_data)
        return jsonify({"status": "success"})
    elif request.method == 'GET':
        return jsonify(get_review())
    else:
        return jsonify({"status": "failed"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
