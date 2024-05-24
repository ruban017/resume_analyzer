from flask import Flask, render_template, request, jsonify,send_file
from flask_cors import CORS, cross_origin
from score import analyze_resume


app = Flask(__name__)

cors = CORS(app)
# @app.route("/")
# def hello():
#     return "Hello there. Hope you are doing good!!"


@app.route("/", methods=["POST"])
def gettingval():
    print("This service is running")
    job_dec = request.form.get('desc')
    resume_file = request.files.get('resume')

    sc = analyze_resume(resume_file, job_dec)
    # return jsonify({"score": sc})
    return send_file('doughnut_chart.png', mimetype='image/png')

# if __name__ == "__main__":
#     app.run(debug=True, port=8080)
