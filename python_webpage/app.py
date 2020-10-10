from flask import Flask , send_file
app = Flask(__name__)


@app.route('/')
def get_index():
    return send_file("src/index.html")


@app.route('/jquery-3.5.1.min.js')

def get_jquery():
    return send_file("src/jquery-3.5.1.min.js")


@app.route('/index.js')
def get_indexjs():
    return send_file("src/index.js")


@app.route('/getStatus')
def get_getStatus():
    return {"pos" : 2}

    # return "Hello World!"




if __name__ == '__main__':
    app.run()