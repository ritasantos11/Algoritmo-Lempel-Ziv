from bitstring import BitArray
import math, sys



data = open(sys.argv[1], "rb")
#print(data)
complete_bitstring = BitArray(data)
data.close()
#print(complete_bitstring)
#print(complete_bitstring.bin)


# nº de bits onde a seguir se acrescentou 8-num 0s para fzr 1 byte
num = int(complete_bitstring[-8:].bin, 2)
del(complete_bitstring[-8:])
if num != 0:
    del(complete_bitstring[-(8-num):])


# nº de bits que se codificou c o codigo da repeticao * 3 em binario
num_bits_binary = complete_bitstring[-8:]
# nº de bits que se codificou c o codigo da repeticao * 3
num_bits = int(num_bits_binary.bin, 2)

if num_bits != 0:
    bitstring = complete_bitstring[0:len(complete_bitstring)-(num_bits+8)]
    print(bitstring.bin)

    # vai conter os num_bits bits que se codificou c o codigo da repeticao
    r_bitstring = complete_bitstring[len(complete_bitstring)-(num_bits+8):len(complete_bitstring)-8]
    print(r_bitstring.bin)


x = BitArray()
y = BitArray()
i = BitArray()
output = BitArray()


list = {0 : ""}

list_index = 1
read_index = 0
index = 0

y_list = False

while index < len(bitstring):
        if len(list) == 1:
            x.append(bitstring[0:1])
            index += 1

        else:
            while read_index < math.ceil(math.log(len(list),2)):
                i.append(bitstring[index:index+1])
                read_index += 1
                index += 1
            
            b = bitstring[index:index+1]
            index += 1
            int_i = i.uint

            if int_i in list:
                a = list.get(int_i)
                y.append(a)
                y_list = True

            
            if y_list == True:
                x.append(y)

            x.append(b)

        list[list_index] = x
        output.append(x)
        
        list_index += 1
        read_index = 0

        i = BitArray()
        x = BitArray()
        y = BitArray()

        y_list = False


index = 0
while index < len(r_bitstring.bin):
    if r_bitstring.bin[index:index+1] == '0':
        output.append('0b0')
        index += 3
    else:
        output.append('0b1')
        index += 3


#print(output)
#print(output.bin)
#print(len(output.bin)%8)

output_bytes = []
for byte in output.cut(8):
    output_bytes.append(byte.hex)


output_file = open(sys.argv[2], "wb")
output_file.write(bytearray(int(i,16) for i in output_bytes))
output_file.close()

