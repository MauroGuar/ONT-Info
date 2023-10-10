import sys
from errors import error_return
def ipv4_validation(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        error_return("La ip introducida no esta compuesta por 4 partes divididas por un '.'","The introduced ip is not divided by 4 '.' characters")

    try:
        for parte in partes:
            num = int(parte)
            if not 0 <= num <= 255:
                error_return("Alguna de las partes de la ip introducida cae fuera del rango numerico requerido: [0-255]", "At least one of the introduced 'octates' is out of the 8 bit unsigned number range(0 to 255)")
            if len(parte) > 1 and parte[0] == '0':
                error_return("La ip introducida contiene 0s a la izquierda o de relleno, formato no permitido.","The ip contains zero padding/leading zeroes (like the zero in 013), incorrect format")
    except ValueError:
        error_return("La ip introducida contiene caracteres que no son enteros, verifique por errores de syntaxis ", "parseint failed")

    return True
def sn_validation(serial,length,base):
    try:
        # verifies if the serial has the exact introduced length
        if len(serial) != length:
            error_return(f"El sn introducido no satisface la longitud requerida: {length} caracteres",f"The introduced serial number does not satisfy the exact length condition of {length}")

        # tries to convert the number to the introduced base
        int(serial, base)
    except ValueError:
        error_return(f"Alguno de los caracteres introducidos como parte del sn no satisfacen la base necesaria: base {base}", f"the serial number does not satisfy the base per character(Value error when parsing), in this case, base: {base}")
def get_input():
    ip_introduced= sys.argv[1]
    sn_introduced= sys.argv[2]
    sn_length= 16
    sn_base= 16
    if len(sys.argv) > 2:
        ipv4_validation(ip_introduced)
        sn_validation(sn_introduced,sn_length,sn_base)
        return ip_introduced, sn_introduced
    else:
        error_return("Falta de argumentos necesarios, introduzca como primer argumento la ip y como segundo argumento la sn","lack of required arguments, correct format: python program.py [IP] [SN]")