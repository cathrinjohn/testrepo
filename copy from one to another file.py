with open(r"D:\data analytics files\python\h.txt", "r") as readf:
    with open("example.txt", "w")as writef:
        for line in readf:
            f=writef.write(line)
            print(f)
