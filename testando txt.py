f = open('agencia.txt', 'r')
filedata = f.read()
f.close()
print(filedata)

newdata = filedata.replace('1000', '2000')

f = open('agencia.txt','w')
f.write(newdata)
f.close()
