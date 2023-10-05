from flask import Flask, request, render_template
import pexpect
from config import OLT_IP, OLT_PASSWORD, OLT_USERNAME

app = Flask(__name__, template_folder='views')

@app.route('/')
def index():
    return render_template('index.html', ip=OLT_IP)

@app.route('/ssh', methods=['POST'])
def shh():
    try:
        ssh_session = pexpect.spawn(f"ssh {OLT_USERNAME}@{OLT_IP}")
        ssh_session.expect(["password:", r"\(yes\/no\/\[fingerprint\]\)", pexpect.TIMEOUT])
        ssh_session.sendline(OLT_PASSWORD)
        ssh_session.expect([">", "Reenter times have reached the upper limit.", "password:", r"\$"])
        ssh_session.sendline("enable")
        ssh_session.expect("#")
        ssh_session.sendline("display ont info by-sn 48575443655C13A0")
        ssh_session.expect("}:")
        ssh_session.sendline("")
        ssh_session.expect("----")
        ssh_session.sendline("")
        ssh_session.sendline("")
        ssh_session.sendline("")
        ssh_session.send("q")
        ssh_session.expect("#")
        output = ssh_session.before.decode("utf-8")

        ssh_session.sendline("config")
        ssh_session.expect("#")
        ssh_session.sendline("interface gpon 0/3")
        ssh_session.expect("#")
        ssh_session.sendline("display ont optical-info 0 1")
        ssh_session.expect("}:")
        ssh_session.sendline("")
        ssh_session.expect("----")
        ssh_session.sendline("")
        ssh_session.sendline("")
        ssh_session.sendline("")
        ssh_session.sendline("")
        ssh_session.sendline("")
        ssh_session.send("q")
        ssh_session.expect("#")
        output0 = ssh_session.before.decode("utf-8")
    
        result = f"SSH Command Output {output}\n\nAdditional Output: {output0}"
        ssh_session.sendline("exit")
        ssh_session.close()
    except Exception as e:
        result = str(e)
    
    return render_template('index.html', ip=OLT_IP, result=result)

if __name__ == '__main__':
    app.run(debug=True)
    