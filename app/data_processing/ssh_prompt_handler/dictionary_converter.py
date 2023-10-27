# Import necessary modules and functions
from app.data_processing.ssh_prompt_handler.session_spawn import (
    get_ssh_session,
    close_session,
)
from app.data_processing.ssh_prompt_handler.ont_prompt import (
    get_ont_info_prompt,
    get_ont_optical_info_prompt,
)
from app.data_processing.ssh_prompt_handler.prompt_analysis import (
    get_dictionary_from_prompt,
)
from app.data_processing.error_handler.user_input import ip_sn_validator


# Define a function to retrieve sample information prompts
def sample_prompt():
    """
    Generate sample ONT information and optical information prompts.

    Returns:
        tuple: Two sample information prompts (info_sample, opt_info_sample) as strings.
    """
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
  OLT Rx ONT optical power(dBm)          : -15.66
    """
    return info_sample, opt_info_sample


# Define a function to retrieve ONT information dictionaries
def get_ont_info_dictionaries(olt_ip, ont_sn, debug_mode=False):
    """
    Retrieve ONT information and optical information dictionaries for a given OLT IP and ONT serial number.

    Args:
        olt_ip (str): The OLT IP address.
        ont_sn (str): The ONT serial number.
        debug_mode (bool): A flag for debugging mode (optional).

    Returns:
        dict: Dictionary containing ONT information.
        dict: Dictionary containing ONT optical information.
    """
    if not debug_mode:
        # Create a character translation dictionary to replace certain characters in ONT SN.
        sn_dictionary = str.maketrans("QOIZS", "00122")

        # Validate and potentially modify the OLT IP and ONT SN using the provided character translation.
        olt_ip, ont_sn = ip_sn_validator(olt_ip, ont_sn, 16, 16, sn_dictionary)

        # Establish an SSH session with the specified OLT IP address.
        ssh_session = get_ssh_session(olt_ip, session_timeout=6)

        # Retrieve the ONT information prompt specific to the ONT SN.
        ont_info_prompt = get_ont_info_prompt(ssh_session, ont_sn)

        # Extract and parse the ONT information from the prompt into a dictionary.
        ont_info_dic = get_dictionary_from_prompt(ont_info_prompt)

        # Retrieve the optical information prompt based on the ONT information.
        ont_optical_info_prompt = get_ont_optical_info_prompt(ssh_session, ont_info_dic)

        # Extract and parse the optical information from the prompt into a dictionary.
        ont_optical_info_dic = get_dictionary_from_prompt(ont_optical_info_prompt)

        # Close the SSH session.
        close_session(ssh_session)
    else:
        # In debug mode, use sample information prompts for testing and debugging.
        info_sample_prompt, opt_info_sample_prompt = sample_prompt()
        ont_info_dic = get_dictionary_from_prompt(info_sample_prompt)
        ont_optical_info_dic = get_dictionary_from_prompt(opt_info_sample_prompt)

    # Return the ONT information and optical information dictionaries.
    return ont_info_dic, ont_optical_info_dic
