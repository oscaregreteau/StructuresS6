liste=[]
f=open("/Users/oscar/Etudes/Ecole/S6/StructuresS6/Seance 1/frenchssaccent.dic",'r')
for ligne in f:
    liste.append(str(ligne[0:len(ligne)-1]))
f.close()
# print(liste)
def mots(M):
    L=M
    k=''
    m=0
    mots_possibles=['saccre','abaca','aberre']
    # for j in liste:
    #     if set(list(j))<=set(L):
    #         mots_possibles.append(j)
    for mot in mots_possibles:
        print(mot)
        k=list(mot)
        m=list(mot)
        L=M
        for i in range(len(k)):
            print(k[i])
            if k[i] in L and k!=[]:
                L.remove(k[i])
                k.remove(k[i])
        if k!=[]:
            mots_possibles.remove(mot)
        k=[]
    return mots_possibles
