import pexpect
from config import OLT_IP, OLT_PASSWORD, OLT_USERNAME


def error(session, error_str):
    print(error_str)
    session.close()
    exit


def main():
    ssh_session = pexpect.spawn(f"ssh {OLT_USERNAME}@{OLT_IP}")
    # Establish SSH connection
    ssh_session.timeout = 4
    i = ssh_session.expect(
        ["password:", r"\(yes\/no\/\[fingerprint\]\)", pexpect.TIMEOUT],
    )
    if i == 1:
        ssh_session.sendline("yes")
        ssh_session.expect("password:")
    elif i == 2:
        error(ssh_session, "No se pudo establecer la conexion")
    ssh_session.sendline(OLT_PASSWORD)
    i = ssh_session.expect(
        [">", "Reenter times have reached the upper limit.", "password:", r"\$"]
    )
    if i == 1:
        error(
            ssh_session,
            "Alguien mas esta usando la sesion ssh, espere unos segundos o contacte con su administrador",
        )
    elif i == 2:
        error(
            ssh_session,
            "La contraseña que esta intentando utilizar es incorrecta, contacte con su administrador",
        )
    elif i == 3:
        error(
            ssh_session,
            "parece que se esta conectando a un dispositivo no soportado, contacte con su administrador",
        )
    ssh_session.sendline("enable")
    ssh_session.expect("#")
    ssh_session.sendline("display ont info by-sn 48575443655C13A0")
    ssh_session.expect("}:")
    ssh_session.sendline("")
    ssh_session.expect("----")
    ssh_session.sendline("")
    ssh_session.sendline("")
    ssh_session.sendline("")
    ssh_session.send("q")
    ssh_session.expect("#")
    output = ssh_session.before.decode("utf-8")
    print(output)
    ssh_session.sendline("config")
    ssh_session.expect("#")
    ssh_session.sendline("interface gpon 0/3")
    ssh_session.expect("#")
    ssh_session.sendline("display ont optical-info 0 1")
    ssh_session.expect("}:")
    ssh_session.sendline("")
    ssh_session.expect("----")
    ssh_session.sendline("")
    ssh_session.sendline("")
    ssh_session.sendline("")
    ssh_session.sendline("")
    ssh_session.sendline("")
    ssh_session.send("q")
    ssh_session.expect("#")
    output0 = ssh_session.before.decode("utf-8")

    # Print the output of the SSH command
    print("SSH Command Output:")
    print(output0)

    # Close the SSH session
    ssh_session.sendline("exit")
    ssh_session.close()


if __name__ == "__main__":
    main()