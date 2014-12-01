from flask import Flask, jsonify, request
import os
import time
import sys
from helpers import *
from httpError import httperror
from stat import *

blacklistFile = os.getcwd()+"/blacklist.conf"
whitelistFile = os.getcwd()+"/whitelist.conf"
#maxsize 50K
maxfilesize = 50000

def cmd_cat(fullpath):
    try:

        if not fullpath.startswith('/'):
            fullpath = '/'+fullpath

        if not os.path.isfile(fullpath):
            return httperror('directory', 'This is not a file!', 404)

        if isinlist(blacklistFile, fullpath):
            return httperror('blacklist', 'This path is in the blacklist !', 403)

        if not isinlist(whitelistFile, fullpath):
            return httperror('whitelist', 'This path is not in the whitelist !', 403)

        with open(fullpath, 'r') as myfile:
            singlefile = {
                'filepath': fullpath,
                'filecontent': myfile.read(maxfilesize),
                'filesize': os.path.getsize(fullpath),
                'filelimit': maxfilesize
            }

        return jsonify({'file': singlefile})
    except OSError as e:
        return httperror('OSError', 'Maybe the command doesn\'t exist? {0} : {1}'.format(e.errno, e.strerror), 400)
    except UnicodeDecodeError:
        return httperror('Decoding Error', 'Can\'t decode this file.', 400)
    except:
        exctype, value = sys.exc_info()[:2]
        return httperror('Error', 'Unhandled Error : {0} -> {1}'.format(exctype, value), 400)