from hashlib import sha1
import os
import hmac

authfile = os.getcwd()+"/authfile.conf"


def isinlist(listfile, path):

    with open(listfile, 'r') as myfile:
        for line in myfile:
            line = line.replace('\n', '').replace('\r', '')
            if line == path or ('*' in line and line.replace("/*", '') in path):
                return True
    return False


def isauth(request):
    try:
        authorization = request.headers.get('Authorization')
        xdate = request.headers.get('X-Date')
        if not authorization or not xdate:
            return False

        authorization = authorization.split(':')
        accesskey = authorization[0]
        signature = authorization[1]

        infile, secretkey = isauthfile(str(accesskey))
        if not infile:
            return False

        message = str(request.method)+' '+str(request.url)+'\n'+str(xdate)
        hashed = hmac.new(str(accesskey), message+secretkey, sha1)
        if hashed.digest().encode("base64").rstrip('\n') != signature:
            return False
        return True
    except:
        return False


def isauthfile(accesskey):
    with open(authfile, 'r') as myfile:
        for line in myfile:
            line = line.replace('\n', '').replace('\r', '')
            keypair = line.split('#')
            if keypair[1] == accesskey:
                return True, keypair[0]
    return False,''