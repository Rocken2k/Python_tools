#!/usr/bin/env python

# Simple program to change MAC address
# Author: Rocken2k

import subprocess #to call the command to change the mac
import optparse #to interpreter the parameters
import re #to search the MAC in ifconfig

def get_arguments(): # setting the parameters
    attribute = optparse.OptionParser()
    attribute.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC")
    attribute.add_option("-m", "--mac", dest="new_mac", help="The new mac address")
    return attribute.parse_args()


def change_mac(interface, new_mac): # check inputs and do the changes
# Check if the inputs are valid
    if not options.interface:
        print("Missing the interface, use --help for more info")
        exit()
    elif not options.new_mac:
        print("Missing the new mac  use --help for more info")
        exit()
# Change mac
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_old_mac(): #get the value of the old mac (execution before changes)
    ifconfig_original = subprocess.check_output(["ifconfig", options.interface])
    old_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_original)
    print("THE !OLD! MAC WAS: " + old_mac.group(0))

def get_new_mac(): #get the value of the new mac (execution after changes)
    ifconfig_new = subprocess.check_output(["ifconfig", options.interface ])
    new_mac1 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_new)
    print ("THE !NEW! MAC IS:  " + new_mac1.group(0))

# Get the parameters to change the mac
(options, arguments) = get_arguments()

#To execute just when the parameters are correct
try:
    get_old_mac()
    change_mac(options.interface, options.new_mac) # Call the function to change mac
    get_new_mac()

except:
    exit()

