import xmlrpclib
from xmlrpclib import _Method
import urllib2

class domrobot ():
    def __init__ (self, address, debug = False):
        self.url = address
        self.debug = debug 
        self.cookie = None
        self.version = "1.0"

    def __getattr__(self, name):
        return _Method(self.__request, name)

    def __request (self, methodname, params):
        tuple_params = tuple([params[0]])
        requestContent = xmlrpclib.dumps(tuple_params, methodname)
        if(self.debug == True):
            print("Anfrage: "+str(requestContent).replace("\n", ""))
        headers = { 'User-Agent' : 'DomRobot/'+self.version+' Python-v2.7', 'Content-Type': 'text/xml','content-length': str(len(requestContent))}
        if(self.cookie!=None):
            headers['Cookie'] = self.cookie
        req = urllib2.Request(self.url, requestContent, headers)
        response = urllib2.urlopen(req)
        responseContent = response.read()
        cookies = response.info().getheader('Set-Cookie')
        if(self.debug == True):
            print ("Antwort: "+str(responseContent).replace("\n", ""))
        apiReturn = xmlrpclib.loads(responseContent)
        apiReturn = apiReturn[0][0]
        if(apiReturn["code"]!=1000):
            raise NameError('There was a problem: %s (Error code %s)' % (apiReturn['msg'], apiReturn['code']), apiReturn)
            return False

        if(cookies!=None):
                cookies = response.info().getheader('Set-Cookie')
                self.cookie = cookies
                if(self.debug == True):
                    print("Cookie:" + self.cookie)
        if("resData" in apiReturn):
            return apiReturn["resData"]

class prettyprint (object):
    """
    This object is just a collection of prettyprint helper functions for the output of the XML-API.
    """

    @staticmethod
    def contacts(contacts):
        """
        iterable contacts:  The list of contacts to be printed.
        """
        output = "\nCurrently you have %i contacts set up for your account at InterNetworX:\n\n" % len(contacts)
        for contact in contacts:
            output += "ID: %s\nType: %s\n%s\n%s\n%s %s\n%s\n%s\nTel: %s\n------\n" % (contact['id'], contact['type'], contact['name'], contact['street'], contact['pc'], contact['city'], contact['cc'], contact['email'], contact['voice'])
        return output

    @staticmethod
    def domains(domains):
        """
        list domains:  The list of domains to be pretty printed.
        """
        output = "\n%i domains:\n" % len(domains)
        for domain in domains:
            output += "Domain: %s (Type: %s)\n" % (domain['domain'], domain['type'])
        return output

    @staticmethod
    def nameserversets(nameserversets):
        """
        list namerserversets:  The list of nameserversets to be pretty printed.
        """
        count, total = 0, len(nameserversets)
        output = "\n%i nameserversets:\n" % total
        for nameserverset in nameserversets:
            count += 1
            output += "%i of %i - ID: %i consisting of [%s]\n" % (count, total, nameserverset['id'], ", ".join(nameserverset['ns']))
        return output

    @staticmethod
    def domain_log(logs):
        """
        list logs:  The list of nameserversets to be pretty printed.
        """
        count, total = 0, len(logs)
        output = "\n%i log entries:\n" % total
        for log in logs:
            count += 1
            output += "%i of %i - %s status: '%s' price: %.2f invoice: %s date: %s remote address: %s\n" % (count, total, log['domain'], log['status'], log['price'], log['invoice'], log['date'], log['remoteAddr'])
            output += "           user text: '%s'\n" % log['userText'].replace("\n",'\n           ')
        return output
    
    @staticmethod
    def domain_check(checks):
        """
        list checks:  The list of domain checks to be pretty printed.
        """
        count, total = 0, len(checks)
        output = "\n%i domain check(s):\n" % total
        for check in checks['domain']:
            count += 1
            output += "%s = %s" % (check['domain'], check['status'])
        return output
        
