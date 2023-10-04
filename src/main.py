from ssh_connection import ssh_get_connection


def main():
    hostname = "172.16.17.48"
    username = "mauro"
    port = 22
    password = "admin123"

    ssh = ssh_get_connection(hostname, port, username, password)

    stdin, stdout, stderr = ssh.exec_command("pwd")

    output_lines = stdout.readlines()

    print("Resultado del comando:")
    for line in output_lines:
        print(line.strip())

    ssh.close()


if __name__ == "__main__":
    main()
