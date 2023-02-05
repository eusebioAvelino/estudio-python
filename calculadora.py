
#=======================#Calcular numero primo===================

def numero_primo(x):

    inicio = 2
    controlPR = 0

    for n in range(inicio,x):
        if x % n == 0:
            controlPR +=1
            print("\n Divisores {}:  ".format(n)) 
    if controlPR  > 0 :
        
        print("\n El número {} no es primo " .format(x))
    else:
        print("\n El nÚmero {} es primo".format(x)) 
#=======================#Calcular numero primo===================
#=======================#Calcular numero par================+====

def numero_par(h):

    inicio = 2
    controlPAR = 0

    for n in range(inicio, h):
        if h % 2 == 0:
            controlPAR+=1  
    if controlPAR > 0 :

        print("\n El nÚmero {} es par"    .format(h)) 
    else:
        print("\n El número {} no es par".format(h))
#=======================#Calcular numero par=======================
#=======================#Multiplos-de un numero====================
def multiplo(j , f):
    r1=[]
    r2=[]
    valor=100
    for x in range(1,valor):
        m1=j*x
        m2=f*x
        r1.append(m1)
        r2.append(m2)
        r3=r1+r2
    n = set([i for i in r3 if r3.count(i) > 1])
    print("\n")
    print("Los multiplos de {0} y {1} = {2}".format(f,j,n)  ) 
#=======================#Multiplos-de un numero====================
#==========================#mcm mcd=================================

#===========================#mcm mcd============================

#Variables externas 
i=100
dato = 0
while(dato < i):
  
    try:
        dato=int(input("\n  introdusca el numero  {}  :  "  .format(i)))
        numero_primo(dato) 
        numero_par(dato)

        if dato % 2 == 0:
            multiplo(dato,dato-3) 
        else:
            multiplo(dato,dato-2)           
        i-=1
    except ValueError:
        print( "\n Erro Solo puede digital numero")
        




