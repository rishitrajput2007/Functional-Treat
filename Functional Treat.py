print("Welcome to the Data Analyzer and Transformer Program")

l=[]

while True:
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Function)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    n=int(input("Please Enter your Choice: "))

    match n:

        case 1:

           print("Enter data for a 1D array (separated by spaces):")

           for i in range(7):
               l.append(int(input()))

           print("Data has been stored successfully!")


        case 2:
            if len(l)==0:
                print("Please Enter the Data first")

            else:
                print("Data Summary:")
                print("- Total elements: ", len(l))
                print("- Minimum Value:", min(l))
                print("- Maximum Value:", max(l))
                print("- Sum of all values:", sum(l))
                print("- Average value:", sum(l) / len(l))


        case 3:



            def fac(a):
                if a == 0:
                    return 1

                elif a<0:
                    print("Invalid Number")

                else:

                    return a * fac(a - 1)


            a = int(input("Enter the number to calculate its factorial: "))
            f = fac(a)
            print(f"Factorial of {a} is :",f)

        case 4:
            c=int(input("Enter the threshold value to filter out data above this value: "))
            print(f"Filtered Data (values>={c})")
            if len(l)==0:
                print("Please Enter the value")

            else:
                a = list(filter(lambda x: x >= c, l))
                print(a)

        case 5:
            print("Choose sorting option: ")
            print("1. Ascending")
            print("2. Descending")

            m=int(input("Enter your choice: "))

            match m:
                case 1:
                    print("Sorted Data in Ascending Order:")
                    l.sort()
                    print(l)
                case 2:
                    print("Sorted Data in Descending Order:")
                    l.sort(reverse=True)
                    print(l)

                case _:
                    print("Invalid Choice")


        case 6:

            if len(l)==0:
                print("Please Enter the Data first")

            else:

                print("Dataset Statistics: ")
                print("- Minimum value: ",min(l))
                print("- Maximum Value:", max(l))
                print("- Sum of all values:", sum(l))
                print("- Average value:", sum(l) / len(l))

        case 7:
            print("Thank you for using the Data Analyzer and Transformer program. Goodbye!")
            break


        case _:
            print("Invalid choice")

