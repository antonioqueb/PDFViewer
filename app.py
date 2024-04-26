from flask import Flask, send_from_directory, Response

app = Flask(__name__)

def send_pdf(filename):
    return send_from_directory('static', filename, mimetype='application/pdf')

@app.route('/1')
def pdf1():
    return send_pdf('documento1.pdf')

@app.route('/2')
def pdf2():
    return send_pdf('documento2.pdf')

@app.route('/3')
def pdf3():
    return send_pdf('documento3.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
