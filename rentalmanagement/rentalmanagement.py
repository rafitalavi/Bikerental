import datetime 

class BikeRental:
    def __init__(self,stock=0):

        """customer class that instances a bike rental management system
        args:
            stock
        """
        
        self.stock= stock
    def display_stock(self):
        """
        a function that display stock
        """
        print(f"{self.stock} number of bike in stock for rent.")
    
    def rent_bike_on_hourly_basis(self,n):
        """
        that rens a bike on hourly basis
        """
        if n <=0 :
            print("number of bike cannotbe equal or less then zero")
            return None
        elif n > self.stock:
            print(f"Sorry! We dont have {n} of bikes availabe.current stock: {self.stock}")
            return None
        else :
            now = datetime.datetime.now()
            print(f"You have succesfully rented {n} bikes on hourly basis at {now}")
            print("you will be charged 50tk per hour")

            self.stock -= n
            return now


    def rent_bike_on_daily_basis(self,n):
        """
        that rens a bike on hourly basis
        """
        if n <=0 :
            print("number of bike cannotbe equal or less then zero")
            return None
        elif n > self.stock:
            print(f"Sorry! We dont have {n} of bikes availabe.current stock: {self.stock}")
            return None
        else :
            now = datetime.datetime.now()
            print(f"You have succesfully rented {n} bikes on daily basis at {now}")
            print("you will be charged 500tk per day")


            self.stock -= n
            return now    
        
    def rent_bike_on_Weekly_basis(self,n):
        """
        that rens a bike on hourly basis
        """
        if n <=0 :
            print("number of bike cannotbe equal or less then zero")
            return None
        elif n > self.stock:
            print(f"Sorry! We dont have {n} of bikes availabe.current stock: {self.stock}")
            return None
        else :
            now = datetime.datetime.now()
            print(f"You have succesfully rented {n} bikes on weekly basis at {now}")
            print("you will be charged 3000tk per hour")

            self.stock -= n
            return now    
        
    def return_bike(self, request):
        """
        A function to return a rental bike
        """  
        rental_basis ,rental_time,  num_of_bike = request
        bill = 0
        if rental_time and rental_basis and num_of_bike:
            self.stock += num_of_bike
            now = datetime.datetime.now()
            rental_period = now -rental_time

            #hourly basis
            if rental_basis == 1:
                bill = round(rental_period.seconds/3600)* num_of_bike * 20

            #daily basis
            elif rental_basis == 2:
                bill = round(rental_period.days) * num_of_bike  * 500

            #weekly basis
            elif rental_basis == 3:
                 bill = round(rental_period.days/7) * num_of_bike  * 3000
            
            print(f"Thank you for renting {num_of_bike} from us. Your bill is : {bill} ")
            return bill
        
        else:
            print("Are you have rented a bike")
            return None
        

class Customer:
    def __init__(self):
        """
        constructor method for customer calss

        """
        self.bike = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    def request_bike(self) -> int:
        bikes = input("how many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("that is not a valid number .") 
            return -1

        if bikes < 1:
            print("that is not a valid number . number of bike should be greater than zero") 
            return -1
        else:
            self.bikes = bikes

        return self.bikes


    def return_bike(self):
        """
         a function for a customer requst for rating a number of 
        """
        if  self.rental_basis and self.rental_time and  self.bikes:
            return self.rental_basis, self.rental_time ,self.bikes
        else:
            return 0,0,0    
                   



        
    