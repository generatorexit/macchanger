#!/usr/bin/python3
import subprocess,os,re,random
from argparse import ArgumentParser

parser = ArgumentParser(description="macchanger [option] ",usage="python3 macchanger --help",epilog="Example: python3 macchanger.py -i [interface] -m [XX:XX:XX:XX:XX:XX]")
req_parser = parser.add_argument_group("Required Arguments")

req_parser.add_argument('-i','--interface',dest="iface",metavar='',type=str,help="Interface you want to change MAC")
parser.add_argument('-m','--mac',dest="newmac",metavar='',type=str,help="MAC Address to change [Manual Mode only] ")
parser.add_argument('-s','--show',help="Show available interface and exit",action="store_true")
parser.add_argument('-R','--Random',help="Automaticaly assign Random MAC",action="store_true")
parser.add_argument('-r','--reset',help="Reset to Original MAC",action="store_true")
args = parser.parse_args()


def control_new_mac(iface):
    ifconfig = subprocess.check_output(["ifconfig",iface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None

def macchanger():
    # -i -m
    if args.iface and args.newmac:
        subprocess.call(["sudo","ifconfig",args.iface,"down"])
        subprocess.call(["sudo","ifconfig",args.iface,"hw","ether",args.newmac])
        subprocess.call(["sudo","ifconfig",args.iface,"up"])
        finalized_mac = control_new_mac(str(args.iface))
        if finalized_mac == args.newmac:
            print("[+]Mac address changed to: " + args.newmac)
        else:
            print("Error!")

    # -i -R
    elif args.iface and args.Random:
        list3=list()
        list4=list()
        for i in range(0,6):
            list1=["a","b","c","d","e","f"]
            random_number = random.randint(0,9)
            random_letter = random.choice(list1)
            list3.append(random_number)
            list4.append(random_letter)
        random_mac_address=str(list3[0])+str(list4[0])+":"+str(list3[1])+str(list4[1])+":"+str(list3[2])+str(list4[2])+":"+str(list3[3])+str(list4[3])+":"+str(list3[4])+str(list4[4])+":"+str(list3[5])+str(list4[5])
        subprocess.call(["ifconfig",args.iface,"down"])
        subprocess.call(["ifconfig",args.iface,"hw","ether",random_mac_address])
        subprocess.call(["ifconfig",args.iface,"up"])  
        finalized_mac = control_new_mac(str(args.iface))
        if finalized_mac == random_mac_address:
            print("[+]Mac address changed to: " + random_mac_address)
        else:
            print("Error!")

    # -i -r
    elif args.reset:
        dsmeg_results = subprocess.check_output(["dmesg"])
        change_original = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(dsmeg_results))
        subprocess.call(["ifconfig",args.iface,"down"])
        subprocess.call(["ifconfig",args.iface,"hw","ether",str(change_original.group(0))])
        subprocess.call(["ifconfig",args.iface,"up"])  
        return print("[+]Permanent MAC: {}\n[+]New MAC: {}".format(str(change_original.group(0)),str(change_original.group(0))))

    # -i -s
    elif args.show:
        print("Available Interface")
        os.system("echo -------------------")
        os.system("sudo netstat -i | awk '{print $1}' > .show.txt")
        os.system("echo ------------------- >> .show.txt")
        subprocess.call(["tail","-n","+3",".show.txt"])
        subprocess.call(["sudo","rm","-rf",".show.txt"])

    else:
        print("-"*63)
        print("Use the '-h' or '--help' parameter to get help. \vcoded by mksec")
        print("-"*63)

if __name__ == '__main__':
    macchanger()