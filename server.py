from flask import Flask, request, jsonify
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from utils import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    # force the blog_post to check appropriate user.id at user table
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
# dont forget >>> db.create_all()
now = datetime.now()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))  # for testing purpose
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# =================================  all routes ==========================

@app.route('/')
def hello_world():
    return start_func()


# ===============================  user =================================
@app.route("/user_create", methods=["POST"])
def user_crete():
    ...


@app.route("/user/descending_id", methods=["GET"])
def user_get_descending_id():
    ...


@app.route("/user/ascending_id", methods=["GET"])
def user_get_ascending_id():
    ...


@app.route("/user/<user_id>", methods=["GET"])
def user_get_by_id(user_id: int):
    ...


@app.route("/user/<user_id>", methods=["DELETE"])
def user_delete_by_id(user_id: int):
    ...


@app.route("/user/<user_id>", methods=["UPDATE"])
def user_update_by_id(user_id: int):
    ...


# =============================  blog ==================================
@app.route("/blog_post/<user_id>", methods=["POST"])
def blog_post_create(user_id: int):
    ...


@app.route("/blog_post/<user_id>", methods=["GET"])
def blog_post_get_all_by_user_id(user_id: int):
    ...


@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def blog_post_get_one_by_id(blog_post_id: int):
    ...


@app.route("/blog_post/<blog_post_id>", methods=["DELETE"])
def blog_post_delete_one_by_id(blog_post_id: int):
    ...


if __name__ == '__main__':
    app.run(debug=True)
