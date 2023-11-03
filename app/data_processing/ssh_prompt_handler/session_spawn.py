# Import necessary modules and functions
import pexpect
from app.config import OLT_USERNAME, OLT_PASSWORD
from app.data_processing.error_handler.errors import error_return


def ssh_startup_analysis(ssh_session, expect_index):
    """
    This function handles the analysis of the SSH startup process and performs error handling based on the expect_index.

    Args:
        ssh_session (pexpect.spawn): The SSH session created using pexpect.
        expect_index (int): An index that determines the specific condition to handle.

    Returns:
        None
    """
    if expect_index == 1:
        ssh_session.sendline("yes")
        ssh_session.expect("password:")
    elif expect_index == 2:
        error_return(
            "Timeout occurred; please verify the correct IP address or contact your administrator.",
            "pexpect TIMEOUT",
        )
    elif expect_index == 3:
        error_return(
            "No route to the device; please check the entered IP or contact your administrator.",
            "ssh: connect to host $IP port $PORT: No route to host",
        )
    elif expect_index == 4:
        error_return(
            "Server is terminating the connection; your IP may be blocked. Please wait for 10 minutes or contact your administrator.",
            "kex_exchange_identification: read: Connection reset by peer",
        )
    elif expect_index == 5:
        error_return(
            "Network not found; check your internet connection or contact your administrator.",
            "Network is unreachable",
        )
    elif expect_index == 6:
        error_return(
            "Connection refused; verify the entered IP or contact your administrator.",
            "ssh: connect to host $host port $PORT: Connection refused",
        )


def ssh_password_analysis(ssh_session, expect_index):
    """
    This function handles the analysis of the SSH password authentication process and performs error handling based on the expect_index.

    Args:
        ssh_session (pexpect.spawn): The SSH session created using pexpect.
        expect_index (int): An index that determines the specific condition to handle.

    Returns:
        None
    """
    if expect_index == 1:
        error_return(
            "Another user is occupying the SSH session. Please wait for a few seconds or contact your administrator.",
            "Reenter times have reached the upper limit.",
        )
    elif expect_index == 2:
        error_return(
            "Incorrect password; please ensure the password is correctly entered or contact your administrator.",
            "Password was requested again after being entered = wrong password OR wrong user",
        )
    elif expect_index == 3:
        error_return(
            "Device connection not supported; contact your administrator.",
            "prompt identifier is $(typical unix) and not >(OLT)",
        )
    elif expect_index == 4:
        error_return(
            "Your IP has been blocked due to multiple failed access attempts; contact your administrator.",
            "Received disconnect from $IP port $PORT: The IP address has been locked",
        )


def get_ssh_session(olt_ip, session_timeout=0):
    """
    Establish an SSH session to the specified OLT device and perform error handling during startup and password authentication.

    Args:
        olt_ip (str): The IP address of the OLT device.
        session_timeout (int): Optional session timeout setting.

    Returns:
        pexpect.spawn: The SSH session established with the OLT device.
    """
    ssh_session = pexpect.spawn(f"ssh -o HostKeyAlgorithms=ssh-rsa {OLT_USERNAME}@{olt_ip}")

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
    Close the SSH session.

    Args:
        ssh_session (pexpect.spawn): The SSH session to be closed.

    Returns:
        None
    """
    ssh_session.close()
