#!/usr/bin/env python3

import argparse 
import flowroute.flowroute


def arguments():
    parser = argparse.ArgumentParser(description="Simple utility to send messages through the Flowroute API")
    parser.add_argument('from_number', help="The number to send from", metavar="from")
    parser.add_argument('to_number', help="The number to send to", metavar="to")
    parser.add_argument('message', help="The message body")
    return parser.parse_args()

def main():
    args = arguments()
    msg = flowroute.flowroute.Messages()
    mdr = msg.send(args.from_number, args.to_number, args.message)
    detail = msg.lookup(mdr)['data']['attributes']
    print("Message sent to", detail['to'])
    print("Cost:", detail['amount_display'])

if __name__ == '__main__':
    main()
   
   
   