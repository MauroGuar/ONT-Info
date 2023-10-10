import pexpect
from .config import OLT_USERNAME, OLT_PASSWORD


def ssh_startup_analysis(ssh_session, expect_index):
    if expect_index == 1:
        ssh_session.sendline("yes")
        ssh_session.expect("password:")
    elif expect_index == 2:
        print("ERROR")
    elif expect_index == 3:
        error_return(
            "No se ha encontrado una ruta al dispositivo, revise la ip introducida o contacte con su administrador",
            "ssh: connect to host $IP port $PORT: No route to host",
        )
    elif expect_index == 4:
        print("ERROR")
    elif expect_index == 5:
        print("ERROR")


def ssh_password_analysis(ssh_session, expect_index):
    if expect_index == 1:
        print("ERROR")
    elif expect_index == 2:
        print("ERROR")
    elif expect_index == 3:
        print("ERROR")
    elif expect_index == 4:
        print("ERROR")


def get_ssh_session(olt_ip, session_timeout=0):
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
    ssh_session.close()
