import re

test_str0 = """
{ <cr>||<K> }:  

  Command:
          display ont info by-sn 48575443655C13A0 
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
MA5800-X7        
"""

# Patrón regex para encontrar names y sus valuees
regex_name_value = r"\s{2}([^\s][^:\n]*\S)\s*:\s*([^\n]*\S)[^\n]*"

# Inicializar un diccionario para almacenar los name_value_pair_0
name_value_pair_0 = {}

# Buscar todas las matches_0 usando el patrón regex
matches_0 = re.findall(regex_name_value, test_str0)

# Almacenar las matches_0 en el diccionario
for name, value in matches_0:
    name_value_pair_0[name.strip()] = value.strip()

# Mostrar los name_value_pair_0 almacenados
# for name, value in name_value_pair_0.items():
#     print(f'{name}: {value}')

f_s = name_value_pair_0["F/S/P"][:3]
f_s_formatted = name_value_pair_0["F/S/P"][:1] + "\\" + name_value_pair_0["F/S/P"][1:3]
p = name_value_pair_0["F/S/P"][4]
ont_id = name_value_pair_0["ONT-ID"]
run_state = name_value_pair_0["Run state"]
description = name_value_pair_0["Description"]
last_down_cause = name_value_pair_0["Last down cause"]
last_up_time = name_value_pair_0["Last up time"]
last_down_time = name_value_pair_0["Last down time"]
ont_online_duration = name_value_pair_0["ONT online duration"]


# Imprime las name_value_pair_0
print("f_s es ", f_s, " f_s_formatted es ", f_s_formatted, " y p es ", p)

test_str1 = """
{ <cr>||<K> }: 

  Command:
          display ont optical-info 0 62 
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
MA5800-X7
"""

name_value_pair_1 = {}

# Buscar todas las matches_1 usando el patrón regex
matches_1 = re.findall(regex_name_value, test_str1)

# Almacenar las matches_1 en el diccionario
for name, value in matches_1:
    name_value_pair_1[name.strip()] = value.strip()

rx_optical_power = name_value_pair_1["Rx optical power(dBm)"]
olt_rx_ont_optical_power = name_value_pair_1["OLT Rx ONT optical power(dBm)"]
