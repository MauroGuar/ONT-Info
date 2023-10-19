import pexpect
from app.config import OLT_USERNAME, OLT_PASSWORD
from app.data_processing.error_handler.errors import error_return


def ssh_startup_analysis(ssh_session, expect_index):
    """
    Analyzes startup responses during SSH session initiation and handles various scenarios.

    Args:
        ssh_session (pexpect.spawn): SSH session object.
        expect_index (int): Index of the expected pattern to match in the response.

    Raises:
        Exception: Custom error messages are raised based on different expect_index values.
    """
    if expect_index == 1:
        ssh_session.sendline("yes")
        ssh_session.expect("password:")
    elif expect_index == 2:
        error_return(
            "se acabo el tiempo de espera, revise que la ip introducida sea correcta o contacte con su administrador",
            "pexpect TIMEOUT",
        )
    elif expect_index == 3:
        error_return(
            "No se ha encontrado una ruta al dispositivo, revise la ip introducida o contacte con su administrador",
            "ssh: connect to host $IP port $PORT: No route to host",
        )
    elif expect_index == 4:
        error_return(
            "la conexion esta siendo terminada por el servidor, puede que su ip haya sido bloqueada, espere 10 minutos o contacte con su administrador",
            "kex_exchange_identification: read: Connection reset by peer",
        )
    elif expect_index == 5:
        error_return(
            "No se ha encontrado la red, revise su conexion a internet o contacte con su administrador",
            "Network is unreachable",
        )
    elif expect_index == 6:
        error_return(
            "Conexion rechazada, verifique la ip introducida o contacte con su administrador",
            "ssh: connect to host $host port $PORT: Connection refused",
        )


def ssh_password_analysis(ssh_session, expect_index):
    """
    Analyzes password-related responses during SSH session initiation and handles various scenarios.

    Args:
        ssh_session (pexpect.spawn): SSH session object.
        expect_index (int): Index of the expected pattern to match in the response.

    Raises:
        Exception: Custom error messages are raised based on different expect_index values.
    """
    if expect_index == 1:
        error_return(
            "Alguien mas esta ocupando la sesion ssh, espere unos segundos o contacte con su administrador",
            "Reenter times have reached the upper limit.",
        )
    elif expect_index == 2:
        error_return(
            "Contraseña incorrecta, revise que la contraseña este bien escrita o contacte con su administrador",
            "Password was requested again after being entered = wrong password OR wrong user",
        )
    elif expect_index == 3:
        error_return(
            "Conexion a dispositivo no soportado, contacte con su administrador",
            "prompt identifier is $(typical unix) and not >(OLT)",
        )
    elif expect_index == 4:
        error_return(
            "su IP ha sido bloqueada por multiples intentos de acceso fallidos, contacte con su administrador",
            "Received disconnect from $IP port $PORT: The IP address has been locked",
        )


def get_ssh_session(olt_ip, session_timeout=0):
    """
    Establishes an SSH session with the specified OLT device.

    Args:
        olt_ip (str): IP address of the OLT device.
        session_timeout (int): Timeout value for the SSH session (default is 0).

    Returns:
        pexpect.spawn: SSH session object.
    """
    ssh_session = pexpect.spawn(f"ssh {OLT_USERNAME}@{olt_ip}")

    if session_timeout > 0:
        ssh_session.timeout = session_timeout

    ssh_startup_analysis(
        ssh_session,
        ssh_session.expect(
            [
                "password:",
                r"\(yes\/no\/\[fingerprint\]\)",
                pexpect.TIMEOUT,
                "No route to host",
                "Connection reset by peer",
                "Network is unreachable",
                "Connection refused",
            ]
        ),
    )

    ssh_session.sendline(OLT_PASSWORD)

    ssh_password_analysis(
        ssh_session,
        ssh_session.expect(
            [
                ">",
                "Reenter times have reached the upper limit.",
                "password:",
                r"\$",
                "The IP address has been locked",
            ]
        ),
    )

    return ssh_session


def close_session(ssh_session):
    """
    Closes the SSH session.

    Args:
        ssh_session (pexpect.spawn): SSH session object to be closed.
    """
    ssh_session.close()
