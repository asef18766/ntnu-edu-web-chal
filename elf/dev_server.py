from flask import Flask, redirect
app = Flask(__name__)

flag = "flag{meow}"

@app.route('/hint')
def index():
    return redirect("https://youtu.be/iI9IygdZhvo?t=45")

if __name__ == '__main__':
    app.debug = True
    app.run()