Product_names = []
Product_purchase_dates = []
Price_of_Products = []
total_price = 0
Products = [Products for Products in input("Products and their purchasing dates: ").split(",")]

for i in range(len(Products)):
    x,y = Products[i].split("_")
    Product_names.append(x)
    Product_purchase_dates.append(y)

Price_of_Products = [float(Price_of_Products) for Price_of_Products in input("Prices of the products: ").split(",")]

while(1):
    temp = input("Starting Year-Ending Year: ")

    if len(temp) != 9:
        print("Years were not entered in correct format.")
        continue
    elif "-" not in temp:
        print("Years were not entered in correct format.")
        continue

    start_year,end_year = temp.split("-")

    try:
        stary_year = int(start_year)
    except ValueError:
        print("Years were not entered in correct format.")
        continue

    try:
        end_year = int(end_year)
    except ValueError:
        print("Years were not entered in correct format.")
        continue

    start_year = int(start_year)
    end_year = int(end_year)

    if start_year <= end_year:
        break
    else :
        print("Years were not entered in correct format.")


while(1):
    Selected_Product = input("Product Name: ")

    if Selected_Product in Product_names:
        for i in range(len(Products)):
            if Product_names[i] == Selected_Product:
                a,b,year = Product_purchase_dates[i].split(".")
                year = int(year)
                if year >= start_year and year <= end_year:
                    total_price += Price_of_Products[i]
        print("Customer spent {} for {} in years {}-{}.".format(total_price,Selected_Product,start_year,end_year))
        break
    else:
        print("The customer did not buy this product.")
