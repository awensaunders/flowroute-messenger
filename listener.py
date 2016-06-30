#!/usr/bin/env python3
import flask
from modules import flowroute

app = Flask(__name__)

@app.route('/',  method='POST')
def post_run():
    print(request.get_json())
    
    
    
    
if __name__ == '__main__':
    app.run(
        host="192.168.42.128",
        port=int("1997")
    )