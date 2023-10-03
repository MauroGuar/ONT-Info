import paramiko

hostname = "172.16.17.48"
username = "mauro"
port = 22
password = "admin123"

ssh = paramiko.SSHClient()

ssh.load_system_host_keys()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname=hostname, port=port, username=username, password=password)

    comando = "pwd"
    stdin, stdout, stderr = ssh.exec_command(comando)

    output_lines = stdout.readlines()

    print("Resultado del comando:")
    for line in output_lines:
        print(line.strip())

except paramiko.AuthenticationException:
    print("Error de autenticación. Por favor, verifica tus credenciales.")
except paramiko.SSHException as e:
    print("Error al establecer la conexión SSH:", str(e))
finally:
    # Cerrar la conexión SSH
    ssh.close()
