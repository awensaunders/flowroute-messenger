#!/usr/bin/env python3
from flask import Flask, request
import flowroute.flowroute
app = Flask(__name__)

msg = flowroute.flowroute.Messages()
text = "Hi! If you're looking for Awen, he has moved to the UK. His new phone number is +44 (0) 7455230843. Please do not reply to this automated message."

@app.route('/',  methods=['POST'])
def post_run():
    POST_request = request.get_json()
    msg.send(POST_request['to'], POST_request['from'], text)
    return '200 OK'
    
    
def main():
#    msg = flowroute.flowroute.Messages()
    app.run(
        host="0.0.0.0",
        port=int("1997")
    )    
if __name__ == '__main__':