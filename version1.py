#version1
#200 generations
#alternate ceaser cypher
#+n -n


#failure....repeats after 26 units


n = 1;
key = "password"
#for i in range(len(key)):
   # print(chr(ord(key[i])+1),end="")
to_array = [char for char in key]

w, h = 8, 200
list = [[0 for x in range(w)] for y in range(h)]
#print((key))

for i in range (0,200):
    for j in range(len(to_array)):


        if j%2 == 0:
            list[i][j] = chr((ord(to_array[j]) + i - 97) % 26 + 97)



        if j%2 != 0:
            list[i][j] = chr((ord(to_array[j]) - i + 97) % 26 + 97)


for i in range(0,200):
    print(list[i],"gen number",i)








