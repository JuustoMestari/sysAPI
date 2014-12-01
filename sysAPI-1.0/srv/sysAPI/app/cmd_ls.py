from flask import Flask, jsonify, request
import os
import time
import sys
from helpers import *
from httpError import httperror
from stat import *

blacklistFile = os.getcwd()+"/blacklist.conf"
whitelistFile = os.getcwd()+"/whitelist.conf"


def cmd_ls(fullpath):
    try:

        if not fullpath.startswith('/'):
            fullpath = '/'+fullpath

        #if not fullpath.endswith('/'):
            #fullpath += '/'

        if not os.path.isdir(fullpath) and not os.path.isfile(fullpath):
            return httperror('directory', 'This path doesn\'t exist!', 404)

        if isinlist(blacklistFile, fullpath):
            return httperror('blacklist', 'This path is in the blacklist !', 403)

        if not isinlist(whitelistFile, fullpath):
            return httperror('whitelist', 'This path is not in the whitelist !', 403)

        allfiles = []
        listfiles = [fullpath]

        if os.path.isdir(fullpath):
            listfiles = os.listdir(fullpath)

        #mask http://stackoverflow.com/questions/5337070/how-can-i-get-a-files-permission-mask
        for files in listfiles:
            #lstat to avoid following symlink
            perm = os.lstat(os.path.join(fullpath, files))
            singlefile = {
                'filename': files,
                'filepath': os.path.join(fullpath, files),
                'filepermissions': oct(perm.st_mode & 0o0777),
                'fileUID': perm.st_uid,
                'fileGID': perm.st_gid,
                #'filedate': time.ctime(perm.st_atime),
                'filedate': perm.st_atime,
                'filesize': perm.st_size,
                'isdir': S_ISDIR(perm.st_mode),
                'isfile':  S_ISREG(perm.st_mode),
                'islink': S_ISLNK(perm.st_mode),
            }
            allfiles.append(singlefile)
        return jsonify({'path': fullpath, 'files': allfiles})
    except OSError as e:
        return httperror('OSError', 'Maybe the command doesn\'t exist? {0} : {1}'.format(e.errno, e.strerror), 400)
    except:
        exctype, value = sys.exc_info()[:2]
        return httperror('Error', 'Unhandled Error : {0} -> {1}'.format(exctype, value), 400)