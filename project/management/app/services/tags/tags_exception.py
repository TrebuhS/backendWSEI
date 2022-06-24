from app.shared.exceptions import AppExceptionCase


class TagException:
    class NotFound(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Tag was not found
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)

    class WrongTagData(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Wrong tag data has been provided
            """
            status_code = 400
            AppExceptionCase.__init__(self, status_code, context)
