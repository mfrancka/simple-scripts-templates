#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser()
# -infra nad --ips can't be used together
infra_group = parser.add_mutually_exclusive_group(required=True)
infra_group.add_argument('-i', '--infra', choices=['dev', 'preprod', 'prod'],
                         default='dev',
                         help='Infrastructure which will be used'
                         )
# --ip can be added multiple time --ip a --ip b and will do ['a','b']
infra_group.add_argument('--ip', action="append",
                         help='List of destination IPs')
parser.add_argument('--to',
                    default='dev', help='Recipient of message',
                    required=True, metavar=('address@domain.com'))
# it put from arguments to args.sender variable
parser.add_argument('--from',
                    default='null@ovh.net', help='Sender address',
                    required=False, metavar=('address@domain.com')
                    dest='sender')
parser.add_argument('--data-file',
                    help='Path to file with whole email (DATA)')
parser.add_argument('--recipients-file',
                    help='Path to file with recipients of messages')
parser.add_argument('--attachment',
                    help='Path to file to attach')
parser.add_argument('--emails-number',
                    help='How many emails need to be send', type=int)
parser.add_argument('--continous-run',
                    help='Sent emails without limit', action='store_true')
parser.add_argument('--senders-number', type=int,
                    default=10, help='How many parallel senders should be runned')
args = parser.parse_args()
print(args)
