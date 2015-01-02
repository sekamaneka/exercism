

def board(what):
    return(rec(what,1,1))


def rec(matrix,x,y):
    
    if x<len(matrix[0])-1:
        return (matrix,x+1,y)
        if y<len(matrix)-1:
            return (matrix,x+1,y+1)
    if x>1:
        return (matrix,x-1,y)
        if y>1:
            return (matrix,x-1,y-1)
    if y<len(matrix)-1:
        return (matrix,x,y+1)
        if x>1:
            return (matrix,x-1,y+1)
    if y>1:
        return (matrix,x,y-1)
        if x<len(matrix[0])-1:
            return (matrix,x+1,y-1)
    return 0


for i in board(["+------+",
               "| *  * |",
               "|  *   |",
               "|    * |",
               "|   * *|",
               "| *  * |",
               "|      |",
               "+------+"]):
    print(i)
