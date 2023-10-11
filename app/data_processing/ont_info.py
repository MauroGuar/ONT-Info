from .session_spawn import get_ssh_session, close_session
from .ont_tables import get_ont_info_table, get_optical_info_table
from .prompt_analysis import get_dictionary_from_table
from .user_input import ip_sn_validator


def sample_prompt():
    info_sample = """
    -----------------------------------------------------------------------------
  F/S/P                   : 0/3/0
  ONT-ID                  : 62
  Control flag            : active
  Run state               : online
  Config state            : normal
  Match state             : match
  DBA type                : SR
  ONT distance(m)         : 12
  ONT last distance(m)    : -
  ONT battery state       : not support
  Memory occupation       : 27%
  CPU occupation          : 1%
  Temperature             : 58(C)
  Authentic type          : SN-auth
  SN                      : 48575443655C13A0 (HWTC-655C13A0)
  Management mode         : OMCI
  Software work mode      : normal
  Isolation state         : normal
  ONT IP 0 address/mask   : -
  Description             : ONT_NO_DESCRIPTION
  Last down cause         : -
  Last up time            : 2023-10-02 13:50:20+08:00
  Last down time          : -        
  Last dying gasp time    : -        
  ONT online duration     : 1 day(s), 19 hour(s), 55 minute(s), 20 second(s)
    """
    opt_info_sample = """
    -----------------------------------------------------------------------------
  ONU NNI port ID                        : 0
  Module type                            : 10G GPON
  Module sub-type                        : N1/N2a/E1/E2a
  Used type                              : ONU
  Encapsulation Type                     : BOSA ON BOARD
  Optical power precision(dBm)           : 3.0
  Vendor name                            : HUAWEI          
  Vendor rev                             : -
  Vendor PN                              : HW-BOB-0004     
  Vendor SN                              : 1817E0052872U   
  Date Code                              : 19-05-14
  Rx optical power(dBm)                  : -15.25
  Rx power current warning threshold(dBm): [-,-]
  Rx power current alarm threshold(dBm)  : [-29.0,-8.0]
  Tx optical power(dBm)                  : 3.80
  Tx power current warning threshold(dBm): [-,-]
  Tx power current alarm threshold(dBm)  : [0.0,6.0]
  Laser bias current(mA)                 : 11
  Tx bias current warning threshold(mA)  : [-,-]
  Tx bias current alarm threshold(mA)    : [0.000,90.000]
  Temperature(C)                         : 48
  Temperature warning threshold(C)       : [-,-]
    """
    return info_sample, opt_info_sample


def get_ont_info(olt_ip_introduced, ont_sn_introduced, debug_mode=False):
    if not debug_mode:
        sn_dictionary = str.maketrans('QOIZ','0012')

        olt_ip, ont_sn = ip_sn_validator(olt_ip_introduced,ont_sn_introduced,16,16,sn_dictionary)
        
        ssh_session = get_ssh_session(olt_ip, session_timeout=4)

        ont_info_table = get_ont_info_table(ssh_session, ont_sn)

        ont_info_dic = get_dictionary_from_table(ont_info_table)

        ont_optical_info_table = get_optical_info_table(ssh_session, ont_info_dic)

        ont_optical_info_dic = get_dictionary_from_table(ont_optical_info_table)

        close_session(ssh_session)
    else:
        info_sample_prompt, opt_info_sample_prompt = sample_prompt()
        ont_info_dic = get_dictionary_from_table(info_sample_prompt)
        ont_optical_info_dic = get_dictionary_from_table(opt_info_sample_prompt)

    return ont_info_dic, ont_optical_info_dic
