#!/usr/bin/python3
import sys
print("\n***___Welcome To NHXHide___***\n\n\n")
if len(sys.argv) != 2:
    print("Usage: NHXHide <image file name>")
    exit(-1)
response = input("Choose from the menu:\n\n(E)xtract existing data\n(P)enetrate new data\n(R)emove existing data\n(Any) other letter to quit\n\n: \t")
if response == "E" or response == "e":
    try:
        image = open(sys.argv[1], "rb")
    except FileNotFoundError:
        print("Error: The file you specified was not found.")
        exit(-1)
    contents = image.read()
    image.close()
    contents = contents[0:-128]
    try:
        data = contents.split(128*b"\x00")[1]
    except IndexError:
        print("No data found.")
        exit(-2)
    print("Your data:\t" + data.decode("ascii"))
    exit(0)
elif response == "P" or response == "p":
    try:
        image = open(sys.argv[1], "rb")
    except FileNotFoundError:
        print("Error: The file you specified was not found.")
        exit(-1)
    data = input("Type data to be infiltrated:\t")
    contents = image.read()
    image.close()
    check = len(contents.split(128*b"\x00"))
    if check > 1:
        print("Infiltration not possible while already having data.")
        exit(-3)
    contents = contents + 128*b"\x00" + data.encode("ascii") + 128*b"\x0f"
    image = open(sys.argv[1], "wb")
    image.write(contents)
    image.close()
    print("Data infiltrated successfully.")
    exit(0)
elif response == "R" or response == "r":
    try:
        image = open(sys.argv[1], "rb")
    except FileNotFoundError:
        print("Error: The file you specified was not found.")
        exit(-1)
    contents = image.read()
    image.close()
    data = contents.split(128*b"\x00")
    image = open(sys.argv[1], "wb")
    image.write(data[0])
    image.close()
    print("Data removed Successfully.")
    exit(0)
else:
    print("Exitting...")
    exit(0)
