import zipfile
import itertools
import string
from threading import Thread


def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print("Password is " + pwd)
    except:
        pass
zipfile = zipfile.ZipFile("/home/jan/Python_Teste/Hello_world2.zip")
myLetters = string.ascii_letters + string.digits + string.punctuation

for i in range(1, 4):
    for j in map(" ".join, itertools.product(myLetters,repeat=i)):
        t = Thread(target=crack, args=(zipfile, j))
        t.start()
        t.join()