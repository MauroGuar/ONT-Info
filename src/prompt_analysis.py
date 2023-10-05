import re

regex = r".*\s:\s(.+)\s*\n"
# El texto de salida de la consola
test_str = (
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
coincidencias = re.findall(regex, test_str)

# Imprime las coincidencias
print("Coincidencias del grupo 1:", coincidencias)
