# sysAPI v0.1

### What is it?

sysAPI is a Python (using [Flask] framework) based API for Linux systems. The package creates a small webserver that runs as a service.

Available API methods (v0.1)

* /ls/ - Get a list files for a specific directory
* /cat/ - Get file content
* /uptime/ - Get uptime

### Requirements

It has only been tested on Debian 7.0 x64 for now.

These packages are required

* build-essential
* python-pip


### Installation

Create and install the package 

```sh
$ git clone https://github.com/JuustoMestari/sysAPI.git
$ cd sysAPI
$ chmod 755 sysAPI-x.x -R
$ dpkg-deb --build sysAPI-x.x
```

Install the package

```sh
$ dpkg -i sysAPI-x.x.deb
```

This will also install :

* virtualenv
* flask

When the installation has been done, a keypair used for API authentication has been created in **/srv/sysAPI/authfile.conf**.
The webserver has also started and the API documentation can be found at : http://youripaddress:8888 . The server runs on all interfaces by default.

### Use

sysAPI runs as a service 

```sh
$ service sysAPI start/stop/restart
```
You can modify the webserver port and interface in **/srv/sysAPI/app/__init.py__** , make sure to restart sysAPI.


You can generate extra keypairs (secretkey#accesskey) for authentication. By default, each key is 32 bytes.

```sh
$ cd /srv/sysAPI
$ python genKeyPair.py
```


### Uninstallation

```sh
$ dpkg -r sysAPI-x.x
```

### To Do

* Add more features and commands

[Flask]:http://flask.pocoo.org/