

class Stack(object):
    #Initialize the stack for a null list
    def __init__(self):
        self.items=[]


    # Return A True If The Stack Is Null Otherwise Return A False
    def is_Empty(self):
        return self.items==[]



    #Return the size of the stack
    def size(self):
        return len(self.items);


    #Return The Top
    #Retrun The value "None" If The Stack Is Null
    def peek(self):
        if self.is_Empty():
            return None
        return self.items[len(self.items)-1]
        #Or call method size
        #return self.items[self.size() -1]



    #Push new values into the stack
    def push(self,item):
        self.items.append(item)


    #Pop the values out of the stack
    def pop(self):
        return  self.items.pop()


