s = '''Programming is best regarded as the process 
of creating works of literature, which are meant to 
be read'''

resp = 'ature' in s
print(resp)

pos = s.find("ss")
if pos == -1:
    print("Nao existe 'fiap' em s")
print(pos)