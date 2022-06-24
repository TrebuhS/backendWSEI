from app.shared.exceptions import AppExceptionCase


class NoteException:
    class NotFound(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Note was not found
            """
            status_code = 404
            AppExceptionCase.__init__(self, status_code, context)

    class WrongNoteData(AppExceptionCase):
        def __init__(self, context: dict = None):
            """
            Wrong note data has been provided
            """
            status_code = 400
            AppExceptionCase.__init__(self, status_code, context)
