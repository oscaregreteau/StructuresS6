liste=[]
f=open("frenchssaccent.dic",'r')
for ligne in f:
    liste.append(ligne[0:len(ligne)-1]

def mots(L):
    mots_possibles=[]
    k=''
    for i in L:
        for j in L:
            if i+j in liste:
                 most_possibles.append(i+j)
            else:
                 for k in L:
                    if i+j+k in liste:
                         most_possibles.append(i+j+k)
                     else:
                        for l in L:
                            if i+j+k+l in liste:
                                 most_possibles.append(i+j+k+l)
                            else:
                                 for m in L:
                                     if i+j+k+l+m in liste:
                                         most_possibles.append(i+j+k+l+m)
                                     else:
                                        for n in L:
                                            if i+j+k+l+m+n in liste:
                                                most_possibles.append(i+j+k+l+m+n)
                                            else:
                                                for o in L:
                                                    if i+j+k+l+m+n+o in liste:
                                                        most_possibles.append(i+j+k+l+m+n+o)
                                                    else:
                                                        for p in L:
                                                            if i+j+k+l+m+n+o+p in liste:
                                                                most_possibles.append(i+j+k+l+m+n+o+p)
    mots_possibles.sort
    return(mots_possibles[1])





