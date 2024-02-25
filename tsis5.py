import re
f = open("row.txt", "a")
f.write("absb0guga0ab")
f.close()


t= open("row.txt", "r")
for x in t:
  for i in range(len(x) - 1):
     if 'ab' in x or 'a0' in x:
        print(x)





t = open("row.txt").read()
print(t)
m = re.findall(r'ab*', t)
print(m)




te= "ddvw_evkeok"
mat = re.findall(r"\b[a-z]+_[a-z]+\b", te)
print(mat)



tex= "Nnjnjk"
matv = re.findall(r'\b[A-Z][a-z]+\b', tex)
print(matv)





tex= "agndgdvb"
matv = re.findall(r'a.*b$', tex)
print(matv)


tex= "agndg dvb"
matv = re.sub(r'[ ,.]', ':', tex)
print(matv)





tex= "AnsnsAscds"
matv =re.findall('[A-Z][^A-Z]*', tex)
print(matv)




tex= "AnsnsAscds"
matv =re.sub(r'([a-z])([A-Z])', r'\1 \2', tex)
print(matv)


































