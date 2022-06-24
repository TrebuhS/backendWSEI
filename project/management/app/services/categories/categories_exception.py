from app.shared.exceptions import AppExceptionCase


class CategoryException:
    class NotFound(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Category was not found
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)

    class WrongCategoryData(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Wrong category data has been provided
            """
            status_code = 400
            AppExceptionCase.__init__(self, status_code, context)
