from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/img/<path:filename>')
def images(filename):
    return send_from_directory("static/img", filename)

if __name__ == '__main__':
  app.run(host='localhost', port=5000, debug=True)