from flask import Flask

from model import calc, scrape

app = Flask(__name__)

@app.route("/")
def test():
    return '1'

if __name__ == '__main__':
    app.run()