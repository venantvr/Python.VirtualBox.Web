# VirtualBox Manager Web Interface

## Description

Ce projet est une interface web pour gérer les machines VirtualBox sur un serveur hôte. L'interface permet de lister, démarrer, et arrêter des machines virtuelles. L'application est écrite en Python en utilisant le framework Flask.

## Fonctionnalités

* Listage des machines virtuelles inactives et actives
* Démarrage des machines inactives en mode "headless"
* Arrêt des machines actives
* Authentification de l'utilisateur via une page de connexion
* Interface utilisateur Bootstrap avec un thème en mode nuit

## Prérequis

* Python 3.x
* Flask

## Installation

* Installation en service...
```
rvv@rvv-desktop:~$ git clone https://github.com/venantvr/Python.VirtualBox.Web.git
rvv@rvv-desktop:~$ cd Python.VirtualBox.Web/
rvv@rvv-desktop:~$ pip install -r requirements.txt
rvv@rvv-desktop:~$ sudo nano /etc/systemd/system/virtualbox-manager-web.service
```

```
[Unit]
Description=VirtualBox Manager Web Interface
After=network.target

[Service]
User=rvv
WorkingDirectory=/home/rvv/Python.VirtualBox.Web
Environment="FLASK_APP=app.py"
Environment="FLASK_ENV=development"
ExecStart=/home/rvv/.local/bin/flask run --host=0.0.0.0 --port=5000

[Install]
WantedBy=multi-user.target
```

* Ne pas oublier de créer fichier credentials.json à la racine...
```
{
  "username": "admin",
  "password": "secret"
}
```

* Démarrage du service...
```
rvv@rvv-desktop:~$ sudo systemctl enable virtualbox-manager-web
rvv@rvv-desktop:~$ sudo systemctl daemon-reload
rvv@rvv-desktop:~$ sudo systemctl start virtualbox-manager-web
```
