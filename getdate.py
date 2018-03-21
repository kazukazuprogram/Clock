#!/usr/bin/env python3

import datetime
from time import ctime
import sys

# please install module using pip-
# (sudo) pip install ntp lib
import ntplib

__author__ = "oomori"
__version__ = "1.2.0"

class MyNTPClient(object):
    def __init__(self, ntp_server_host):
        self.ntp_client = ntplib.NTPClient()
        self.ntp_server_host = ntp_server_host

    def get_nowtime(self, timeformat = '%Y/%m/%d %H:%M:%S'):
        try:
            res = self.ntp_client.request(self.ntp_server_host)
            nowtime = datetime.datetime.strptime(ctime(res.tx_time), "%a %b %d %H:%M:%S %Y")
            return nowtime.strftime(timeformat)
        except Exception as e:
            print("An error occured")
            print("The information of error is as following")
            print(type(e))
            print(e.args)
            print(e)
            sys.exit(1)

#ntp.nict.jp
#time.google.com
#s2csntp.miz.nao.ac.jp
#ntp.ring.gr.jp

def getdate(n):
    ntp_client = MyNTPClient('ntp.nict.jp')
    da = ntp_client.get_nowtime()
    print(da)
    db = da.split(' ')
    dca = db[0].split('/')
    dcb = db[1].split(':')
    data = dca + dcb
    if n == 0:
        re = data
    elif n == 1:
        re = db[1]
    return re

if __name__ == '__main__':
    print(getdate(1))
