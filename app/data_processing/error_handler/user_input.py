# Import necessary modules and functions
import sys
from app.data_processing.error_handler.errors import error_return


# Define a function for validating IPv4 addresses
def ipv4_validation(ip):
    """
    Validate an IPv4 address to ensure it is in a correct format.

    Args:
        ip (str): The IPv4 address to validate.

    Returns:
        str: The validated IPv4 address if it passes validation.
        bool: True if validation is successful, else returns an error using the 'error_return' function.
    """
    partes = ip.split(".")
    if len(partes) != 4:
        # Check if the IP is composed of four parts separated by periods ('.').
        error_return(
            "La ip introducida no esta compuesta por 4 partes divididas por un '.'",
            "The introduced ip is not divided by 4 '.' characters",
        )

    try:
        for parte in partes:
            num = int(parte)
            if not 0 <= num <= 255:
                # Check if each part of the IP is within the valid range [0-255].
                error_return(
                    "Alguna de las partes de la ip introducida cae fuera del rango numerico requerido: [0-255]",
                    "At least one of the introduced 'octates' is out of the 8 bit unsigned number range (0 to 255)",
                )
            if len(parte) > 1 and parte[0] == "0":
                # Ensure there are no leading zeros in the IP, which is an incorrect format.
                error_return(
                    "La ip introducida contiene 0s a la izquierda o de relleno, formato no permitido.",
                    "The ip contains zero padding/leading zeroes (like the zero in 013), incorrect format",
                )
            return ip
    except ValueError:
        # Catch ValueError indicating that the IP contains non-integer characters or syntax errors.
        error_return(
            "La ip introducida contiene caracteres que no son enteros, verifique por errores de sintaxis",
            "parseint failed",
        )

    return True


# Define a function for validating serial numbers
def sn_validation(
        introduced_serial,
        introduced_length,
        introduced_base,
        introduced_dictionary={"Ñ": "N"},
):
    """
    Validate a serial number (SN) to ensure it satisfies length, base, and character conditions.

    Args:
        introduced_serial (str): The introduced serial number to validate.
        introduced_length (int): The required length of the SN.
        introduced_base (int): The base in which the SN should be interpreted (e.g., 16 for hexadecimal).
        introduced_dictionary (dict): A translation dictionary for characters (default {'Ñ': 'N'}).

    Returns:
        str: The validated serial number if it passes validation.
        bool: True if validation is successful, else returns an error using the 'error_return' function.
    """
    serial = introduced_serial.upper().translate(
        introduced_dictionary)  # serial to uppercase and convert based on the dictionary
    try:
        # Verify if the serial has the exact introduced length.
        if len(serial) != introduced_length:
            error_return(
                f"El sn introducido no satisface la longitud requerida: {introduced_length} caracteres",
                f"The introduced serial number does not satisfy the exact length condition of {introduced_length}",
            )

        # Try to convert the number to the introduced base.
        int(serial, introduced_base)
        return serial
    except ValueError:
        # Catch ValueError indicating that some characters in the SN do not satisfy the base condition.
        error_return(
            f"Alguno de los caracteres introducidos como parte del sn no satisfacen la base necesaria: base {introduced_base}",
            f"The serial number does not satisfy the base per character (Value error when parsing), in this case, base: {introduced_base}",
        )


# Define a function to validate an IP address and a serial number and return the results.
def ip_sn_validator(ip_introduced, sn_introduced, sn_length, sn_base, sn_dictionary):
    """
    Validate an IP address and a serial number and return the validation results.

    Args:
        ip_introduced (str): The introduced IP address.
        sn_introduced (str): The introduced serial number.
        sn_length (int): The required length of the serial number.
        sn_base (int): The base in which the serial number should be interpreted (e.g., 16 for hexadecimal).
        sn_dictionary (dict): A translation dictionary for characters.

    Returns:
        str: The validated IP address and serial number or True if both pass validation.
    """
    ip_return = ipv4_validation(ip_introduced)
    sn_return = sn_validation(sn_introduced, sn_length, sn_base, sn_dictionary)
    return ip_return, sn_return


# Define a function to get input from command line arguments and perform validation
def get_input():
    """
    Get input from command line arguments and perform IP and serial number validation.

    This function expects two command line arguments: an IP address and a serial number.
    """
    if len(sys.argv) > 2:
        # Check if there are at least two command line arguments.
        ip_introduced = sys.argv[1]
        sn_introduced = sys.argv[2]
        sn_length = 16
        sn_base = 16
        # The following dictionary makes sense if we think about base 16 (letters like Z should not be there, hence we guess that it should be a 2)
        # Only uppercase is needed because inside the function everything is uppercased
        sn_dictionary = str.maketrans("QOIZS", "00122")
        ip_return, sn_return = ip_sn_validator(ip_introduced, sn_introduced, sn_length, sn_base, sn_dictionary)
        return ip_return, sn_return
    else:
        # Raise an error if the expected number of arguments is not provided.
        error_return(
            "Falta de argumentos necesarios, introduzca como primer argumento la ip y como segundo argumento la sn",
            "Lack of required arguments, correct format: python program.py [IP] [SN]",
        )
