#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# author: InterNetworX, info →AT→ inwx.de

#############################################################################
###### This is an example of how to use the inwx class #######

from inwx import domrobot, prettyprint, getOTP
from configuration import get_account_data

def main():
    api_url, username, password, shared_secret = get_account_data(True)
    inwx_conn = domrobot(api_url, False)
    loginRet = inwx_conn.account.login({'lang': 'en', 'user': username, 'pass': password})

    if 'tfa' in loginRet and loginRet['tfa'] == 'GOOGLE-AUTH':
        loginRet = inwx_conn.account.unlock({'tan': getOTP(shared_secret)})

    domain = "*"
    checkRet = inwx_conn.domain.list({})
    print(prettyprint.domains(checkRet))

if __name__ == '__main__':
    main()
