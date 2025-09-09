import pandas as pd

class Inventory_Management:
    #To create a Dataframe file with columns as below
    def __init__(self):
        self.inventory = pd.DataFrame(columns=['Product ID','Name','Price','Quantity'])

    #To save the Dataframe as a CSV File
    def Save_to_CSV(self):
        self.inventory.to_csv('Inventory.csv',index = False)

    #To add New products to the DataFrame/ CSV File
    def Add_Products(self,prod_dict):
        self.new_prod = pd.DataFrame(prod_dict)
        self.inventory = pd.concat([self.inventory,self.new_prod],axis = 0,ignore_index = False) 


    #To Remove a product from DataFrame/CSV file By Product ID
    def Rem_Prod(self,prod):
        if prod not in self.inventory['Product ID'].values:
            print(f"{prod} not found in inventory!!")
            return

        self.inventory = self.inventory[self.inventory['Product ID'].values != prod]
    

    #To check if a product is available or not By product ID
    def is_available(self,prod):
        if prod in self.inventory['Product ID'].values:
            return True
        return False    
    

    #To print CSV File using Print() function
    def __str__(self):
        return f"{pd.read_csv('Inventory.csv')}"


if __name__ == '__main__':
    Obj1 = Inventory_Management()
    Obj1.Save_to_CSV()
    products = {'Name': ['Laptop','Mouse','Keyboard','Speakers'],
                'Price': [55000,2500,1500,4000],
                'Product ID': ['P01','P02','P03','P04'],
                'Quantity': [50,100,80,150]}
    Obj1.Add_Products(products)
    Obj1.Save_to_CSV()

    print(Obj1) 

    
    Obj1.Rem_Prod('P03')
    Obj1.Save_to_CSV()
    
    products = {'Name': ['Charger','Data Cable','Mobile','Camera'],
                'Price': [1500,499,15000,40000],
                'Product ID': ['P05','P06','P07','P08'],
                'Quantity': [124,235,62,43]}
    Obj1.Add_Products(products)
    Obj1.Save_to_CSV()
    print(Obj1) 
    print(Obj1.is_available('P03'))