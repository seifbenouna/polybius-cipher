import numpy as np
import function_chiffre as fc
from parity import codeParity, strtoBinary
def recreate_table(table,key):
    # then transform string to number for store in list
    list_key =fc.nlister(key)
    
    # order the list of key
    list_key_concate = list(dict.fromkeys(fc.nlister(key))) 
    list_key = list(dict.fromkeys(list_key))
    list_key.sort()    
    
    # then delete key from table
    for i in  range(len(list_key)-1,-1,-1):
        table = np.delete(table,list_key[i])

    # then add key in the top of the list
    table = np.concatenate((list_key_concate,table))

    # the reshape list to 2d list
    table = np.reshape(table, (16, 16))
    return table
#end    

def lire():
    rslt_lire = ''
    while (rslt_lire==''):
        rslt_lire = input("enter your text :") 
    return rslt_lire

def cripter(ntable,key):
    
    table = recreate_table(ntable,key) 
    # then star cipher
    text_clair = lire() 
    text_clair_list = list(set(text_clair.strip(" ")))
    text_clair_list.sort()
    print('-------------------------------')

    #get index of letters
    list_xy = []
    fc.get_index(table,text_clair_list,list_xy)

    #remplace les lettre par index of letter
    text_chiffre = fc.remplace_index_in_text(text_clair,text_clair_list,list_xy)
    print('-------------------------')
    print("cipher text =",text_chiffre)
    rs_bin =strtoBinary(text_clair)
    text_bin = codeParity(rs_bin)
    print('bin :',rs_bin)
    print(f"code parite text clair:{text_bin}")
    #__________FIN CRYPTER_________________

def nlister(list):
    nlist = []
    for i in list:
        nlist.append(ord(i))
    return nlist    
#end nlister

def get_index(table,listeleme,list_xy):
    listelement = nlister(listeleme)
    for i in listelement:
        for j in range(len(table)):
            try:
                list_xy.append([j,list(table[j]).index(i)])  
                break
            except:
                continue            
#end get_indexx    

def remplace_index_in_text(txt,text_clair_list,list_index):
    dictionary = dict()
    for i in range(len(list_index)):
        dictionary[text_clair_list[i]] = f'{list_index[i][0]} {list_index[i][1]} '
    transTable = txt.maketrans(dictionary)
    txt = txt.translate(transTable)
    return txt
#end   remplace_index_in_text
