
n=10
vet=[]
for i in range(0,n,1):
    vet.append(10+i)
print("\nO vetor:",end="")
print(vet)

print("\nNovamente o vetor impresso em 2 modos:")
i=0
for item in vet:
    print("(%2d, %2d)"%(item,vet[i]),end="")
    i+=1
print()