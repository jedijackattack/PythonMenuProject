marketPrice = 38

class Dish(object):
    

    Dishes = []
    

    def __init__(name,price,dtype,seasonal,local):
        
        self.name = name
        self.price = price
        self.dtype = dtype
        self.seasonal = seasonal
        self.local = local
        Dishes.append(self)


    @staticmethod
    def generateDishesFromTable(tableAdd):
    """This gets the dishes from the Menu file"""
        
        with open("MenuData.txt","r") as f:
            file = f.readlines()

            for line in file:
                line = line.rstrip("\n")
                data = line.split(",")

                if(data[1] == "%"):
                    Dish(data[0],marketPrice,data[2],data[3],data[4])
                else:
                    Dish(data[0],data[1],data[2],data[3],data[4])
    
                
                

    
        
