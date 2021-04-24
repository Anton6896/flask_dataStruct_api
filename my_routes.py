from server import app


@app.route("/user_create", methods=["POST"])
def user_crete():
    ...


@app.route("/user/descending_id", methods=["GET"])
def user_get_descending_id():
    ...


@app.route("/user/ascending_id", methods=["GET"])
def user_get_ascending_id():
    ...