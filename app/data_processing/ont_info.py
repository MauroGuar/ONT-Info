from .session_spawn import get_ssh_session, close_session
from .ont_tables import get_ont_info_table, get_optical_info_table
from .prompt_analysis import get_dictionary_from_table


def get_ont_info(olt_ip, ont_sn):
    ssh_session = get_ssh_session(olt_ip, session_timeout=4)

    ont_info_table = get_ont_info_table(ssh_session, ont_sn)

    ont_info_dic = get_dictionary_from_table(ont_info_table)

    ont_optical_info_table = get_optical_info_table(ssh_session, ont_info_dic)

    ont_optical_info_dic = get_dictionary_from_table(ont_optical_info_table)

    close_session(ssh_session)

    return (ont_info_dic, ont_optical_info_dic)
