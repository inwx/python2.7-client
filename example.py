#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# author: InterNetworX, info →AT→ inwx.de

#############################################################################
###### This is an example of how to use the inwx class #######

from inwx import domrobot, prettyprint
from configuration import get_account_data

def main():
    api_url, username, password = get_account_data(True)
    inwx_conn = domrobot(api_url, False)
    loginRet = inwx_conn.account.login({'lang': 'en', 'user': username, 'pass': password})

    domain = "mydomain.com"
    checkRet = inwx_conn.domain.check({'domain': domain})
    print prettyprint.domain_check(checkRet)
    
if __name__ == '__main__':
    main()