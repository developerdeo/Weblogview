print('Enter name of the file:')
xl = input()
f = open(xl, "a")
f.write("Now the file has more content!")
f = open(xl, "r")
w=f.read
x = w.find("GET")
print(w)
#print(f.read())

f.close()

