from flask import jsonify


def start_func():
    return jsonify({
        "message": "Data Structures For Python Developers (w/ Flask) - Course",
        "YouTube_link": "https://www.youtube.com/watch?v=74NW-84BqbA&list=WL&index=4&t=48s",
        "GitHub_link": "https://github.com/selikapro/FlaskDS",
        "organization": "freeCodeCamp.org",
        "text": "remember data struct, by using flask interfaces"
    }), 200
