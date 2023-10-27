# Define a custom exception class
class personalized_exception(Exception):
    """
    Custom exception class for handling personalized exceptions.

    Args:
        human_readable_error (str): A human-readable error message.
        technical_error (str): A technical error message.
    """

    def __init__(self, human_readable_error, technical_error):
        """
        Initialize a personalized_exception object.

        Args and Attributes:
            human_readable_error (str): A human-readable error message.
            technical_error (str): A technical error message.

        Returns:
            personalized_exception: An instance of the personalized_exception class.
        """
        self.human_readable = human_readable_error
        self.technical_error = technical_error
        super().__init__(self.human_readable)

    def __str__(self):
        """
        Return a formatted string representation of the exception.

        Returns:
            str: A string representation of the exception including human-readable and technical error messages.
        """
        return f"\nError: {self.human_readable}\nError técnico: {self.technical_error}"


# Define a function for raising a personalized exception
def error_return(human_error, technical_error):
    """
    Raise a personalized_exception with the provided error messages.

    Args:
        human_error (str): A human-readable error message.
        technical_error (str): A technical error message.

    Raises:
        personalized_exception: A personalized exception with the specified error messages.
    """
    raise personalized_exception(human_error, technical_error)
    # raise is to send an error like a personalized exception
