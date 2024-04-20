"""
Mine puzzle program
"""

def validate_board(board:list)->bool:
    """"
    list->bool
    Checks a list with puzzle game and
    says if it is correct
    """
    for line in board:
        lst=[]
        for symb in line:
            if symb!=' ' and symb!="*":
                if symb in lst:
                    return False
                else:
                    lst.append(symb)
    for ind in range(len(board)):
        lst0=[]
        for line1 in board:
            if line1[ind]!=' ' and line1[ind]!="*":
                if line1[ind] not in lst0:
                    lst0.append(line1[ind])
                else:
                    return False
    k=len(board)
    for chislo in range(len(board)):
        lst007=[]
        sum1=0
        for line001 in board:
            if line001[chislo]!=' ' and line001[chislo]!='*' and k-1>sum1:
                if line001[chislo] in lst007:
                    return False
                lst007.append(line001[chislo])
            elif k-1==sum1:
                for g in line001[len(board)-k:]:
                    if g!=' ' and g!='*':
                        if g in lst007:
                            return False
                        lst007.append(g)
            sum1+=1
        k-=1
    return True
