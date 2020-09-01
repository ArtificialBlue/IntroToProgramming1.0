#Asks the user for Input of what shape they'd like to Calculate the volume of
shapeSelected = raw_input("Select Shape to Calculate Volume Of:")
#List of Shapes available currently to calculate volume of
shapeSelection = ["Sphere","Pyramid","Cone","Ellipsoid","Cylinder","Torus"]
#Mathematical Pi constant used in various calculations
piConstant = 3.1415926
#If statement which checks to see if shape input is within the loist of shapes available,
#Otherwise states that shape isn't recognized, and for the program to be run again. 
if shapeSelected in shapeSelection:
    print("Shape Confirmed")
    if shapeSelected == "Sphere":
        #User Input for needed variables
        radius = raw_input("Insert radius of Sphere to Calculate")
        #Mathematical Formula for Sphere Volume
        Volume = (4.0/3.0) * piConstant * ((int(radius))** 3)
        print(Volume)

    elif shapeSelected == "Pyramid":
        print("Note: Volume for Right Rectangular Pyramid")
        #User Input for needed variables
        length = int(raw_input("Insert length of Pyramid Base"))
        width = int(raw_input("Insert width of Pyramid Base"))
        height = int(raw_input("Insert height of Pyramid"))
        #Mathematical Formula for Right Rectangular Pyramid Volume
        Volume = (1.0/3.0) * length * width * height
        print(Volume)
        
    
    elif shapeSelected == "Cone":
        #User Input for needed variables
        radius = raw_input("Insert radius of Cone Base to Calculate")
        height = raw_input("Insert height of Cone to Calculate")
        #Mathematical Formula for Cone Volume
        Volume = (1.0/3.0) * piConstant * ((int(radius))** 2) * int(height)
        print(Volume)

    elif shapeSelected == "Ellipsoid":
        #User Input for needed variables
        axisA =  int(raw_input("Insert radius of first Axis to Calculate"))
        axisB =  int(raw_input("Insert radius of second Axis to Calculate"))
        axisC =  int(raw_input("Insert radius of third Axis to Calculate"))
        #Mathematical Formula for Ellipsoid Volume
        Volume = (4.0/3.0) * piConstant * axisA * axisB * axisC
        print(Volume)
        

    elif shapeSelected == "Cylinder":
        #User Input for needed variables
        radius = raw_input("Insert radius of Cylinder Base to Calculate")
        height = raw_input("Insert height of Cylinder to Calculate")
        #Mathematical Formula for Cylinder Volume
        Volume = piConstant * (int(radius)** 2) * int(height)
        print(Volume)

    elif shapeSelected == "Torus":
        #User Input for needed variables
        R = int(raw_input("Insert radius R of Major radius to Calculate"))
        r = int(raw_input("Insert radius r of Minor radius to Calculate"))
        #Mathematical Formula for Torus Volume
        Volume = 2.0 * (piConstant ** 2) * (r ** 2) * R
        print(Volume)


    else:
        #Code for built-in redundancy in case the user 
        #*somehow* gets a shape confirmed yet the shape isn't within the options.
        print("Error. Please Try Again.")
else:
    print("I do not Recognize that shape. Please try again.")