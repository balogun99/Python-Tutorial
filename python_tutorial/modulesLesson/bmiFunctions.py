def calculate_bmi(weight, height):
    calculation = weight / (height * height)
    return calculation

def show_results(weight, height):
    calculation = calculate_bmi(weight, height)
    if calculation <= 18.5:
        print("Underweight")
    elif calculation > 18.5 and calculation <= 25:
        print("Normal")
    else:
        print("Overweight")