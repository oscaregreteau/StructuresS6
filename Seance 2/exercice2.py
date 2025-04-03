class Polyq:
    def __init__(self,coef,q,n):
        self.q=q
        self.n=n
        self.coef=coef[:]
        for k in range(len(coef)):
            for j in range(1,int(((len(coef)-1)-k)/n)+1):
                coef[k]+=((-1)**(j))*coef[k+j*n]
        for j in range(n,len(coef)):
            coef[j]=0
        self.coef = [c%q for c in coef]


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


    def signe(x):
        if x<0:
            return "-"
        else:
            return "+"


    def scalar(c,P):
        for i in range(len(P.coef)):
            P.coef[i]=c*P.coef[i]
        return P

    def rescale(self,r):
        Q=self.coef
        for i in range(len(Q)):
            Q[i]=Q[i]%r
        return Polyq(Q)

    def __add__(self,P2):
        Q=[0]*(min(len(self.coef),len(P2.coef)))
        for i in range(min(len(self.coef),len(P2.coef))):
            Q[i]=self.coef[i]+P2.coef[i]
        if len(self.coef)>=len(P2.coef):
            return Polyq(Q+self.coef[(len(self.coef)-len(P2.coef))+1:],self.q,self.n)
        elif len(self.coef)<=len(P2.coef):
            return Polyq(Q+P2.coef[(len(P2.coef)-len(self.coef))+1:],self.q,self.n)
        else:
            return Polyq(Q,self.q,self.n)


    def __mul__(self,P):
        Q=[0]*len(self.coef)
        for i in range(len(self.coef)):
            for k in range(i):
                Q[i]+=self.coef[k]*self.coef[i-k]
        return Polyq(Q,self.n,self.q)

    def karatsuba(self,P):
