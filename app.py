from flask import Flask, request, render_template
import pexpect
import pymongo
from config import OLT_IP, OLT_PASSWORD, OLT_USERNAME

app = Flask(__name__, template_folder='views')
client = pymongo.MongoClient("mongodb+srv://scapitani:santiago2005@cluster0.gds8oe1.mongodb.net/?retryWrites=true&w=majority")
db = client["ITC_CLI"]
collection = db["orders"]

@app.route('/')
def index():
    return render_template('index.html', ip=OLT_IP)

@app.route('/historial', methods=['GET'])
def historial():
    ip = request.args.get('ip')
    sn = request.args.get('sn')
    historial = list(collection.find({"ip":ip,"sn":sn}, {"id":0}).sort("fecha", pymongo.DESCENDING))
    for item in historial:
        item["fecha"] = item["fecha"].strftime("%Y-%m-%d %H:%M:%S")
    return render_template('historial.html', historial=historial)

@app.route('/ssh', methods=['POST'])
def shh():
    ip = request.form.get('ip')
    sn = request.form.get('sn')
    output_lines = []
    
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

        output_lines.extend(ssh_session.before.decode("utf-8").splitlines())

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

        document = {
            "ip": ip,
            "sn": sn,
            "comando": "\n".join(output_lines)
        }
        collection.insert_one(document)
    
        result = f"SSH Command Output {output_lines}\n\nAdditional Output: {output0}"
        ssh_session.sendline("exit")
        ssh_session.close()
    except Exception as e:
        result = str(e)
    
    return render_template('index.html', ip=OLT_IP, result=result,)

if __name__ == '__main__':
    app.run(debug=True)
    