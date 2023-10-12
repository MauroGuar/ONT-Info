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


def get_info_prompt(session, ont_sn):
    ont_info_prompt = ""
    send_line(session, "enable")
    expect_asterisk(session)
    send_line(session, f"display ont info by-sn {ont_sn}")
    expect_bracket(session)
    send_enter(session)
    expect_hyphens(session)
    send_enter(session, 3)
    send_line(session, "q")
    expect_asterisk(session)
    ont_info_prompt = session.before.decode("utf-8")
    return ont_info_prompt


def get_optical_info_prompt(session, ont_info_dic):
    ont_optical_info_prompt = ""

    ont_front_slot = ont_info_dic["f/s/p"][:3]
    ont_port = ont_info_dic["f/s/p"][4]
    ont_id = ont_info_dic["ont-id"]

    send_line(session, "config")
    expect_asterisk(session)
    send_line(session, f"interface gpon {ont_front_slot}")
    expect_asterisk(session)
    send_line(session, f"display ont optical-info {ont_port} {ont_id}")
    expect_bracket(session)
    send_enter(session)
    expect_hyphens(session)
    send_enter(session, 5)
    send_line(session, "q")
    expect_asterisk(session)
    ont_optical_info_prompt = session.before.decode("utf-8")
    return ont_optical_info_prompt


def get_ont_info_prompt(ssh_session, ont_sn):
    ont_info_prompt = get_info_prompt(ssh_session, ont_sn)
    return ont_info_prompt


def get_ont_optical_info_prompt(ssh_session, ont_info_dic):
    ont_optical_info_prompt = get_optical_info_prompt(ssh_session, ont_info_dic)
    return ont_optical_info_prompt
