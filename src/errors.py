import sys
def error_return(human_error, technical_error):
    print(f"\n{human_error}")
    print(f"\nError tecnico: '{technical_error}'")
    sys.exit()