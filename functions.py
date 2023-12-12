import socket
import os
import subprocess

#visit a webpage with firefox
def visit_page():
    subprocess.call(["firefox", "https://youtube.com/"])

#os info
def sys_os_info():
    x = os.popen("uname -a").read()
    return x

#fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    return ', '.join(map(str, fibonacci_sequence[:n]))

#launch lxterminal
def launch_terminal():
    os.system("lxterminal")

#my ip
def getIP():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    return IPAddr

#ping an ip, check if host is up
def ping_check(): 
    IP = "google.com"
    c = "4"

    str1=("Pinging " + IP + " with count: " + c + "\n")
    strings=" "

    response = os.system("ping -c " + c + " -w 10 " + IP + " >/dev/null")
    if response == 0:
        str2=("Host is up")
        strings = [str1, str2]
        result = ', '.join(strings)
        return result
    else:
            str3=("Host is down")
            strings = [str1, str3]
            result = ', '.join(strings)
            return result

def check_internet_con():
    IP = "8.8.8.8"
    response = os.system("ping -c 4 -w 10 " + IP + " >/dev/null")

    if response == 0:
        print("Host is up")
    else:
            print("Host is down")

