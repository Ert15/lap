import os

for dirpach, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
        print('Каталоги: ', os.path.join(dirpach, dirname))
    for filename in filenames:
        print('Файлы: ', os.path.join(dirpach, filename))



        


def che(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Readable:", os.access(path, os.R_OK))
        print("Writable:", os.access(path, os.W_OK))
        print("Executable:", os.access(path, os.X_OK))
    else:
        print("not")

path = "C:/Users/15/Downloads/osdvs"
che(path)




import os

def ana(path):
    if os.path.exists(path):
        print("Path exists.")
        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("not")

pat = "C:/Users/15/Downloads/osdvs"
ana(pat)





def cou(f):
    try:
        with open(f, 'r') as file:
            l = sum(1 for line in file)
        print("Number of lines:", l)
    except FileNotFoundError:
        print("not")

text = "C:/Users/15/Downloads/osdvs"
cou(text)



def w(f, d):
    with open(f, 'w') as file:
        for x in d:
            file.write(str(x) + '\n')

list = [ 1, 2, 3, 4, 5]
o = "C:/Users/15/Downloads/osdvs"
w(o)







