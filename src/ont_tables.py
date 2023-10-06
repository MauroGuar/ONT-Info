import pexpect


def send_line(session, line_to_send):
    session.sendline(line_to_send)


def expect_prompt(session, prompt_to_expect):
    session.expect(prompt_to_expect)


def expect_asterisk(session):
    expect_prompt(session, "#")


def expect_bracket(session):
    expect_prompt(session, "}:")


def send_enter(session, number_of_enters=1):
    for i in range(number_of_enters):
        send_line(session, "")


def expect_hyphens(session):
    expect_prompt(session, "----")


def get_info_table(session):
    table = ""
    send_line(session, "enable")
    expect_asterisk(session)
    send_line(session, "display ont info by-sn 48575443655C13A0")
    expect_bracket(session)
    send_enter(session)
    expect_hyphens(session)
    send_enter(session, 3)
    send_line(session, "q")
    expect_asterisk(session)
    table = session.before.decode("utf-8")
    return table


def get_optical_info_table(session):
    table = ""
    send_line(session, "config")
    expect_asterisk(session)
    send_line(session, "interface gpon 0/3")
    expect_asterisk(session)
    send_line(session, "display ont optical-info 0 1")
    expect_bracket(session)
    send_enter(session)
    expect_hyphens(session)
    send_enter(session, 5)
    send_line(session, "q")
    expect_asterisk(session)
    table = session.before.decode("utf-8")
    return table


def get_ont_tables(ssh_session):
    ont_info_table = get_info_table(ssh_session)
    ont_optical_info_table = get_optical_info_table(ssh_session)
    return (ont_info_table, ont_optical_info_table)
