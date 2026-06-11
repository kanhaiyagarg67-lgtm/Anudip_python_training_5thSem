import twodfigures1
while True:

    print("\n===== 2D FIGURE MENU =====")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    figure_choice = int(input("Enter your choice: "))

    if figure_choice == 4:
        print("Program Ended")
        break

    # Circle
    elif figure_choice == 1:

        radius = float(input("Enter radius: "))

        while True:
            print("\n--- Circle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Circle")

            operation = int(input("Enter choice: "))

            if operation == 1:
                print("Area =", twodfigures1.circle_area(radius))

            elif operation == 2:
                print("Perimeter =", twodfigures1.circle_perimeter(radius))

            elif operation == 3:
                break

            else:
                print("Invalid Choice")

    # Rectangle
    elif figure_choice == 2:

        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        while True:
            print("\n--- Rectangle Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Rectangle")

            operation = int(input("Enter choice: "))

            if operation == 1:
                print("Area =", twodfigures1.rectangle_area(length, breadth))

            elif operation == 2:
                print("Perimeter =", twodfigures1.rectangle_perimeter(length, breadth))

            elif operation == 3:
                break

            else:
                print("Invalid Choice")

    # Square
    elif figure_choice == 3:

        side = float(input("Enter side: "))

        while True:
            print("\n--- Square Operations ---")
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Square")

            operation = int(input("Enter choice: "))

            if operation == 1:
                print("Area =", twodfigures1.square_area(side))

            elif operation == 2:
                print("Perimeter =", twodfigures1.square_perimeter(side))

            elif operation == 3:
                break

            else:
                print("Invalid Choice")

    else:
        print("Invalid Figure Choice")

