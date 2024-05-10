class RestaurantTable:
    menus={
        'pizza': 5000,
        'cola': 600,
        'apple juice' : 3000,
        'hamburger': 6000,
        'fried potatoes' : 2000,
    }

    def __init__(self):
        self.total = 0
        self.orders = []

    def addOrder(self, order):
        self.orders.append(order)
        self.total += self.menus[order]

    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menus[order]}')

        print(f'total price is {self.total}')

def startProgram():
    table= RestaurantTable()
    while True:
        order= input('Add order:')
        table.addOrder(order)
        another = input('Order again ? y/n: ')
        
        if another == 'y':
            continue
        if another == 'n':
            table.printBill()
            break
        else: 
            break


startProgram()