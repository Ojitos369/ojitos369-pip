from .utils import print_line_center
from .errors import CatchErrors

class MYE(Exception):
    pass
ce = CatchErrors(name_project='')

class TryIt:
    def __init__(self, **kwargs):
        self.MYE = MYE
        self.ce = ce
        self.send_email = False

        for key, value in kwargs.items():
            setattr(self, key, value)

    def try_id(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self.MYE as e:
                error = self.ce.show_error(e)
                print_line_center(error)
                return e
            except Exception as e:
                error = self.ce.show_error(e, send_email=self.send_email)
                print_line_center(error)
                return e

        return wrapper


