inwx.com XML-RPC Python 2.7 Client
=========
**Please notice, that the Return of the Function contains now the complete API-Return not only the resData**

You can access all functions of our frontend via an application programming interface (API). Our API is based on the XML-RPC protocol and thus can be easily addressed by almost all programming languages. The documentation and programming examples in PHP, Java, Ruby and Python can be downloaded here.

There is also an OT&E test system, which you can access via ote.inwx.com. Here you will find the known web interface which is using a test database. On the OTE system no actions will be charged. So you can test how to register domains etc.

Documentation
------
You can view a detailed description of the API functions in our documentation. The documentation as PDF ist part of the Projekt. You also can read the documentation online http://www.inwx.de/en/help/apidoc

Example
-------

```python
from inwx import domrobot, prettyprint
from configuration import get_account_data

def main():
    api_url, username, password = get_account_data(True)
    inwx_conn = domrobot(api_url, False)
    loginRet = inwx_conn.account.login({'lang': 'en', 'user': username, 'pass': password});

    domain = "mydomain.com"
    checkRet = inwx_conn.domain.check({'domain': domain})
    print prettyprint.domain_check(checkRet)
    
if __name__ == '__main__':
    main()
```

You can also look at the example.py in the Project.

License
----

MIT
