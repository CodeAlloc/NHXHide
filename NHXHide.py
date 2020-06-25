#!/usr/bin/python3
import sys
print("\n\t***___Welcome To NHXHide___***\n\n\n")
if len(sys.argv) < 2:
    print("\t\tUsage: NHXHide <multimedia file name> <optional:data file>")
    exit(-1)
response = input("\tChoose from the menu:\n\n\t\t(E)xtract existing data\n\t\t(P)enetrate new data\n\t\t(R)emove existing data\n\t\t(Any) other letter to quit\n\n: \t")
if response == "E" or response == "e":
    try:
        image = open(sys.argv[1], "rb")
    except FileNotFoundError:
        print("Error: The multimedia file you specified was not found.")
        exit(-1)
    contents = image.read()
    image.close()
    contents = contents[0:-512]
    try:
        data = contents.split(1024*b"\x0f")[1]
    except IndexError:
        print("No data found.")
        exit(-2)
    if len(sys.argv) > 2:
        towrite = open(sys.argv[2], "w+b")
        towrite.write(data)
        towrite.close()
        print("Data written to the file successfully.")
    else:
        print("Your Data:\t" + data.decode("ascii"))
        exit(0)
elif response == "P" or response == "p":
    try:
        image = open(sys.argv[1], "rb")
    except FileNotFoundError:
        print("Error: The multimedia file you specified was not found.")
        exit(-1)
    if len(sys.argv) < 3:
        data = input("Type data to be penetrated:\t")
        data = data.encode("ascii")
    else:
        try:
            toread = open(sys.argv[2], "rb")
        except FileNotFoundError:
            print("Error: The file to read data from was not found.")
            exit(-1)
        data = toread.read()
        toread.close()
    contents = image.read()
    image.close()
    check = len(contents.split(1024*b"\x0f"))
    if check > 1:
        print("Penetration not possible while already having data.")
        exit(-3)
    contents = contents + 1024*b"\x0f" + data + 512*b"\x0f"
    image = open(sys.argv[1], "wb")
    image.write(contents)
    image.close()
    print("Data infiltrated successfully.")
    exit(0)
elif response == "R" or response == "r":
    try:
        image = open(sys.argv[1], "rb")
    except FileNotFoundError:
        print("Error: The multimedia file you specified was not found.")
        exit(-1)
    contents = image.read()
    image.close()
    data = contents.split(1024*b"\x0f")
    image = open(sys.argv[1], "wb")
    image.write(data[0])
    image.close()
    print("Data removed Successfully.")
    exit(0)
else:
    print("Exitting...")
    exit(0)
