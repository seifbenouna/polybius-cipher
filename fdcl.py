import function_chiffre as fc
def decrypter(mtable,key):
    
    table = fc.recreate_table(mtable,key)
    text_chiffre = fc.lire()
    list_txt_chiffre = list(text_chiffre.split(' '))

    text_new =''
    for i in range(0,len(list_txt_chiffre)-1,2):
        di=int(list_txt_chiffre[i+1])
        dj=int(list_txt_chiffre[i])
        text_new+=chr(table[di][dj])+""
    return text_new   