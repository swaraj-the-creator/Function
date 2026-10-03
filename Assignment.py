i = 0
r = 0
while i <= 100:
    def greet_customer():
        print("Welcome to the Art Supplies Store!")
        print("Get your colours, brushes, and paper here.")
    greet_customer()
    price_per_item = float(input("Enter the price per art item in dollars: "))
    items_bought = int(input("Enter the number of art items bought: "))
    def calculate_total(price, items):
        total = price * items
        return total
    total_cost = calculate_total(price_per_item, items_bought)
    rounded_total = round(total_cost, 2)
    print("Total Cost:", rounded_total)
    amount_paid = float(input("Enter the amount paid by the customer: "))
    def late_change(paid, total):
        change = total - paid
        return change
    def calculate_change(paid, total):
            change = paid - total
            return change
    change_due = calculate_change(amount_paid, rounded_total)
    ha = late_change(amount_paid, rounded_total)
    runded_tota = round(ha,2)
    rounded_change = round(change_due, 2)
    def thank_you_message(items):
        if items >= 5:
            return "Great choice! You picked many art supplies for your project."
        else:
            return "Thanks for shopping at the art supplies store!"
    money = runded_tota
    closing_message = thank_you_message(items_bought)
    print("")
    print("===== ART SUPPLIES BILL =====")
    print("Price Per Item:", price_per_item)
    print("Items Bought:", items_bought)
    print("Total Cost:", rounded_total)
    print("Amount Paid:", amount_paid)
    if amount_paid <= rounded_total:
        print("Money left to pay: ",money) 
        print(closing_message)
    else:
        print(closing_message)
        print("Change Due:", rounded_change)
    print("=============================")
    yn = str(input("More customer? yes/no:"))
    if yn == "yes":
        continue
    elif yn == "no":
        break
    else:
        print("it's an invalid answer.")
    i = i + 1
    r =+ 1
print("Total customers served: ",r)
