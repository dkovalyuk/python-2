
# https://docs.python.org/3/library/datetime.html#date-objects
# https://docs.python.org/3/howto/sorting.html
# https://stackoverflow.com/questions/10052912/how-to-sort-dictionaries-of-objects-by-attribute-value
# https://tproger.ru/translations/python-sorting/

#https://www.webucator.com/article/maximum-recursion-depth-exceeded-while-calling-a-p/


from collections import UserDict
import datetime
import operator

#Товар
class Product:
    article_id = 0
    name = ''
    _price = 0.0

    def set_price(self, price_value):
        if price_value > 0:
            self._price = float(price_value)
        else:
            print('error negative price')
    
    def format_price(self):
        return '{:.2f} грн.'.format(self._price)

    price = property(format_price, set_price)    


#Продукт з терміном придатності
class FoodProduct(Product):
    expiration_date = None

    def __init__(self, good_id, good_name, good_price):
        self.article_id = good_id
        self.name = good_name
        self.price = good_price

    def __repr__(self) -> str:
        return "|{:^5}|{:<40}|{:>15}|{:>15}|".format(self.article_id, self.name, self.price, self.exp_date)    


    @property
    def exp_date(self):
        return self.expiration_date.strftime('%d.%m.%Y') 

    
    @exp_date.setter
    def exp_date(self, new_date):
        #date_str = '10.12.2017' # The date - 29 Dec 2017
        #format_str = '%d.%m.%Y' # The format
        #datetime_obj = datetime.datetime.strptime(date_str, format_str)
        self.expiration_date = datetime.datetime.strptime(new_date, "%d.%m.%Y")


#Товари в магазині
class Assortment(UserDict):
    SORT_BY_NAME = 1
    SORT_BY_PRICE = 2
    SORT_BY_DATE = 3


    #зчитуємо товари з файлу
    def load_goods(self, filename = ''):
        if not filename:
            good = FoodProduct(1, 'milk', 28)
            good.exp_date = '10.02.2022'
            self.data[good.article_id] = good

            good = FoodProduct(3, 'coffe', 198)
            good.exp_date = '01.08.2023'
            self.data[good.article_id] = good

            good = FoodProduct(5, 'sugar', 20)
            good.exp_date = '02.06.2022'
            self.data[good.article_id] = good
        else:
            #load from file
            pass


    #отримати товар по ID
    def get_good_by_id(self, good_id):
        if good_id in self.data.keys():
            return self.data[good_id]
        else:
            return None


    #відсортувати товари                  
    def sort_goods(self, order_id):
        if(order_id == self.SORT_BY_NAME): 
            for good in sorted(self.data.values(), key=operator.attrgetter('name')):
                print(good)    
            
        if(order_id == self.SORT_BY_PRICE):
            for good in sorted(self.data.values(), key=operator.attrgetter('_price')):
                print(good) 
        
        
        if(order_id == self.SORT_BY_DATE): 
            for good in sorted(self.data.values(), key=operator.attrgetter('expiration_date')):
                print(good) 


#Товари в корзині користувача
class Basket(UserDict):
    def add_good(self, good_id, quantity):
        if good_id in self.data.keys():
            self.data[good_id] += quantity
        else:
            self.data[good_id] = quantity


#Менеджер меню 
class UI:
    def print_menu(self):
        menu = '''Оберіть команду:
        1 - перегляд товарів в магазині
        2 - перегляд товарів в кошику
        3 - додати товар в кошик
        4 - оплатита  
        0 - закінчити роботу'''
        print(menu)


    def do_action(self):
        user_basket = Basket()

        goods_in_shop = Assortment()
        goods_in_shop.load_goods()

        self.print_menu()
        while True :
            menu_number = int(input())

            #match... але не у всіх 3.10
            if(menu_number == 0):
                print('Good Buy')
                break  

            elif (menu_number == 1):
                print('sort by: 1-title | 2-price | 3-date')
                order_id = int(input())
                goods_in_shop.sort_goods(order_id)
                print()

            elif (menu_number == 2):
                print('Googs in busket')
                for good_id, good_count in user_basket.items():
                    print(goods_in_shop[good_id].name, good_count)
                print()
    
            elif (menu_number == 3):
                print('Enter goods article and count, example 1 4')
                good_id, goods_count = input().split()
                user_basket.add_good(int(good_id), int(goods_count))
                print('Good Added')
                print()
    
            elif (menu_number == 4):
                print('Your receipt')

                for good_id, good_count in user_basket.items():
                    good = goods_in_shop.get_good_by_id(good_id)
                    good_sum = good._price * good_count
                    print("{:<40} {:>15} X {:>15} = {:>15}|".format( good.name, good.price,  good_count, good_sum)) 


ui_manager = UI()
ui_manager.do_action()