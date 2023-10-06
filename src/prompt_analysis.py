import re

test_str0 = (
    "MA5800-X7#display ont info by-sn 48575443655C13A0 \n"
    "{ <cr>||<K> }: \n\n"
    "  Command:\n"
    "          display ont info by-sn 48575443655C13A0 \n"
    "  -----------------------------------------------------------------------------\n"
    "  F/S/P                   : 0/3/0\n"
    "  ONT-ID                  : 1\n"
    "  Control flag            : active\n"
    "  Run state               : online\n"
    "  Config state            : normal\n"
    "  Match state             : match\n"
    "  DBA type                : SR\n"
    "  ONT distance(m)         : 12\n"
    "  ONT last distance(m)    : -\n"
    "  ONT battery state       : not support\n"
    "  Memory occupation       : 28%\n"
    "  CPU occupation          : 1%\n"
    "  Temperature             : 55(C)\n"
    "  Authentic type          : SN-auth\n"
    "  SN                      : 48575443655C13A0 (HWTC-655C13A0)\n"
    "  Management mode         : OMCI\n"
    "  Software work mode      : normal\n"
    "  Isolation state         : normal\n"
    "  ONT IP 0 address/mask   : -\n"
    "  Description             : ONT_NO_DESCRIPTION\n"
    "  Last down cause         : -\n"
    "  Last up time            : 2023-10-05 03:06:37+08:00\n"
    "  Last down time          : -        \n"
    "  Last dying gasp time    : -        \n"
    "  ONT online duration     : 0 day(s), 2 hour(s), 19 minute(s), 38 second(s) \n"
    "  Type C support          : Not support\n"
    "  Interoperability-mode   : ITU-T    \n"
    "  Power reduction status  : -        \n"
    "  ONT NNI type            : auto     \n"
    "  ONT actual NNI type     : 10G/2.5G \n"
    "                                     \n"
    "MA5800-X7"
)
test_str1 = """
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
regex_name_value = r'([^\s][^:\n]*\S)\s+:\s*([^\n]*\S)[^\n]*'

# Inicializar un diccionario para almacenar los name_value_pair_0
name_value_pair_0 = {}

# Buscar todas las matches_0 usando el patrón regex
matches_0 = re.findall(regex_name_value, test_str1)

# Almacenar las matches_0 en el diccionario
for name, value in matches_0:
    name_value_pair_0[name.strip()] = value.strip()

# Mostrar los name_value_pair_0 almacenados
# for name, value in name_value_pair_0.items():
#     print(f'{name}: {value}')

f_s = name_value_pair_0['F/S/P'][:3] 
f_s_formatted = name_value_pair_0['F/S/P'][:1] + "\\" + name_value_pair_0['F/S/P'][1:3]
p = name_value_pair_0 ['F/S/P'][4]
ont_id = name_value_pair_0 ['ONT-ID']
run_state = name_value_pair_0['Run state']



# Imprime las name_value_pair_0
print("f_s es ",f_s," f_s_formatted es ",f_s_formatted," y p es ",p)


