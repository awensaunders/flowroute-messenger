# About
Flowroute-messenger is software that I am using to send (and one day hopefully receive) SMS messages through the RESTful API provided by flowroute. 

# Install
I strongly recommend the use of python virtualenvs. 

Using virtualenvwrapper:
`mkvirtualenv flowroute`
`pip install -r requirements.txt`

In order for the software to work, it is necessary to have a .secrets.yml file with the required authenitcation information. To create it, run `./secrets.py` (I have not finished this, check back in a couple days) 
