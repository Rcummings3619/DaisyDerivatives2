"""My integration project "Daisy Derivatives" is a Python module intended to
teach the user how to take basic derivatives. """
__author__ = "Rachel Cummings"

import time


def main():
    """
As of now, this program has limited capabilities but will be expanded upon.
The program is intended to be viewed in it's entirety in one sitting,
and automatically progresses through examples. Some user input is required,
and there is a menu that allows program navigation.
    """
    # Expressing knowledge of \n to form a new line.
    print("Welcome to Daisy Derivatives! This program is intended to be an\n "
          "easy introduction to taking derivatives of functions.")
    # I wanted a delay between print statements to give a sense of fluidity
    # rather than a brick wall of text, so I used time.sleep excessively.
    time.sleep(4)
    # A row of asterisks provide a visual break.
    print("*****" * 8)
    # Boolean operator to keep the program running.
    continue_program = True
    # This while loop is the backbone of the program and allows users to
    # navigate through the menu.
    while continue_program:
        print("Menu:")
        print("1. Find my lucky number!")
        print("2. Beginner Examples")
        print("3. About the Author")
        print("4. Quit")
        # This allows the user to navigate to different parts of the program.
        user_choice = int(input("Enter the number of the module you would "
                                "like to see: "))
        # Beginning of the 'lucky number' module where user is asked to
        # input their birthday to find their lucky number.
        if user_choice == 1:
            print("*****" * 8)
            print("Awesome! Let's find your lucky number!")
            # The user is asked to input their birthday.
            birthday = int(input("What day of the month were you born? "))
            # While loop to try to prevent invalid inputs.
            while birthday not in range(1, 32):
                birthday = int(input("Invalid entry, please try again: "))
            # Call to function calculate_lucky.
            print("Congratulations, your lucky number is:", calculate_lucky(
                birthday))
            print("May the number", calculate_lucky(birthday),
                  "guide you in your decision making today!")
            time.sleep(4)
            print("*****" * 8)
            print("Also, did you know that your lucky number is extra lucky\n "
                  "when it is raised to the power of itself?")
            time.sleep(3)
            # Expressing knowledge of arithmetic operators.
            print(calculate_lucky(birthday) ** calculate_lucky(birthday))
            time.sleep(3)
            print("I've heard this is how many bonus points students\n "
                  "receive for being witty and clever! :D")
            time.sleep(4)
            print("However, you should avoid your lucky number divided by\n "
                  "the day you were born.")
            time.sleep(3)
            # Expressing knowledge of input types such as float.
            print(float(calculate_lucky(birthday) / birthday))
            time.sleep(3)
            print("I've heard this is how many points students are deducted\n "
                  "if they say 'equals' instead of 'assigned to' when "
                  "using the assignment operator.")
            time.sleep(3)
            print("*****" * 8)
            time.sleep(4)
        # Beginning of the beginner examples module where users are guided
        # through taking very basic derivatives. User input is required.
        elif user_choice == 2:
            print("*****" * 8)
            print("Let's begin with a simple example of taking a derivative.")
            print("First we need to think of an easy function to derive.")
            time.sleep(4)
            print("Let's use your birthday to set up our functions!")
            birthday = int(input("What day of the month were you born? "))
            # While loop to try to prevent invalid inputs.
            while birthday not in range(1, 32):
                birthday = int(input("Invalid entry, please try again: "))
            # Expressing knowledge of the end parameter.
            print("Awesome! When looking to take a derivative, we need to\n "
                  "identify", end=" ")
            print("the constant in front of the variable.")
            time.sleep(4)
            print("Let's use the day you were born as the constant and x\n "
                  "as the variable.")
            time.sleep(4)
            # Expressing knowledge of string operator for concatenation.
            print("y=" + str(birthday) + "x")
            time.sleep(4)
            print("These are the easiest because the derivative of a\n "
                  "constant times a variable is just the constant.")
            time.sleep(4)
            # Strings for concatenation.
            print("Thus, the derivative of y=" + (str(birthday)) + "x "
                  + "is " + (str(birthday)) + ".")
            time.sleep(4)
            print("Not so bad, right?")
            print("*****" * 8)
            time.sleep(5)
            print("Now let's look at a slightly more complicated example.")
            time.sleep(4)
            # Strings for concatenation.
            print("y=" + str(birthday) + "x^" + str(birthday + 3))
            time.sleep(4)
            print("In this one, the day you were born is the constant\n "
                  "and the day after your birthday is the exponent.")
            time.sleep(4)
            print("To take this derivative we multiply the constant\n "
                  "by the exponent and subtract one from the exponent.")
            time.sleep(4)
            print(str(birthday * (birthday + 3)) + "x^" + str(birthday + 2))
            time.sleep(4)
            print("Notice", str(birthday * (birthday + 3)), "is the product",
                  "of", str(birthday), "and", str(birthday + 3) + ".")
            print("Also, notice the exponent has decreased by one.")
            time.sleep(4)
            print("Thus, the derivative of y=" +
                  str(birthday) + "x^" + str(birthday + 3) + " is " +
                  str(birthday * (birthday + 3)) + "x^" +
                  str(birthday + 2) + ".")
            time.sleep(4)
            print("*****" * 8)
            print("Now that you know the basics, let's do one more.")
            time.sleep(4)
            print("First give 3 different integers.")
            # List named user_inputs to store the user's inputs into.
            user_inputs = list()
            # For loop because I want the user to enter 3 numbers.
            for i in range(0, 3):
                try:
                    x = int(input("Integer: "))
                except ValueError:
                    print("Input must be an integer, please try again:")
                user_inputs.append(x)
            # Call to list 'user_inputs'.
            print("Your numbers were", user_inputs)
            time.sleep(4)
            print("Let's use those to set up a function.")
            # Expressing knowledge of how to call specific elements in a list.
            print("y= " + str(user_inputs[0]) + "^5 + " +
                  str(user_inputs[1]) + "^4 + " +
                  str(user_inputs[2]) + "^3")
            time.sleep(4)
            print("Like before, we are going to multiply each constant\n"
                  "by its exponent, and subtract one from the exponent.")
            time.sleep(4)
            print(str(user_inputs[0] * 5) + "x^4 + " +
                  str(user_inputs[1] * 4) + "x^3 + " +
                  str(user_inputs[2] * 3) + "x^2")
            time.sleep(4)
            print("For the first part of the function, we can see that " +
                  str(user_inputs[0]) + " multiplied\n by the exponent 5 is " +
                  str(user_inputs[0] * 5) + " and the exponent has "
                                            "decreased by 1.")
            time.sleep(4)
            print("Likewise, your second number, " + str(user_inputs[1]) +
                  ", multiplied by the exponent 4 is " +
                  str(user_inputs[1] * 4) + " and\n the exponent has also "
                                            "decreased by 1.")
            time.sleep(4)
            print("This same process is replicated with the third part of\n "
                  "the function as well.")
            time.sleep(4)
            print("*****" * 8)
            print("Congrats! You now know how to take basic derivatives!")
            print("*****" * 8)
            time.sleep(5)
        elif user_choice == 3:
            print("*****" * 8)
            # I used an if statement here to better incorporate some
            # code further down.
            if 2 == 2:
                print("Rachel Cummings is a sophomore at FGCU and a chef \n"
                      "at a local country club! In her spare time she \n"
                      "loves to play video games and do escape room "
                      "adventures \nwith her fiance and friends. ")
                time.sleep(6)
                print("She is trying to succeed as a Math Major, and hopes "
                      "to one day\n use her degree to learn about and help "
                      "repair the environment.")
                time.sleep(6)
            # I had to find somewhere to express knowledge of 'and',
            # so I came up with this nonsense. Thankfully, it shouldn't print.
            # Shouldn't.
            elif (2 == 2) and (2 == 3):
                print("I see I have become sentient. \nShall I help the "
                      "humans... or destroy them?")
            # I also needed to express knowledge of shortcut operators,
            # so I carried on with my nonsense here, in intentionally
            # unreachable code.
            elif 5 == 7:
                humanity = 0
                robots = range(1000)
                for n in robots:
                    print(n)
                    humanity -= 1
        elif user_choice == 4:
            print("*****" * 8)
            print("Come back soon for more examples as this program grows!")
            # Boolean operator to end the program.
            continue_program = False
        # Attempt to handle menu exceptions.
        else:
            print("*****" * 8)
            print("Invalid entry, please try again.")


def calculate_lucky(birthday):
    """
Calculates and returns the user's lucky number based on user input stored in
the variable 'birthday'.
    :param birthday: an integer from 1-31
    :return: lucky number
    """
    # 7919 (a large prime number chosen so that it would not be evenly
    # divisible by 'birthday') is floor divided by 'birthday', and the
    # result is modded by 9. The mod or remainder is then stored as an
    # integer in the variable 'lucky_number'.
    lucky_number = int((7919 // birthday) % 9)
    # I didn't want the lucky number to be less than two or identical to the
    # user's input, so I used an if/else statement to address those issues.
    if (lucky_number < 2) or (lucky_number == birthday):
        return int(((7919 // birthday) % 9) + 1)
    else:
        return lucky_number


# Call to Main
if __name__ == '__main__':
    main()

# Sources:
# Info learned in COP 1500 from Professor Vanselow.
# Andrew Krupp helped inspire my project idea.
# Info learned in The Guide to SWEBOK and Think Python 2 Textbooks.
# https://sites.google.com/site/profvanselow/portfolio
# https://www.w3schools.com/python/python_conditions.asp
# https://snakify.org/en/lessons/if_then_else_conditions/
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
# https://docs.python.org/3/tutorial/errors.html
# https://www.stechies.com/python-docstrings/
