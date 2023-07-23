from rentalmanagement import BikeRental,Customer
def main():
    bike_shop = BikeRental(50)
    customer = Customer()

    while True:

      print("""
           ============ Bike rental management system ===========
            1. Display avail Bikes 
            2. request a bike on hourly basis. Rate : 20 tk
            3. request a bike on daily basis. Rate : 500 tk
            4. request a bike on weekly basis. Rate : 3000 tk
            5. Return a rented bike
            6. Exit


        """
             

        )

      choice = input("enter choice")   

      try:
         choice = int(choice)

       
      except ValueError:
         print("this is not a valid  choice . ")
         continue
      if choice == 1:
         bike_shop.display_stock()
      elif choice == 2:
         customer.rental_time = bike_shop.rent_bike_on_hourly_basis(customer.request_bike())   
         customer.rental_basis = 1
      elif choice == 3:
         customer.rental_time = bike_shop.rent_bike_on_daily_basis(customer.request_bike())   
         customer.rental_basis = 1
      elif choice == 4:
         customer.rental_time = bike_shop.rent_bike_on_Weekly_basis(customer.request_bike())   
         customer.rental_basis = 1
      elif choice ==5:
         customer.bill = bike_shop.return_bike(customer.return_bike())
         customer.rental_basis, customer.rental_time, customer.bikes = 0,0,0
      elif choice == 6:
         break
      else :
         print("Invalid input")
    print("thank you fr rental service")

if __name__=='__main__':
   main()

              

