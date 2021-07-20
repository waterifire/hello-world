import socket
import time
PORT = 443
RETRY = 1
DELAY = 1
TIMEOUT = 1


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
        for i in range(RETRY):
            if checking_status(ip, port):
                ip_up = True
                break
            else:
                time.sleep(DELAY)
        return ip_up

    if check_host(ip, port):
        current_status = "OK"
        return ip, port, current_status

    if not check_host(ip, port):
        current_status = "DOWN"
        return ip, port, current_status


def start_program():
    focus_list = []
    temp_list = []

    print("[STARTING]...")
    try:
        with open('apples.txt') as opened_file:
            read_file = opened_file.read()
            rr = read_file.split("\n")
            for i in rr:
                ss = i.split(" ")
                focus_list.append(ss)

    except FileNotFoundError:
        print("file not found!!!!")

    for i in focus_list:
        host = i[0]
        port = i[1]
        var1, var2, var3 = activate_now(host, port)
        temp_list.append((var1, var2, var3))

    with open('oranges.txt', 'w') as f:  # clears the file
        f.write("")

    for a in temp_list:
        with open('oranges.txt', 'a') as f:
            f.write(f"{a[0]}\t===\tport\t{a[2]}")
            f.write("\n")

    print("[COMPLETED]...")


start_program()
