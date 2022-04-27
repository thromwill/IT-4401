print("""
                         Welcome to Position Calculator!
             Please enter initial conditions as float values in meters.
             
      """)

do_calculation = True
while(do_calculation):
        while (True):
            try:
                    pInit = float(input("Enter initial position (x0): "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                    break

        while (True):
            try:
                    vInit = float(input("Enter initial velocity (v0): "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                    break
        while (True):
            try:
                    acc = float(input("Enter acceleration (a): "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                    break
        while (True):
            try:
                    time = float(input("Enter time (t): "))
                    if(time < 0):
                            print("Please enter a non-negative time.")
                            continue
            except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                    break        


        pFin = (pInit) + (vInit*time) + ((0.5)*acc*(time*time))

        print("\nFinal position (xf) = x0 + v0*t + (1/2)* a *(t^2)")
        print("               (xf) =",pInit,"+", vInit,"*",time,"+ (1/2)*",acc,"*(",time,"^ 2)") 
        print("               (xf) =",pFin)
        print("\nThe final position of the object is", pFin,"meters.")

        another_calculation = input("Do you want to perform another calculation? (y/n)")
        if (another_calculation != "y"):
                do_calculation = False
exit()
