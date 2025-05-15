from twisted.protocols.ftp import FTPFactory, FTPRealm
from twisted.internet import reactor
from twisted.cred.portal import Portal
from twisted.cred.checkers import AllowAnonymousAccess, FilePasswordDB
from ftplib import FTP as ftp

def __init__():
    pass
p = Portal(FTPRealm('./'), [AllowAnonymousAccess(), FilePasswordDB("pass.dat")])
f = FTPFactory(p)

def run():
    reactor.listenTCP(21, f)
    print("FTP server running...")
    reactor.run()
# run()
