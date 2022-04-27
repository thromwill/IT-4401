import math

print("""
                         Welcome to Paint Job Estimator!
             Please enter positive values for wall space (FT^2)
                            and paint cost per gallon.
             
      """)

do_calculation = True
while(do_calculation):
        while (True):
            try:
                    wallSpace = float(input("Enter wall space (FT^2): "))
                    if wallSpace <= 0:
                        print("Please enter a positive amount of wall space.")
                        continue
                    break
            except ValueError:
                    print("Invalid input. Please enter a number.")
            
            else:
                    break

        while (True):
            try:
                    paint = float(input("Enter paint cost per gallon: "))
                    if paint <= 0:
                        print("Please enter a positive dollar amount.")
                        continue
                    break
            except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                    break
              

        gals = math.ceil((wallSpace/350))
        paintCost = gals*paint
        hours = gals*6
        laborCost = hours*62.25
        total = paintCost + laborCost
        
        print("\nPaint Gallons: " + str(gals))
        print("\tCost: $" + str(round(paintCost,2)))
        print("Labor hours: " + str(hours))
        print("\tCost: $" + str(round(laborCost,2)))
        print("Total Cost: $" + str(round(total,2)))
        

        another_calculation = input("\nDo you want to perform another calculation? (y/n)")
        if (another_calculation != "y"):
                do_calculation = False
exit()
