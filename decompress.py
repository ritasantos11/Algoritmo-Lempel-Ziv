from bitstring import BitArray
import math, sys

data = open(sys.argv[1], "rb")
print(data)
bitstring = BitArray(data)
print(bitstring)
print(bitstring.bin)


x = BitArray()
output = BitArray()
c = BitArray()
y = BitArray()


list = {0 : ""}

list_index = 1
read_index = 0
index = 0
i = 0

while index < len(bitstring):
        print("INDEX:" + str(index))
        if len(list) == 1:
            c.append(bitstring[0:1])
            x.append(c)
            index += 1

        else:
            while read_index < math.ceil(math.log(len(list),2)):
                print("ola")
                c.append(bitstring[index:index+1])
                read_index += 1
                index += 1
            
            if len(c) == 1:
                print("len(c)=1")
                y = ""
                b = c
            else:
                i = c[0:len(c)]
                b = c[-1:]
                int_i = i.uint
                print(int_i)
                print(list.get(int_i))
                y.append(list.get(int_i))
                #print(y)
                #x.append(y.bin)

            x.append(b)

        list[list_index] = x.bin
    
        list_index += 1
        #index += 1
        read_index = 0
        c = BitArray()
        x = BitArray()
        y = BitArray()

