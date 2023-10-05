import pexpect
from config import OLT_IP, OLT_PASSWORD, OLT_USERNAME
from session_spawn import get_ssh_session


def main():
    ssh_session = get_ssh_session(session_timeout=4)

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
