#fuction to calculaate thr electrionics GST
def  calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst

#fuction to calculaate thr Fashon GST
def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst

#fuction to calculate Food GST
def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst

# function to calculate Total bill 
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    total_bill = electronics + fashion + food
    return total_bill

# function to calculate discounted bill
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount
    return final_amount

a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("Total after GST =", total,)
print("Discount =", discount,)
print("Final payable amount =", final_amount,)