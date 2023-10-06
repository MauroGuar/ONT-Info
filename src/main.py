from config import OLT_IP_ENV, ONT_SN_ENV
from session_spawn import get_ssh_session, close_session
from ont_tables import get_ont_info_table, get_optical_info_table
from prompt_analysis import get_dictionary_from_table


def main():
    OLT_IP = OLT_IP_ENV
    ONT_SN = ONT_SN_ENV

    ssh_session = get_ssh_session(olt_ip=OLT_IP, session_timeout=4)

    ont_info_table = get_ont_info_table(ssh_session, ONT_SN)

    ont_info_dic = get_dictionary_from_table(ont_info_table)

    ont_optical_info_table = get_optical_info_table(ssh_session, ont_info_dic)

    ont_optical_info_dic = get_dictionary_from_table(ont_optical_info_table)

    # print(ont_info_table)
    # print(ont_optical_info_table)
    # print(f"{ont_info_dic}\n\n{ont_optical_info_dic}")

    close_session(ssh_session)


if __name__ == "__main__":
    main()
