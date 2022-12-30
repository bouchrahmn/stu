import numpy as np
from numpy import *
import sys

def decomp_Lower_up(a,b,n):
  
  l=eye(n)
  u=copy(a)
  for i in range(0,n):
      p=u[i][i]
      for j in range (i+1,n):
         l[j][i]=u[j][i]/p
         u[j]=u[j]-l[j][i]*u[i]

  print("l \n",l)
  print("u \n",u)


  y=zeros(n,float) 
  y[0]=b[0]/l[0,0] 
  for i in range(1,n):
    y[i]=b[i]
    for j in range(0,i):
        y[i]=y[i]-(l[i,j]*y[j])
    y[i]=y[i]/l[i,i]
  print("y=",y)


  x=zeros(n,float)
  x[n-1]=y[n-1]/u[n-1,n-1]
  for i in range(n-2,-1,-1):
     s=0
     for j in range(i+1,n,1):
        s=s+(u[i, j]*x[j])
     x[i]=((y[i]-s)/u[i,i])    
  print("les x sont  ",x)




def gaussjor(a,n):
 np.shape(a)[0]

 for i in range(n):
    for j in range (n):
        a[i,:]=a[i,:]/a[i,i]
        if(i!=j):
            f=a[j,i]/a[i,i]
            for k in range(0,n+1):
                a[j,k]=a[j,k]-f*a[i,k]

 print("matrice identite est =",a)
 x=a[:,n]
 print("le vecteur x est=",x)

 


def gauss1(a,n):

 for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('error!') #devision sur zero
        
    for j in range(i+1, n):
        factor = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - factor * a[i][k]
 print("a=",a)


 # Back Substitution
 x[n-1] = a[n-1][n]/a[n-1][n-1]
 for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

 # afficher la solution X
 print('\nles X sont: ')
 for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')

#--------------main-------------
n = int(input('donner le nombre des x: '))
a = np.zeros((n,n+1))
x = np.zeros(n)
b = np.zeros((n,1))

#remplir la fonction A avec vecteur b
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
    b[i]=a[i,n]  
#afficher la matrice a et vecteur b
print("b",b)
print("a=",a)

#choisir la methode de resolution
nbr = int(input('donner le nomero de la methode: '))
print("1-gauss\n")
print("2-gauss jordan\n")
print("3-decomposition LU\n ")

#gaussjordan
if (nbr==2):  
 print('\n methode de gausse jordan\n')
 a=gaussjor(a,n)

#gauss
elif (nbr==1):
 a=gauss1(a,n)

#decompositin LU
elif(nbr==3):
 print('\n decomposition lu \n')
 a=decomp_Lower_up(a,b,n)


