from flask import Flask, request, jsonify
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from utils import (
    start_page, linked_list
)

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

@app.route('/', methods=['get'])
def hello_world():
    return start_page.start_func()


# ===============================  user =================================
@app.route("/user_create", methods=["POST"])
def user_crete():
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data["email"],
        address=data["address"],
        phone=data["phone"],
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 200


@app.route("/user/descending_id", methods=["GET"])
def user_get_descending_id():
    users_query = User.query.all()  # return ascending order
    users_ll = linked_list.LinkedList()

    for user in users_query:
        users_ll.insert_beginning(
            linked_list.Node(
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "address": user.address,
                    "phone": user.phone,
                }
            )
        )

    return jsonify(users_ll.to_list()), 200


@app.route("/user/ascending_id", methods=["GET"])
def user_get_ascending_id():
    # same just push to end of the list  --> insert_to_end
    users_query = User.query.all()  # return ascending order
    users_ll = linked_list.LinkedList()

    for user in users_query:
        users_ll.insert_to_end(
            linked_list.Node(
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "address": user.address,
                    "phone": user.phone,
                }
            )
        )

    return jsonify(users_ll.to_list()), 200


@app.route("/user/<user_id>", methods=["GET"])
def user_get_by_id(user_id: int):
    users_query = User.query.all()
    users_ll = linked_list.LinkedList()

    for user in users_query:
        users_ll.insert_beginning(
            linked_list.Node(
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "address": user.address,
                    "phone": user.phone,
                }
            )
        )

    user = users_ll.get_user_by_id(user_id)
    return jsonify(user), 200


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
