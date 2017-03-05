import zipfile
import itertools
import string
from threading import Thread


def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print("Password is " +pwd)
    except:
        pass
zipfile = zipfile.ZipFile("/home/jan/Python_Teste/Hello_world4.zip")
myLetters = string.ascii_letters + string.digits + string.punctuation

threadlist = []
newlist = []

for i in range(1, 4):
    for j in map(" ".join, itertools.product(myLetters,repeat=i)):
        t = Thread(target=crack, args=(zipfile, j))
        t.start()
        t.join()
        threadlist.append(t)
        if len(threadlist) == 100 :
            newlist.append(threadlist)
            t.join()
            del threadlist[0:100]