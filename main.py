import numpy as np 
import function_chiffre  as fc
import function_dechiffre as fdc
import fchcl as fcl
import fdcl as fdl
from parity import codeParity, strtoBinary

#_____________MAIN__________________
# first make letter list as numbers
def crmenu():
    print("___________MENU______________")
    print("--1--> Normal")
    print("--2--> Colomn")
    print("--0--> exit")
    choise = input('enter your choise :')
    return choise

def nmenu():
    print('-------------Normal Mode-------------')
    print("----3--> encrypt")
    print("----4--> decrypt")
    print("----9--> back")
    print("----0--> exit")
    choise = input('enter your choise :')
    return choise

def clmenu(): 
    print('-------------Colomn Mode-------------')
    print("----5--> encryptcl")
    print("----6--> decryptcl")
    print("----9--> back")
    print("----0--> exit")
    choise = input('enter your choise (cl):')
    return choise   
    

def lire_key():
    rslt_lire_key = ''
    while (rslt_lire_key==''):
        rslt_lire_key = input("enter your key :") 
    return rslt_lire_key


choise = '1'
while (choise != '0'):
    choise = crmenu()
    if(choise == '1'):
        #normal partie
        while (choise != '0'):
            choise = nmenu()
            if (choise == '3'):
                key = lire_key()
                fc.cripter(np.arange(0,256),key)
            elif (choise == '4'):
                key = input('enter your key :')
                reslt = fdc.decrypter(np.arange(0,256),key)
                rslt_bin = strtoBinary(reslt)
                text_parity = codeParity(rslt_bin)
                print('clear text =',reslt)
                print('bin :',rslt_bin)
                print('parity :',text_parity)
            elif (choise == '9'):
                print('**** Back To Global Menu ****\n')
                break
            else:
                print("********** invalide choise *********\n")
        #end normal while    
        
    elif(choise == '2'):
        #colomn partie
        while (choise != '0'):
            choise = clmenu()
            if (choise == '5'):
                key = lire_key()
                fcl.cripter(np.arange(0,256),key)
            elif (choise == '6'):
                key = input('enter your key :') 
                reslt = fdl.decrypter(np.arange(0,256),key)
                rslte_bin = strtoBinary(reslt)
                text_parity = codeParity(rslte_bin)
                print('clear text =',reslt)
                print('bin :',rslte_bin)
                print('parity :',text_parity)
            elif (choise == '9'):
                print('**** Back To Global Menu ****\n')
                break
            else:
                print("********** invalide choise *********\n")
        #end colomn while    

    elif (choise == '0'):
        print('end program')
        break        
    else:
        print("********** invalide choise *********")
