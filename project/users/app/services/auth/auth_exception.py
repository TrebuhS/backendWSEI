from app.shared.exceptions import AppExceptionCase


class AuthException:
    class WrongToken(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Provided token is not correct.
            """
            status_code = 401
            AppExceptionCase.__init__(self, status_code, context)

    class IncorrectCredentials(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Incorrect email or password
            """
            status_code = 401
            AppExceptionCase.__init__(self, status_code, context)
