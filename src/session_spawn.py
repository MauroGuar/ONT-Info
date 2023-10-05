import pexpect
from config import OLT_IP, OLT_PASSWORD, OLT_USERNAME


def ssh_startup_analysis(ssh_session, expect_index):
    if expect_index == 1:
        ssh_session.sendline("yes")
        ssh_session.expect("password:")
    elif expect_index == 2:
        print("ERROR")
        ssh_session.close()


def ssh_password_analysis(ssh_session, expect_index):
    if expect_index == 1:
        print("ERROR")
        ssh_session.close()
    if expect_index == 2:
        print("ERROR")
        ssh_session.close()
    if expect_index == 3:
        print("ERROR")
        ssh_session.close()


def get_ssh_session(session_timeout=0):
    ssh_session = pexpect.spawn(f"ssh {OLT_USERNAME}@{OLT_IP}")

    if session_timeout > 0:
        ssh_session.timeout = session_timeout

    ssh_startup_analysis(
        ssh_session,
        ssh_session.expect(
            ["password:", r"\(yes\/no\/\[fingerprint\]\)", pexpect.TIMEOUT]
        ),
    )

    ssh_session.sendline(OLT_PASSWORD)

    ssh_password_analysis(
        ssh_session,
        ssh_session.expect(
            [">", "Reenter times have reached the upper limit.", "password:", r"\$"]
        ),
    )

    return ssh_session
