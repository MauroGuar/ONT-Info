import sys
class personalized_exception(Exception):
    def __init__(self, human_readable_error, technical_error):
        self.human_readable = human_readable_error
        self.technical_error = technical_error
        super().__init__(self.human_readable)

    def __str__(self):
        return f"\nError: {self.human_readable}\nError tecnico: {self.technical_error}"
def error_return(human_error, technical_error):
    raise personalized_exception(human_error,technical_error)