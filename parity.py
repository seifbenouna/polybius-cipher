def strtoBinary(aList):
    return  ' '.join(format(ord(x), 'b') for x in aList) 
#end strtoBinary
          
# def intToBinary(aList):
#     return ' '.join(format(x, 'b') for x in aList)
# #end intToBinary

def codeParity(aStr):
    cop = (aStr.count("1"))%2
    if ( cop == 0 ):
        # print("code parity = 0")
        return 0
    else:
        # print("code parity = 1")
        return 1
#end code parity
