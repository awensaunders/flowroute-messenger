import requests
import yaml 
import io
import json

default = {'flowroute': {'passwd': 'password', 'user': 'user'}, 'exists': True}

class Secrets(object):
    """Class for manipulating the .secrets.yml file which contains authentication information required to send messages"""
    def __init__(self, path):
        """Constructor. Takes 1 argument, filepath"""
        try:
            self.file = io.open(path, 'r+t')
        except IOError:
            try:
                self.file = io.open(path, 'a+t')
                print("Config file does not exist -- Creating.")
                self._write(default) 
            except IOError:
                print("Error! Config file could not be read or written")
        self.data = self._read()
        self.user = self.data['flowroute']['user']
        self.passwd = self.data['flowroute']['passwd']
                
    def _write(self, dict):
        """Writes the config and overwrites any existing data takes one argument"""
        self.file.seek(0)
        self.file.truncate()
        yaml.dump(dict, self.file, default_flow_style=False)
    
    def _read(self): 
        """Reads the config and returns it as a dictionary"""
        self.file.seek(0)
        return yaml.safe_load(self.file)

class Messages(object):
    def __init__(self):
        """Constructor, takes argument from_number (should be string), which is the number which the messages should originate from (must be owned by your account)."""
        self.secrets = Secrets(".secrets.yml")
        
    def send(self, from_number, to_number, body):
        """Method for sending messages. Takes three arguments, from, to, and body. To is the string of the phone number the message should be sent to. Body is the content of the message. This method returns a message detail record identifier that can be used to look up a message at a later date"""
        self.from_number = str(from_number)
        self.to_number = str(to_number)
        payload = {'to': self.to_number, 'from': self.from_number, 'body': str(body)}
        self.response = requests.post('https://api.flowroute.com/v2/messages', auth=(self.secrets.user, self.secrets.passwd), data=json.dumps(payload))
        return self.response.json()['data']['id']
    
    def lookup(self, mdr):
        """This method returns a parsed JSON response (dictionary) with all the information available about a particular message. This method takes one argument: mdr. This argument should be a string representing the message detail record identifier as returned by Messages.send()"""
        self.response = requests.get('https://api.flowroute.com/v2/messages/' + str(mdr), auth=(self.secrets.user, self.secrets.passwd))
        return self.response.json()
    