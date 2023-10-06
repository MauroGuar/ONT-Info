import pexpect
from config import OLT_IP, OLT_PASSWORD, OLT_USERNAME
from session_spawn import get_ssh_session, close_session
from ont_tables import get_ont_tables


def main():
    ssh_session = get_ssh_session(session_timeout=4)

    ont_info_table, ont_optical_info_table = get_ont_tables(ssh_session)

    print("SSH Command Output:")
    print(ont_info_table)
    print(ont_optical_info_table)

    close_session(ssh_session)


if __name__ == "__main__":
    main()
