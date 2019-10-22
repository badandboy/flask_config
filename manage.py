#coding=utf-8
from app import create_app
from flask_cors import CORS
from config import serverPort


app = create_app()
app.secret_key = '\x1d\x18R\xe5x\x04\xeeN\x1cD\xba\x7f\xf8*\xba\x81\xf7\xcc\xbc\xe5\x0eC\x99\xa8'
CORS(app, resources=r'/*')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=serverPort)
    # manager.run()