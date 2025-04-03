class Polynomial:
    def __init__(self,coef):
        self.coef=coef

    def __str__(self):
        if self.coef[0]!=0:
            m=str(self.coef[0])+signe(self.coef[1])
        else:
            m=signe(self.coef[1])
        for i in range(1,len(self.coef)-1):
            if self.coef[i]==0:
                continue
            else:
                m+=str(abs(self.coef[i]))+'*X^'+str(i)+signe(self.coef[i+1])
        return m+str(self.coef[len(self.coef)-1])+'*X^'+str(len(self.coef)-1)


    def __add__(self,P2):
        Q=[0]*(min(len(self.coef),len(P2.coef)))
        for i in range(min(len(self.coef),len(P2.coef))):
            Q[i]=self.coef[i]+P2.coef[i]
        if len(self.coef)>=len(P2.coef):
            return Polynomial(Q+self.coef[(len(self.coef)-len(P2.coef))+1:])
        elif len(self.coef)<=len(P2.coef):
            return Polynomial(Q+P2.coef[(len(P2.coef)-len(self.coef))+1:])
        else:
            return Polynomial(Q)


def signe(x):
    if x<0:
        return "-"
    else:
        return "+"

# if __name__ == '__main__':
#     P1=Polynomial([1,2,3,4,5])
#     P2=Polynomial([1,2,3,4,5,5,67,8,3])
#     P3=P1.add(P2)
#     assert P1.add(P2).coef==P3.coef


