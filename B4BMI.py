class bmi(Exception):
    print("\t************************************************************************************")
    print("\t\t\t\t      Wel-Come To BMI Calculator")
    print("\t************************************************************************************\n")

    pass

while True:
    try:
        name = input("\t\t\t\t Enter Your Name: ")
        h_t = float(input("\t\t\t\t Enter Your Height in Centimeters: "))
        w_t = float(input("\t\t\t\t Enter Your Weight in Kg: "))
        print()
        h_t = h_t / 100
        b_mi = w_t / (h_t * h_t)
        print("\t\t\t\t Your Body Mass Index is: ", b_mi)
        if b_mi > 0:
            if b_mi<=17:
                print("\t\t\t\t You Are Extermely Weightless")
            elif b_mi <= 19:
                print("\t\t\t\t You Are Underweight")
            elif b_mi <= 26:
                print("\t\t\t\t You Are Physically Fit")
            elif b_mi <= 31:
                print("\t\t\t\t You are Overweight")
            else:
                print("\t\t\t\t You Are Extermely Outsize")
        else:
            print("\t\t\t\t Enter valid details")
    except ValueError:
        print("\t\t\t\t Please enter a valid number for height and weight")
    else:
        print("\n\t************************************************************************************\n")
        ch = input("\t\t\t\t Do You Want To Continue... (YES/NO)? ")
        if ch.upper() != "YES":
            print("\n\t**************************** Thank You For Visiting ********************************")
            break







        
