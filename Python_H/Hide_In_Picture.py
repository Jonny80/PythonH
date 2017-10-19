f = open("", encoding="ISO-8859-1",mode="r")   #schreiben mode = "a+"


#f.write("")


try:
    byte = f.read(1)
    str = ""
    while byte != "":
        str += byte
        byte = f.read(1)
    print(str)

finally:
    f.close()