'''
jabber = open("sample.txt","r")
#jabber = open("C:\\Users\\lauri\\Downloads\\sample.txt","r")

for line in jabber:
    if "jabberwock" in line.lower():
        print(line,end="")

jabber.close()
'''

'''
with open("sample.txt","r") as jabber: # closes the file
    for line in jabber:
        if "JAB" in line.upper():
            print(line,end="")
'''
'''
with open("sample.txt","r") as jabber:
    line = jabber.readline()
    while line:
        print(line,end="")
        line = jabber.readline()
'''

'''
with open("sample.txt","r") as jabber:
    lines = jabber.readlines()
print(lines,end="")

for line in lines:
    print(line,end="")
'''

'''
with open("sample.txt","r") as jabber:
    lines = jabber.readlines()
print(lines,end="")

for line in lines[::-1]:
    print(line,end="")
'''
print('*'*40)

with open("sample.txt","r") as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line,end="")


