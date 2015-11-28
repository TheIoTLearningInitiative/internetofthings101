#!/usr/bin/env/python

'''
 mBotCommands.py
 Authored by: Yonattan Louise, Javier Perez, Gerardo Acevedo

 Send commands to control mBot via Bluetooth. Example of usage:

 ./mBotCommands.py --target 00:05:02:03:14:E9 --command "f"
 commands
 f=100
 b=500/9;
'''

import sys
import bluetooth
import argparse

def find_mBot():
	target_name = "Makeblock"
	target_address = None

	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
		if target_name == bluetooth.lookup_name( bdaddr ):
		    target_address = bdaddr
		    break

	if target_address is not None:
		print "found target bluetooth device with address ", target_address
	else:
		print "could not find target bluetooth device nearby"
	return target_address

def send_command(bd_addr, command, id_node=5):
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, 1)) #first port in bluetooth

	command = command + "/%d;"%id_node
	print "Sending command (%s)" % command
	sock.send(command)
	sock.settimeout(2)
	response = ""
	try:
		while True:
			r = sock.recv(255)
			if not r:
				break

			response = response + r
			if r.find(";") != -1: # we have reach end of message
				break
	except:
		pass
	print "Response: (%s)" % response

	sock.close()

def send_commands(bd_addr, str_commands):

	if not bd_addr:
		print "Cannot connect to mBod"
		sys.exit(1)

	if not str_commands:
		print "Command to send (q to quit) \nFormat [F|R|B|L]([=d] lenght in mls, default=100)*  example: F"
		while True:
			command = raw_input("Command to send: ")
			if command.strip() == "q":
				break
			if command.find("=") == -1:
				command = command + "=100"
			send_command(bd_addr, command.strip())
	else:
		for command in str_commands.split(";"):
			if command:
				send_command(bd_addr, command.strip())

parser = argparse.ArgumentParser(description='mBot bluetooth controller.')
parser.add_argument('--target', help='mBot bluetooth mac address.')
parser.add_argument('--command', default=None, help='command to run on mBot.')
args = parser.parse_args()

if args.target == None:
	bd_addr = find_mBot()
else:
	bd_addr = args.target

send_commands(bd_addr, args.command)
