from datetime import datetime
#this variable is outside the functions because otherwise it couldn't be accessible 
subtotal=float(input("What is the subtotal?: "))
# principal function
def compute_discount():
    # here the main code will be, inside the main function
    def main():
        current_date = datetime.now(tz=None)
        print("today is: "+ str(current_date))
        day_of_week=current_date.weekday()
        if subtotal >= 50 and day_of_week == 1 or day_of_week == 2:
            print("Today is Tuesday or Wednesday that means you will have 10% discount in your subtotal if is greater than 50$ :)")
            #I added a variable givin the returning value the function discount gives
            result=discount()
            #Here I give the variable one of the two values that the function returns
            result_of_subtraction=result[0]
            print(f"this is your subtotal with the discount: {result_of_subtraction}")
            money_saved=result[3]
            print(f"Discount amount: {money_saved:.2f}")
            sales_amount =result[1]
            print(f"Sales tax amount {sales_amount:.2f}")
            #Here I give the variable one of the two values that the function returns
            sales_total=result[2]
            print(f"This is the total with the taxes included: {sales_total:.2f}")
        elif subtotal < 50:
            print("We would had give you a 10% discount if you were inside the rules :(")
            result01=taxes()
            sales_amount=result01[1]
            print(f"Sales tax amount {sales_amount:.2f}")
            total=result01[0]
            print(f"This is the total with the taxes included: {total:.2f}")
        else:
            print("On Tuesday and Wednesday we have 10% discount in your subtotal if its greater than 50$, but dont worry we will be waiting for you in these days")
            result02=taxes()
            sales_amount=result02[1]
            print(f"Sales tax amount {sales_amount:.2f}")
            total=result02[0]
            print(f"This is the total with the taxes included: {total:.2f}")
    # this function adds the taxes to the subtotal
    def taxes():
        sales_tax=6
        sales_tax_decimal = sales_tax/100
        sales_number= subtotal * sales_tax_decimal
        sales_total = subtotal + (subtotal * sales_tax_decimal)
        return sales_total, sales_number
    # this function subtract the subtotal and add taxes
    def discount():
        sales_tax=6
        discount_percentage = 10
        decimal_to_subtract = discount_percentage/100
        money_saved= subtotal * decimal_to_subtract
        result_of_subtraction = subtotal - (subtotal * decimal_to_subtract)
        sales_tax_decimal = sales_tax/100
        taxes_price = result_of_subtraction * sales_tax_decimal
        sales_total = result_of_subtraction + (result_of_subtraction * sales_tax_decimal)
        return result_of_subtraction, taxes_price, sales_total, money_saved
    # I name the function so it could run the program after reading all that is needed
    main()
    # I name the function so it could run the program after reading all that is needed
compute_discount()