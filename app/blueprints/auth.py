from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return jsonify({"message": "Login Page"})

@auth.route('/logout')
def logout():
    return jsonify({"message": "Logout Page"})
