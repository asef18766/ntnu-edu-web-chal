from flask import Flask, request, abort, send_from_directory
from database.op import *
import database.flag
from os import getenv
app = Flask(__name__)
SUPER_SECRET_ADMIN_TOKEN = getenv("SUPER_SECRET_ADMIN_TOKEN", "48763")

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('frontend', path)

@app.route("/api/view")
def view_comment():
    '''
    view comment by query string
    if no query string provided, it will return id list
    '''
    cid = request.args.get("id")
    if cid is None:
        return query_ids()
    return query_comment(int(cid))

@app.route("/api/submit", methods=["POST"])
def submit_comment():
    '''
    store comment into database, and return its comment id
    '''
    add_comment(str(request.json["comment"]))
    return {"res":"success"}

@app.route("/api/edit", methods=["POST"])
def edit_comment():
    '''
    edit bad comment, only admin can do that
    '''
    print("user cookie: ", request.cookies.get("SUPER_SECRET_ADMIN_TOKEN"))
    if request.cookies.get("SUPER_SECRET_ADMIN_TOKEN") == SUPER_SECRET_ADMIN_TOKEN:
        cid = int(request.json["id"])
        ctx = str(request.json["ctx"])
        update_comment(cid, ctx)
        return {"res":"success"}
    abort(403)

if __name__ == "__main__":
    app.run("0.0.0.0", 48763)