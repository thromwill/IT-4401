print("""
                         Welcome to Position Calculator!
             Please enter initial conditions as float values in meters.
             
      """)

#create variables for initial position, initial velocity,
#acceleration, time, and have them set to user input
pInit = float(input("Enter initial position (x0): "))
vInit = float(input("Enter initial velocity (v0): "))
acc = float(input("Enter acceleration (a): "))
time = float(input("Enter time (t): "))

#calculate final position using Xf = X0 + V0t + 1/2at^2
pFin = (pInit) + (vInit*time) + ((0.5)*acc*(time*time))

print("\nFinal position (xf) = x0 + v0*t + (1/2)* a *(t^2)")
print("               (xf) =",pInit,"+", vInit,"*",time,"+ (1/2)*",acc,"*(",time,"^ 2)") 
print("               (xf) =",pFin)
print("\nThe final position of the object is", pFin,"meters.")
