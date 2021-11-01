from functools import wraps
from flask import abort, request
from ms.helpers.jwt import jwtHelper


def auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        authorization = request.headers.get('Authorization')

        if not authorization:
            abort(403)

        valid = jwtHelper.check(authorization)

        if not valid:
            abort(403)

        payload = jwtHelper.decode(authorization)
        print(payload)

        return f(*args, **kwargs)
    return decorated_function
