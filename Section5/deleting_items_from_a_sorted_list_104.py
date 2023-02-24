# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191]
# data = [104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# data = [104,105,110,120,130,130,150,160,170,183,185,187,188,191]
# data = [1041,1051,1101,1201,1301,1301,1501,1601,1701,1851,1871,1881,1911]
data = []


min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop) # for debug
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1): # (a) len(data)-1, (b) -1 from list end, (c) step -1
    if data[index] <= max_valid:
        # We have the index of the last item to keep
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break

print(start) # for debug
del data[start:]
print(data)

print('-' * 30)


data_2 = [3,5,12,21,45,67,121,345,401]
for index in range(len(data_2) - 1, -1, -2):
    print(data_2[index], end =" ")
    # print(index)