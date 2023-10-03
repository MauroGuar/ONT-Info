import re

# El texto de salida de la consola
console_output = """
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
  Rx optical power(dBm)                  : -15.10
  Rx power current warning threshold(dBm): [-,-]
  Rx power current alarm threshold(dBm)  : [-29.0,-8.0]
  Tx optical power(dBm)                  : 3.61
  Tx power current warning threshold(dBm): [-,-]
  Tx power current alarm threshold(dBm)  : [0.0,6.0]
  Laser bias current(mA)                 : 11
  Tx bias current warning threshold(mA)  : [-,-]
  Tx bias current alarm threshold(mA)    : [0.000,90.000]
  Temperature(C)                         : 49
  Temperature warning threshold(C)       : [-,-]
  Temperature alarm threshold(C)         : [-10,80]
  Voltage(V)                             : 3.240
  Supply voltage warning threshold(V)    : [-,-]
  Supply voltage alarm threshold(V)      : [3.000,3.600]
  OLT Rx ONT optical power(dBm)          : -15.41
  CATV Rx optical power(dBm)             : -
  CATV Rx power alarm threshold(dBm)     : [-,-]
  -----------------------------------------------------------------------------
"""

# Utilizamos expresiones regulares para buscar los valores de Rx optical power(dBm) y OLT Rx ONT optical power(dBm)
rx_optical_power_match = re.search(
    r"Rx optical power\(dBm\)\s+:\s+([0-9.-]+)", console_output
)
olt_rx_ont_optical_power_match = re.search(
    r"OLT Rx ONT optical power\(dBm\)\s+:\s+([0-9.-]+)", console_output
)

# Comprobamos si se encontraron coincidencias y extraemos los valores
if rx_optical_power_match:
    rx_optical_power = rx_optical_power_match.group(1)
else:
    rx_optical_power = None

if olt_rx_ont_optical_power_match:
    olt_rx_ont_optical_power = olt_rx_ont_optical_power_match.group(1)
else:
    olt_rx_ont_optical_power = None

# Imprimimos los valores
print("Rx optical power(dBm):", rx_optical_power)
print("OLT Rx ONT optical power(dBm):", olt_rx_ont_optical_power)
