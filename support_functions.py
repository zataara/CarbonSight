from flask import Flask, session
from werkzeug.exceptions import Unauthorized


def checkUserId(username):

    if 'username' not in session or username != session['username']:
        raise Unauthorized()