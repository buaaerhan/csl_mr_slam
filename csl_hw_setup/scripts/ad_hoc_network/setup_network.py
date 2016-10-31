#!/usr/bin/env python
# Tue Oct 4 12:31:30 EEST 2016, Nikos Koukis

"""
Tue Oct 4 12:31:34 EEST 2016, Nikos Koukis

Current script sets up the adhoc network connection for the current host.

TODO:
- Have the netowrk as a variable e.g. net_prefix="192.168.100"

"""

from __future__ import print_function
import argparse
from subprocess import call
import os
import sys
from time import gmtime, strftime


# Import the modules directory
modules_dir = os.path.join(os.path.dirname(__file__), "../../misc")
if modules_dir not in sys.path:
    sys.path.insert(0, modules_dir)
from custom_exceptions import NoRootAccessError, \
    ProgramNotFoundError, InterfaceNotFoundError

# Arguement Parsing
parser = argparse.ArgumentParser(
    description='Setup Ad-Hoc network configuration for multi-robot SLAM')

# wireless interface
parser.add_argument(
    '-w', '--wlan_interface',
    default="wlan0",
    help='Specify the wireless interface')

# dry-run flag
parser.add_argument(
    '-d', '--dry-run',
    default=False,
    action="store_true",
    help="Monitor the actions that the script will take if executed")

# ip-address of current host
parser.add_argument(
    '-I', '--ip_address',
    help="Specify the IP address of the current host")

# Run interactively
parser.add_argument(
    "-i", "--interactive",
    action="store_true",
    help="Run script in interactive mode")
args = vars(parser.parse_args())


def main():
    interactive = args["interactive"]
    dry_run = args["dry_run"]

    # Specify whether we are running for real or on a dry-run
    if dry_run:
        print("[!] Script is running on a dry run! Specified commands will not be executed")


    if interactive:
        print("[!] In interactive mode:")
        wlan_interface = raw_input(
            "wlan interface to be used: [Default = wlan0] ")
        ip_address = raw_input(
            "Current host's IP address in ad-hoc: [Default = 192.168.100.11] ")
    else:
        wlan_interface = args["wlan_interface"]
        ip_address = args["ip_address"]

    check_reqs(ip_address=ip_address, wlan_interface=wlan_interface)

    # create interfaces file
    interfaces_main = "/etc/network/interfaces"
    # interfaces_main = "kalimera"

    # Search for current wlan* configuration in interfaces file - if there,
    # exit
    print("Checking if {wlan} configuration already exists in {fname}".format(
        wlan=wlan_interface,
        fname=interfaces_main))
    wlan_already_configured = False
    wlan_exists_line = "iface {}".format(wlan_interface)
    with open(interfaces_main, "r") as f:
        lines = [line.strip() for line in f.readlines()]

        for a_line in lines:
            if wlan_exists_line in a_line:
                wlan_already_configured = True
                break
    if wlan_already_configured:
        print("{wlan} is already configured in {fname}. If configuration is not correct, remove the corresponding entries and run the program again Exiting...".format(
            wlan=wlan_interface,
            fname=interfaces_main))
        sys.exit(1)

    # write the interfaces file
    with open(interfaces_main, "a") as f:
        comments = [
            "Automatically generated script - {date}".format(
                date=strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
        ]
        directives = ["auto {wlan}".format(wlan=wlan_interface),
                      "iface {wlan} inet static".format(wlan=wlan_interface),
                      "   wireless-essid multi-robot-exp",
                      "   wireless-mode ad-hoc",
                      "   wireless-channel 5",
                      "   wireless-enc off",
                      "   address {addr}".format(addr=ip_address),
                      "   netmask 255.255.255.0",
                      "   broadcast 192.168.100.255",
                      "   gateway 192.168.100.1",
                      "   dns-nameservers 192.168.100.1",
                      ]

        comments = ["# " + comment + os.linesep for comment in comments]
        directives = [directive + os.linesep for directive in directives]

        print("Writing interfaces file...\nContents:")
        for line in comments + directives:
            print("\t" + line, sep="")

        if not dry_run:
            f.write(os.linesep)
            f.write("".join(comments))
            f.write("".join(os.linesep))
            f.write("".join(directives))

    print("Successfully written ad-hoc configuration to {}".format(
        interfaces_main))


    # Restart the network interface for the changes to take effect
    print("Restarting {wlan} interface...".format(wlan=wlan_interface))
    if not dry_run:
        call(["ifconfig", wlan_interface, "down"])
        call(["ifconfig", wlan_interface, "up"])
    print("OK")



def check_reqs(**kargs):
    """Check if the reuired tools exist in the system."""

    # root access?
    if os.getuid() != 0:
        raise NoRootAccessError()

    # ifconfig installed?
    print("Checking if ifconfig command is available...")
    if call(["which", "ifconfig"]) != 0:
        raise ProgramNotFoundError("ifconfig")
    print("OK")

    # wlan interface exists?
    print("Checking if given interface is valid...")
    if call(["iwconfig", kargs["wlan_interface"]]) != 0:
        print("")
        raise InterfaceNotFoundError(kargs["wlan_interface"])
    print("OK")



if __name__ == "__main__":
    main()

