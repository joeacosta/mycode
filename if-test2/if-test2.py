#!/usr/bin/env python3
# iftest2
ipchk = '192.168.0.1' # this line now prompts teh user for input

if ipchk =='192.168.70.1': # if a match on '192.168.70.1'
	print('Looks like the IP address of teh Gateway was set: ' + ipchk + ' This is not recommended.') # indented under if
elif ipchk: # if any data is provided, this will test true
	print('Looks like the IP address was set: ' + ipchk) # indented under if
else: # if data is NOT provided
	print('You did not provide input.') # indented under else