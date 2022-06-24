from app.shared.exceptions import AppExceptionCase


class TaskException:
    class NotFound(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Task was not found
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)

    class WrongTaskData(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Wrong task data has been provided
            """
            status_code = 400
            AppExceptionCase.__init__(self, status_code, context)
