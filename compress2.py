from bitstring import BitArray, BitStream
import math

data = open("file", "rb")
print(data)
bitstring = BitArray(data)
print(bitstring)
print(bitstring.bin)


list = [""]

x = BitArray()
output = BitArray()
c = BitArray()

#x = bitstring.bin[0]
output = bitstring.bin[0]
c = bitstring.bin[0]

index = 0
i = 0

newloop = False
y_list = False

while index < len(bitstring):
    if newloop == False:
        x = bitstring.bin[index]
    else:
        x += bitstring.bin[index]
        newloop = False
    
    print("\nXXXXXX:" + str(x))
    print("index:" + str(index))
    for elem in list:
        if elem == x:
            newloop = True
            break
    
    if newloop == False:
        if len(str(x)) == 1:
            y = ""
            b = x
        else:
            y = x[0:len(x)-1]
            print("Y:" + str(y))
            b = x[-1:]
            print("B:" + str(b))
        
        for elem in list:
            if elem == y:
                y_list = True
                i = list.index(elem)
                break

        if y_list == True:
            binary_i = "{0:b}".format(i)
            print("binary:" + str(binary_i))
            if len(binary_i) < math.log(len(list),2):
                count = 0
                while count < math.log(len(list),2)-1:
                    c += '0'
                    count += 1
            
            c += "{0:b}".format(i)
            c += b
            print(c)
            c = c[1:len(c)]
            print("c:" + str(c))
            
        output += c

        list.append(x)

    index += 1
    y_list = False
    c = bitstring.bin[0]
    

output = output[1:len(output)]
print(output)

data.close()

f = open("file.lz", "w")
f.write(output)
