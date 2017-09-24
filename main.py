from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form method="post">
            <label>Rotate by:
                <input name="rot" type="text" value="0"/>
            </label>
            <br>
            <input type="textarea" name="text"/>
            <br>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])

    encrypted = rotate_string(text,rot)
    return form + '<h1>' + encrypted + '</h1>'

@app.route("/")
def index():
    return form

app.run()
