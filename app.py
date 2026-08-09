from flask import Flask, jsonify
import config

app = Flask(__name__)

@app.get('/track/<code>')
def track(code):
    return jsonify(code=code, status='In transit', eta='2-3 days')

if __name__ == '__main__':
    app.run(debug=config.DEBUG)
