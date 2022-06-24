from app.shared.exceptions import AppExceptionCase


class FriendsException:
    class NotFound(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            User was not found
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)

    class WrongUserData(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Wrong user data has been provided
            """
            status_code = 400
            AppExceptionCase.__init__(self, status_code, context)
