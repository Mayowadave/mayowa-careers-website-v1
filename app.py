from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'location': 'Port Harcour, Nigeria',
    'title': 'Data analyst',
    'salary': 'N100,000'
  },
  {
    'id': 2,
    'location': 'Lagos, Nigeria',
    'title': 'Data scientist',
    'salary': 'N200,000'
  },
  {
    'id': 3,
    'location': 'Abuja, Nigeria',
    'title': 'Frontend engineer',
    'salary': 'N100,000'
  },
  {
    'id': 4,
    'location': 'Warri, Nigeria',
    'title': 'Backend engineer',

  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
