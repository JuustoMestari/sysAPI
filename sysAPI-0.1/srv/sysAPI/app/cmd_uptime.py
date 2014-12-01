from flask import Flask, jsonify, request
import os
import time
import sys
from helpers import *
from httpError import httperror
from stat import *
from datetime import timedelta



def cmd_uptime():
    try:

        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds = uptime_seconds))

        return jsonify({'uptime': uptime_string})
    except OSError as e:
        return httperror('OSError', 'Maybe the command doesn\'t exist? {0} : {1}'.format(e.errno, e.strerror), 400)
    except:
        exctype, value = sys.exc_info()[:2]
        return httperror('Error', 'Unhandled Error : {0} -> {1}'.format(exctype, value), 400)