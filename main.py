import re
import subprocess

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start_vm', methods=['POST'])
def start_vm():
    vm_name = request.form.get('vm_name')
    try:
        subprocess.run(["VBoxManage", "startvm", vm_name, "--type", "headless"], check=True)
        return jsonify({"status": "success"}), 200
    except subprocess.CalledProcessError:
        return jsonify({"status": "error"}), 500


@app.route('/stop_vm', methods=['POST'])
def stop_vm():
    vm_name = request.form.get('vm_name')
    try:
        subprocess.run(["VBoxManage", "controlvm", vm_name, "poweroff"], check=True)
        return jsonify({"status": "success"}), 200
    except subprocess.CalledProcessError:
        return jsonify({"status": "error"}), 500


@app.route('/list_vms', methods=['GET'])
def list_vms():
    result = subprocess.run(["VBoxManage", "list", "vms"], capture_output=True, text=True, check=True)
    output = result.stdout.split('\n')
    vms = [re.search(r'\"(.+?)\"', line).group(1) if re.search(r'\"(.+?)\"', line) else None for line in output if line]
    return jsonify(vms)


@app.route('/list_active_vms', methods=['GET'])
def list_active_vms():
    result = subprocess.run(["VBoxManage", "list", "runningvms"], capture_output=True, text=True, check=True)
    output = result.stdout.split('\n')
    vms = [re.search(r'\"(.+?)\"', line).group(1) if re.search(r'\"(.+?)\"', line) else None for line in output if line]
    return jsonify(vms)


@app.route('/list_inactive_vms', methods=['GET'])
def list_inactive_vms():
    # Get all VMs
    result_all = subprocess.run(["VBoxManage", "list", "vms"], capture_output=True, text=True, check=True)
    all_vms = extract_vm_names(result_all.stdout.split('\n'))

    # Get active VMs
    result_active = subprocess.run(["VBoxManage", "list", "runningvms"], capture_output=True, text=True, check=True)
    active_vms = extract_vm_names(result_active.stdout.split('\n'))

    # Get inactive VMs
    inactive_vms = [vm for vm in all_vms if vm not in active_vms]
    return jsonify(inactive_vms)


def extract_vm_names(lines):
    return [re.search(r'\"(.+?)\"', line).group(1) if re.search(r'\"(.+?)\"', line) else None for line in lines if line]


if __name__ == '__main__':
    app.run(debug=True)
