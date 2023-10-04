from flask import Flask, request, render_template
import paramiko

app = Flask(__name__)
app = Flask(__name__, template_folder='views')

#Valores del servidor SSH
hostname = "192.168.1.1"
username = "mauro"
port = 22
password = "admin123"
comando = "pwd"

@app.route('/')
def index():
    return render_template('index.html', ip=hostname)

@app.route('/ssh', methods=['POST'])
def ssh():
    hostname = request.form['ip']

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(comando)
        result = stdout.read().decode('utf-8')
    except Exception as e:
        result = str(e)
    finally:
        ssh.close()

    return render_template('index.html', ip=hostname, result=result)

if __name__ == '__main__':  
    app.run(debug=True)
