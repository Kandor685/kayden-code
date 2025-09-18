from flask import Flask
app = Flask(__name__)
app.secret_key = 'a_secret_key'

import routes

if __name__ == '__main__':
    app.run(debug=True)