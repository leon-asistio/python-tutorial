while True:
    print("======PYTHON TUTORIAL=======")
    print("What do you want to learn?")
    print("1. INTRODUCTION TO PROGRAMMING")
    print("2. BASIC SYNTAX")
    print("3. ARITHMETIC OPERATORS")

    answer = int(input("CHOOSE A LESSON: "))
    if answer == 1:
        print("\nWHAT IS PROGRAMMING LANGUAGE?")
        print("A programming language is a special language that computers understand and use to perform tasks.")
        print("Why learn PYTHON?")
        print("1. Simple and easy to learn, 2. Readable Syntax, 3. Versatile\n")
        print("QUESTION:")
        print("Which is an example of Programming language?")
        print("a. Pycharm")
        print("b. VS code")
        print("c. Python")

        answer1 = input("\nEnter your choice: ").lower()
        if answer1 == 'a':
            print("Incorrect answer.")
        elif answer1 == 'b':
            print("Incorrect answer.")
        elif answer1 == 'c':
            print("You are correct!")
        else:
            print("Invalid choice")


    elif answer == 2:
        print("\nWHAT IS PYTHON SYNTAX?")
        print("Syntax refers to the set of rules that tells us how to correctly write a program in Python.")
        print("\nREMEMBER!")
        print("1. PYTHON IS CASE SENSITIVE")
        print("Python treats uppercase and lowercase letters differently")
        print("2. INDENTATION")
        print("Unlike other programming languages, Python uses indentation (spaces) to define blocks of code.")
        print("\nQUESTION:")
        print("Is variable 'Name' and 'name' the same?(yes/no): ")
        answer3 = input("\nEnter your choice: ").lower()
        if answer3 == 'yes':
            print("Incorrect answer.")
        elif answer3 == 'no':
            print("You are correct!")
        else:
            print("Invalid choice")

        print("\nIs Indentation in Python important?(yes/no): ")
        answer4 = input("\nEnter your choice: ").lower()
        if answer4 == 'yes':
            print("You are correct!")

        elif answer4 == 'no':
            print("Incorrect answer.")
        else:
            print("Invalid choice")

    elif answer == 3:
        print("\nWHAT ARE ARITHMETIC OPERATORS?")
        print("Arithmetic operators are symbols used to perform mathematical calculations on numbers.")
        print("They work the same way as the operators used in everyday mathematics.")
        print("\nPYTHON ARITHMETIC OPERATORS")
        print("(Add +) (Sub -) (Sum ) (division /) (floor division //) (Modulus %) (Exponentiation *)\n")
        print("SOLVE THIS:")
        print("a = 2")
        print("b = 2")
        print("c = 4")
        print("(a + b / c)")
        print("Which answer is correct?")
        print("a. 8 b. 4 c. error")
        answer5 = input("\nEnter your choice: ").lower()
        if answer5 == 'b':
            print("You are correct!")
        elif answer5 == 'a':
            print("Incorrect answer.")
        elif answer5 == 'c':
            print("Incorrect answer.")
        else:
            print("Invalid choice")

        print("SOLVE THIS:")
        print("a = 6")
        print("b = 5")
        print("c = 7")
        print("(a - b * c)")
        print("Which answer is correct?")
        print("a. 41 b. b. 7 c. error")

        answer6 = input("\nEnter your choice: ").lower()
        if answer6 == 'a':
            print("You are correct!")
        elif answer6 == 'b':
            print("Incorrect answer.")
        elif answer6 == 'c':
            print("Incorrect answer.")
        else:
            print("Invalid choice")

        print("\nREMEMBER:")
        print("Python follows the order of (PEMDAS)")
        print("Parenthesis, Exponents, Multiplication")
        print("Division, Addition, Subtraction\n")
        print("THANK YOU! 🙂")
        break

    else:
        print("Invalid choice")