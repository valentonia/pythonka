
file = open("C:/Users/Asus/Downloads/pythonka/input.txt","r")
l = []
while True:
    line = file.readline()
    if len(line) == 0:
        break
    l.append(line)
file.close()

outfile = open("C:/Users/Asus/Downloads/pythonka/output.txt","w")
for lin in l:
    outfile.write(lin.capitalize())
file.close()
    

