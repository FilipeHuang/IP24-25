price = float(input())
type = input()
if type == "P":
    print(f"Customer: P | Price: {round(price*1.06,3)}")
else:
    if price < 50:
        print(f"Customer: F | Price: {round(price*0.98,3)}")
    elif price > 200:
        print(f"Customer: F | Price: {round(price*0.90,3)}")
    else:
        print(f"Customer: F | Price: {round(price*0.95,3)}")