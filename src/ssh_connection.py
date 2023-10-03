from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException


def ssh_get_connection(hostname, port, username, password):
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        ssh_client.connect(
            hostname=hostname, port=port, username=username, password=password
        )
    except AuthenticationException:
        print("Authentication Error. Please verify your credentials.")
    except SSHException as e:
        print("Error establishing SSH connection:", str(e))
    else:
        return ssh_client
