string="0123456789abcdefghijklmnopq"
print("\Imprime caracteres e ses códigos ")
for char in string:
    print("%10c: %3d"%(char,ord(char)))
print()

print("Digite uma frase e tecle Enter")
string=input()
print("Foi digitada uma frase com %d caracteres: %s"%(len(string),string))