import itertools
class Garden(object):
    
    list_of_names = ['Alice','Bob','Charlie','David','Eve','Fred','Ginny','Harriet','Ileana','Joseph','Kincaid','Larry']
    
    def __init__(self,planting_order):
        self.myList = [i for i in planting_order]

        self.myList.remove('\n')
        #self.planting_order.remove('\n')
        

            
    def plants(self,what):
        group_adjacent = lambda a, k: zip(*([iter(a)] * k))
        self.myList = list(group_adjacent(self.myList,2))
        self.myList = zip(self.myList[:len(self.myList)//2:],self.myList[len(self.myList)//2::])
        self.myList = list(zip(self.myList,self.list_of_names))
        
        for i in self.myList:
            for name in self.list_of_names:
                if name in i:
                    ready_to_play = i[0:len(i)-1:]
        about_to_be_returned = []     
        for i in ready_to_play:
            for j in i:
                print(i)
                #for e in j:
##                    if e == 'R':
##                        ready_to_play.append('Radishes')
##                    if e == 'C':
##                        ready_to_play.append('Clover')
##                    if e == 'V':
##                        ready_to_play.append('Violets')
##                    if e == 'G':
##                        ready_to_play.append('Grass')
        return about_to_be_returned

            
        return 0


    
