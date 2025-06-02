weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ").strip().lower()

if unit == "l":
    weight_lb = weight * 2.20462
    print("Weight in Lbs: ", weight_lb)
elif unit == "k":
    weight_kg = weight / 2.20462
    print("Weight in Kg: ", weight_kg)
else:
    print("Invalid Input")

