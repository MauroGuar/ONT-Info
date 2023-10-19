import pexpect
from app.data_processing.error_handler.errors import error_return


def send_line(session, line_to_send):
    """
    Sends a command line to the SSH session.

    Args:
        session (pexpect.spawn): SSH session object.
        line_to_send (str): Command line to be sent to the SSH session.
    """
    session.sendline(line_to_send)


def expect_prompt(session, prompt_to_expect):
    """
    Expects a specific prompt in the SSH session.

    Args:
        session (pexpect.spawn): SSH session object.
        prompt_to_expect (str or list): Prompt(s) to expect in the session.

    Returns:
        int: Index of the matched prompt in the list if a list of prompts is provided.
    """
    return session.expect(prompt_to_expect)


def expect_hashtag(session):
    """
    Expects a '#' prompt in the SSH session.

    Args:
        session (pexpect.spawn): SSH session object.
    """
    expect_prompt(session, "#")


def expect_bracket(session):
    """
    Expects a '}' prompt in the SSH session.

    Args:
        session (pexpect.spawn): SSH session object.
    """
    expect_prompt(session, "}:")


def send_enter(session, number_of_enters=1):
    """
    Sends a specified number of 'Enter' key presses to the SSH session.

    Args:
        session (pexpect.spawn): SSH session object.
        number_of_enters (int): Number of 'Enter' key presses to send (default is 1).
    """
    for i in range(number_of_enters):
        send_line(session, "")


def expect_hyphens(session):
    """
    Expects a '----' prompt in the SSH session.

    Args:
        session (pexpect.spawn): SSH session object.
    """
    expect_prompt(session, "----")


def get_info_prompt(session, ont_sn):
    """
    Retrieves ONT information prompt for a given ONT serial number.

    Args:
        session (pexpect.spawn): SSH session object.
        ont_sn (str): ONT serial number.

    Returns:
        str: ONT information prompt as a string.
    """
    ont_info_prompt = ""
    send_line(session, "enable")
    expect_hashtag(session)
    send_line(session, f"display ont info by-sn {ont_sn}")
    expect_bracket(session)
    send_enter(session)
    i = expect_prompt(session, ["----", "ONT does not exist"])
    if i == 1:
        error_return(
            "The entered Serial Number (SN) was not found. Please check the spelling and ensure the correct OLT is entered, or contact your administrator.",
            "The required ONT does not exist",
        )
    send_enter(session, 3)
    send_line(session, "q")
    expect_hashtag(session)
    ont_info_prompt = session.before.decode("utf-8")
    return ont_info_prompt


def get_optical_info_prompt(session, ont_info_dic):
    """
    Retrieves optical information prompt for a given ONT information dictionary.

    Args:
        session (pexpect.spawn): SSH session object.
        ont_info_dic (dict): Dictionary containing ONT information.

    Returns:
        str: Optical information prompt as a string.
    """
    ont_optical_info_prompt = ""

    ont_front_slot = ont_info_dic["f/s/p"][:3]
    ont_port = ont_info_dic["f/s/p"][4]
    ont_id = ont_info_dic["ont-id"]

    send_line(session, "config")
    expect_hashtag(session)
    send_line(session, f"interface gpon {ont_front_slot}")
    expect_hashtag(session)
    send_line(session, f"display ont optical-info {ont_port} {ont_id}")
    expect_bracket(session)
    send_enter(session)
    expect_hyphens(session)
    send_enter(session, 5)
    send_line(session, "q")
    expect_hashtag(session)
    ont_optical_info_prompt = session.before.decode("utf-8")
    return ont_optical_info_prompt


def get_ont_info_prompt(ssh_session, ont_sn):
    """
    Retrieves ONT information prompt for a given SSH session and ONT serial number.

    Args:
        ssh_session (pexpect.spawn): SSH session object.
        ont_sn (str): ONT serial number.

    Returns:
        str: ONT information prompt as a string.
    """
    ont_info_prompt = get_info_prompt(ssh_session, ont_sn)
    return ont_info_prompt


def get_ont_optical_info_prompt(ssh_session, ont_info_dic):
    """
    Retrieves optical information prompt for a given SSH session and ONT information dictionary.

    Args:
        ssh_session (pexpect.spawn): SSH session object.
        ont_info_dic (dict): Dictionary containing ONT information.

    Returns:
        str: Optical information prompt as a string.
    """
    ont_optical_info_prompt = get_optical_info_prompt(ssh_session, ont_info_dic)
    return ont_optical_info_prompt
