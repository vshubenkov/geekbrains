class ErrortoAddItemtoStorage(Exception):
    def __init__(self, txt):
        self.txt = txt

class Department:
    pass

class Storage:
    def __init__(self, name):
        self.name = name
        self.storage_dictionary = {}
        self.count_items = 0
        self.item_id = 0

    def add_item_to_storage(self, item):
        '''
        :param item: Object (New Scanner or Printer)
        :return:
        '''
        #Check Item already exist in storage (paramenter for checking is serial id of item)
        try:
            for key, value in self.storage_dictionary.items():
                if value.serial == item.serial and value.category == item.category:
                    raise ErrortoAddItemtoStorage("Item with this serial is already in storage" + str(item.__dict__))
                else:
                    continue
        except ErrortoAddItemtoStorage as err:
            print(err)
        else:
            self.item_id += 1
            self.count_items += 1
            self.storage_dictionary[self.item_id] = item


    def print_storage(self):
         for key, value in self.storage_dictionary.items():
             print(key, value.__dict__)


class ToolsParent:

    count_items = 0

    def __init__(self, width, height, mass, color):
        self.width = width
        self.hight = height
        self.mass = mass
        self.color = color

    def pass_item_to_storage(self, storage):
        storage.add_item_to_storage(self)


class Printer(ToolsParent):

    def __init__(self, width, height, mass, color, printer_type, firm, serial):
        super().__init__(width, height, mass, color)
        self.type = printer_type
        self.firm = firm
        self.serial = serial
        self.category = 'Printers'
        Printer.count_items += 1


class Scanner(ToolsParent):
    def __init__(self, width, height, mass, color, firm, serial):
        super().__init__(width, height, mass, color)
        self.firm = firm
        self.serial = serial
        self.category = 'Scanners'
        Scanner.count_items += 1


objStorage = Storage('North')

objPrinter_1 = Printer(30, 30, 5, 'red', 'laser', 'Cannon', '#1')
objPrinter_2 = Printer(40, 20, 4, 'red', 'jet', 'Dell', '#2')
objPrinter_3 = Printer(30, 30, 5, 'red', 'laser', 'Cannon', '#2')

objScanner_1 = Scanner(20, 20, 2, 'black', 'Xerox', '#1')
objScanner_2 = Scanner(10, 10, 1, 'blue', 'Cannon', '#2')
objScanner_3 = Scanner(25, 15, 5, 'grey', 'HP', '#3')


objPrinter_1.pass_item_to_storage(objStorage)
objPrinter_2.pass_item_to_storage(objStorage)

objPrinter_1.pass_item_to_storage(objStorage) #Try to add the same object
objPrinter_3.pass_item_to_storage(objStorage) #Try to add the object with an already existing serial

objScanner_1.pass_item_to_storage(objStorage)
objScanner_2.pass_item_to_storage(objStorage)
objScanner_3.pass_item_to_storage(objStorage)

objStorage.print_storage()

print('Scanner.count_items =', Scanner.count_items)
print('Printer.count_items =', Printer.count_items)

