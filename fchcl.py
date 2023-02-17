import function_chiffre as fc
from parity import codeParity,strtoBinary

def cripter(ntable,key):
    
    table = fc.recreate_table(ntable,key) 
    # then star cipher
    text_clair = fc.lire()
    text_clair_list = list(set(text_clair.strip(" ")))
    text_clair_list.sort()
    print('-------------------------------')

    #get index of letters
    list_xy = []
    get_index(table,text_clair_list,list_xy)

    #remplace les lettre par index of letter
    text_chiffre = fc.remplace_index_in_text(text_clair,text_clair_list,list_xy)
    print('-------------------------')
    print("cipher text =",text_chiffre)
    rst_bin = strtoBinary(text_clair)
    text_bin = codeParity(rst_bin)
    print('bin :',rst_bin)
    print(f"code parite clair text :{text_bin}")
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
                list_xy.append([list(table[j]).index(i),j])  
                break
            except:
                continue            
#end get_indexx    
