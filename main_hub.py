import socket
import time
IP_NAME = []
IP_DNS = []
PORT = 443
RETRY = 5
DELAY = 10
TIMEOUT = 3


def activate_now(ip, port):
    def checking_status(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        try:
            s.connect((ip, int(port)))
            s.shutdown(socket.SHUT_RDWR)
            return True
        except:
            return False
        finally:
            s.close()

    def check_host(ip, port):
        ip_up = False
        for i in range(RETRY):  # it will try this so many times
            if checking_status(ip, port):
                ip_up = True
                break
            else:
                time.sleep(DELAY)
        return ip_up

    if check_host(ip, port):
        print(ip + " === status: UP")
    if not check_host(ip, port):
        print(ip + " === status: Down")

def start_program():
    focus_list = []

    try:
        with open('apples.txt') as opened_file:
            read_file = opened_file.read()
            rr = read_file.split("\n")
            for i in rr:
                ss = i.split(" ")
                focus_list.append(ss)

    except FileNotFoundError:
        print("file not found!!!!")

    print(focus_list)

    # oceans = ["apples", "and", "oranges", "are", "fruit"]
    # with open('oranges.txt', 'w') as f:  # a will append, w will write
    #     for ocean in oceans:
    #         f.write(ocean)
    #         f.write("\n")

    for i in focus_list:
        print(f"#----------- {i}")
        host = i[0]
        port = i[1]
        activate_now(host, port)


start_program()

"""
#!/usr/bin/python
import socket
import time
ip = "google.com"
port = 443
retry = 5
delay = 10
timeout = 3
def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()
def checkHost(ip, port):
        ipup = False
        for i in range(retry):
                if isOpen(ip, port):
                        ipup = True
                        break
                else:
                        time.sleep(delay)
        return ipup
if checkHost(ip, port):
        print ip + " is UP"


-----------------
read a file in
10.0.0.1:22
10.0.0.1:25
10.0.0.1:80
10.0.0.2:80
does the code
outputs 2 files. open and closed ports
"""