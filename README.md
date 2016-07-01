# About
Flowroute-messenger is software that I am using to send and recieve SMS messages through the RESTful API provided by flowroute. 

# Install

I strongly recommend the use of python virtualenvs. With virtualenvwrapper, this can be done with

~~~~ sh
mkvirtualenv flowroute
~~~~


## API Keys
The API authentication information is saved in a file called `secrets.yml`. Edit the `secrets.yml.default` file in the `flowroute` directory to add your [API keys](https://manage.flowroute.com/accounts/preferences/api/) and rename it to `secrets.yml`.

## Installation with pip
After creating a virtualenv (or not, for a system-wide installation) and creating a `secrets.yml` file, the package can be installed with pip. 

~~~~~ sh
cd flowroute-messenger
pip3 install .  
~~~~~

# Usage

## Sending messages

the sendmessage utility that is installed with the package can send SMS messages from the command line. 

~~~~
$ sendmessage -h 
usage: sendmessage [-h] from to message

Simple utility to send messages through the Flowroute API

positional arguments:
  from        The number to send from
  to          The number to send to
  message     The message body
~~~~

## Recieving messages

Also included in the package is `smslistener`, which is currently set up to autoreply to any messages it recieves with a blurb about how I have moved to the UK (which was the motivation behind this project). It is designed to be deployed to a wsgi server (like apache mod\_wsgi). In order to recieve messages with it at all, it is neccesary to open port 1997 (this is configurable in `listener.py`) to the public internet and configure the SMS callback url in the Flowroute API control panel. 