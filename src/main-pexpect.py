import pexpect

# OLT SSH connection details
olt_ip = "172.16.17.48"
username = "mauro"
password = "admin123"

# SSH command to be executed
ssh_command = "enable"

# Establish SSH connection
ssh_session = pexpect.spawn(f"ssh {username}@{olt_ip}")
i = ssh_session.expect(['password:',r'\(yes\/no\/\[fingerprint\]\)'])
if i == 1:
    ssh_session.sendline("yes")
    ssh_session.expect("password:")
ssh_session.sendline(password)
i = ssh_session.expect([">","Reenter times have reached the upper limit.","password:"])
if i == 1:
    print("Alguien mas esta usando la sesion ssh, espere unos segundos o contacte con su administrador")
    ssh_session.close
    exit
if i == 2:
    print("La contraseña que esta intentando utilizar es incorrecta, contacte con su administrador")
    ssh_session.close
    exit
ssh_session.sendline(ssh_command)
ssh_session.expect("#")
ssh_session.sendline("display ont info by-sn 48575443655C13A0")
ssh_session.expect("}:")
ssh_session.sendline("")
ssh_session.expect("----")
ssh_session.send("q")
ssh_session.expect("#")
output = ssh_session.before.decode("utf-8")

# Print the output of the SSH command
print("SSH Command Output:")
print(output)

# Close the SSH session
ssh_session.sendline("exit")
ssh_session.close()
