<p align="center">
  <a href="https://www.inwx.com/en/" target="_blank">
    <img src="https://images.inwx.com/logos/inwx.png">
  </a>
</p>

INWX Domrobot Python 2.7 Client
=========
**If you're looking for our Python 3 Client you can find it [here.](https://github.com/inwx/python-client)**

You can access all functions of our frontend via our API, which is available via the XML-RPC or JSON-RPC protocol and thus can be easily consumed with all programming languages.

There is also an OT&E test system, which you can access via [ote.inwx.com](https://ote.inwx.com/en/). Here you will find the known web interface which is using a test database. On the OT&E system no actions will be charged. So you can test as much as you like there.

Documentation
------
You can view a detailed description of the API functions in our documentation. You can find the online documentation [by clicking here](https://www.inwx.de/en/help/apidoc).

If you still experience any kind of problems don't hesitate to contact our [support via email](mailto:support@inwx.de).

Example
-------

```python
from inwx import domrobot, prettyprint, getOTP
from configuration import get_account_data

def main():
    api_url, username, password, shared_secret = get_account_data(True)
    inwx_conn = domrobot(api_url, False)
    loginRet = inwx_conn.account.login({'lang': 'en', 'user': username, 'pass': password})

    if 'resData' in loginRet:
        loginRet = loginRet['resData']

    if 'tfa' in loginRet and loginRet['tfa'] == 'GOOGLE-AUTH':
        loginRet = inwx_conn.account.unlock({'tan': getOTP(shared_secret)})

    domain = "mydomain.com"
    checkRet = inwx_conn.domain.check({'domain': domain})
    print(prettyprint.domain_check(checkRet))

if __name__ == '__main__':
    main()
```

You can also look at the example.py in the Project.

License
----

MIT
