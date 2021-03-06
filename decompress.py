from bitstring import BitArray
import math, sys


data = open(sys.argv[1], "rb")
complete_bitstring = BitArray(data)
data.close()
#print(complete_bitstring.bin)


# nº bits onde a seguir se acrescentou 8-num 0s para fazer 1 byte
num = complete_bitstring[-8:].uint
del(complete_bitstring[-8:])
if num != 0:    # apagar os 0s que se acrescentou para fazer 1 byte
    del(complete_bitstring[-(8-num):])


# nº bytes que o nº bits que sobrou do algoritmo ocupa
num_bytes = complete_bitstring[-8:].uint
num_bits = num_bytes*8

del(complete_bitstring[-8:])

# nº bits que se codificou com o codigo da repeticao em binario
num_bits_r_bitstring = complete_bitstring[-num_bits:]
# nº bits que se codificou com o codigo da repeticao
size_r_bitstring = num_bits_r_bitstring.uint * 3

if size_r_bitstring != 0:
    # bitstring vai conter os bits que se codificou pelo Lempez-Ziv
    bitstring = complete_bitstring[0:len(complete_bitstring)-(num_bits+size_r_bitstring)]

    # r_bitstring vai conter os num_bits bits que se codificou com o codigo da repeticao
    r_bitstring = complete_bitstring[len(complete_bitstring)-(num_bits+size_r_bitstring):len(complete_bitstring)-(num_bits)]



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


#print(output.bin)


output_bytes = []
for byte in output.cut(8):
    output_bytes.append(byte.uint)


output_file = open(sys.argv[2], "wb")
output_file.write(bytearray(output_bytes))
output_file.close()


