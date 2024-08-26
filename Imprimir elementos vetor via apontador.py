import copy
def copiar(lst_tpl):
    lista=[]
    for item in lst_tpl:lista.append(item)
    return lista

lista=[1,2,[3]]
aux=lista
aux[2]=-1
print("Lista: lista=%s" %lista)

lista=[1,2,[3]]
print("Lista: lista=%s" %lista)
aux1=copy.copy(lista)
aux2=list(lista)
aux3=copiar(lista)

aux1[2]=-1
aux2[2]=-1
aux3[2]=-1
print("aux1=%s, lista=%s" %(aux1, lista))
print("aux2=%s, lista=%s" %(aux2, lista))
print("aux3=%s, lista=%s" %(aux3, lista))

tupla=[1,2,[3]]
print("Tupla: tupla=%s" %tupla)
aux1=copy.copy(tupla)
aux2=list(tupla)
aux3=copiar(tupla)
print("aux1=%s, tupla=%s" %(aux1, tupla))
print("aux2=%s, tupla=%s" %(aux2, tupla))
print("aux3=%s, tupla=%s" %(aux3, tupla))