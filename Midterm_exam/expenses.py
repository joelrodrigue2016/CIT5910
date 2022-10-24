"""
This Python exam will involve implementing a system for managing expenses.  You will
download the skeleton of the program, then implement the functions.  The design of the
program has been set up for you.

In this system, users will be able to add and deduct expenses, update expenses, sort expenses,
and export filtered expenses to a file.  The program will initially load a collection of expenses
from 2 different .txt files (in the same format) and store them in a dictionary.

NOTE(S):
- It is important that you DO NOT edit the expenses.txt file or the expenses_2.txt file.  If you do,
you could fail the automated testing.
- DO NOT change the spacing or remove any blank lines.
- DO NOT copy/paste the text from the expenses.txt file or the expenses_2.txt file into another file.
"""


def import_expenses(expenses, file):
    """Reads data from the given file and stores the expenses in the given expenses dictionary,
    where the expense type is the key and the total expense amount for that expense is the value.

    The same expense type may appear multiple times in the given file.

    Ignore expenses with missing amounts. If a line contains both an expense type and an expense amount,
    they will be separated by a colon (:).

    You can assume that if they exist, expense types are one-word strings and the amounts are numerical.

    Strip any whitespace before or after the expense types and amounts.

    Blank lines should be ignored.

    Expenses are case sensitive. "coffee" is a different expense from "Coffee"

    Note: This function will be called twice in main with the same dictionary but different files.

    This function doesn’t return anything.  Rather, it updates the given expenses dictionary based
    on the expenses in the given file.
    """

    # TODO insert your code
    # open the file read-only mode
    file1 = open(file, "r")
    # now we get every single line in the file
    for line in file1:
        # strip the spaces and add a colon to create a dictionary
        line = line.strip()
        elem = line.split(":")
        # the document in our case has only two position therefore the elements inside the file should only occupy position 0 and 1
        if len(elem) < 2 or not elem[1].strip().isdigit():
            continue
        else:

            if elem[0] in expenses:
                expenses[elem[0]] += float(elem[1])
            else:
                expenses[elem[0]] = float(elem[1])



    # for testing purposes, uncomment the following line. I did it here and in the main function as well
    # print(expenses)


def get_expense(expenses, expense_type):
    """Prints and returns the value for the given expense type in the given expenses dictionary.

    Prints a friendly message and returns None if the expense type doesn't exist. (Note: Printing a friendly message
    means that the program should not raise an error or otherwise terminate. Simply tell the user that the requested
    expense type does not exist and continue the program. Also note that None is a specific keyword in Python of
    NoneType. You should not return a string “None” from this function.)
    """

    # TODO insert your code
    try:
        # nothing gets input by the user
        if expenses[expense_type] is None:
            pass
        # something gets entered by the user, the program keeps running normally
        else:
            return expenses[expense_type]
        # any other type of expense would be a key error
    except KeyError:
        print(" the requested expense type does not exist ")
        return None


def add_expense(expenses, expense_type, value):
    """Adds the given expense type and value to the given expenses dictionary.

    If the expense type already exists, add the value to the total amount.

    Otherwise, creates a new expense type with the value.

    Prints the expense amount.

    This function doesn’t return anything.
    """

    # TODO insert your code
    # Try/except method in order to catch anything that is not a expense type
    try:
        # if the user does not input anything (not Zero since it is still an input)
        if expenses[expense_type] is None:
            pass
        # every other value can be added to the expense file including 0 as an expense.
        else:
            expenses[expense_type] += value
        # catches every possible error by not defining it and keeping it as a broad exception clause
    except Exception as e:
        expenses[expense_type] = value
        # prints expenses.
    print(expenses)


def deduct_expense(expenses, expense_type, value):
    """Deducts the given value from the given expense type in the given expenses dictionary.

    Raises a RuntimeError if the value is greater than the existing total of the expense type. Note: You are not
    supposed to use try/except to catch the RuntimeError you raised. We expect the function to raise a RuntimeError
    if the value is greater than the existing total of the expense type.

    Prints a friendly message if the expense type doesn't exist. (Note: Printing a friendly message means that the
    program should not raise an error or otherwise terminate. Simply tell the user that the requested expense type
    does not exist and continue the program.)

    Print the updated expense amount if runtime error is not raised.

    This function doesn’t return anything.
    """

    # TODO insert your code
    # Try/except method in order to catch anything that is not a expense type
    try:
        # if the user does not input anything (not Zero since it is still an input)
        if expenses[expense_type] is None:
            print("you did not deduct anything from the total amount")
            # every other value can be subtracted to the expense file including 0 as an expense
        else:
            # expense_type cannot be greater than the existing total amount of the item
            if value > expenses[expense_type]:
                print("Sorry, you input a value that is greater than the existing total")
            else:
                expenses[expense_type] -= value
            # catches every possible error by not defining it and keeping it as a broad exception clause
    except Exception as e:  # this catches every exception and keeps the program running
        print("The expense type does not exist")
        # prints expenses.
    print(expenses)


def update_expense(expenses, expense_type, value):
    """Updates the given expense type with the given value in the given expenses dictionary.

       Prints a friendly message if the expense type doesn't exist.  Note: Printing a friendly message means that the program should not raise an error or otherwise terminate. Simply tell the user that the requested expense type does not exist and continue the program.

       Prints the updated expense amount if it exists.

       This function doesn’t return anything.

    """

    # TODO insert your code
    # expenses is the file whereas expense_type and value represent the items inside the file expenses.txt
    try:

        if expense_type in expenses:
            expenses[expense_type] = value

        else:
            print("requested expense type does not exist")


    except Exception as e:
        print("The expense does not exist")
        # prints expenses.
    print(expenses)


def sort_expenses(expenses, sorting):
    """Converts the key:value pairs in the given expenses dictionary to a list of tuples and
    sorts based on the given sorting argument.

    If the sorting argument is the string ‘expense_type’, sorts the list of tuples based on the
    expense type (e.g. ‘rent’) in ascending alphabetical order,
    e.g. sorted results: ("coffee", 5), ("food", 5000), ("rent", 1000)

    Otherwise, if the sorting argument is ‘amount’, sorts the list of tuples based on the total
    expense amount (e.g. 825) in descending order,
    e.g. sorted results: ("food", 5000), ("rent", 1000), ("coffee", 5)

    Returns the list of sorted items. (Note: If the given sorting argument is not an acceptable value (e.g. ‘expense_type’ or 'amount'),
    this function does nothing except print a friendly message and return None.)
    """

    # TODO insert your code
    # If the sorting argument is the string ‘expense_type’, sorts the list of tuples based on the
    # expense type (e.g. ‘rent’) in ascending alphabetical order
    # sort by keys if sorting is expense_type. there are two keys/items 0,1
    if sorting == 'expense_type':
        expenses = sorted(expenses.items())
    # sort by value if sorting is based on the amount
    elif sorting == 'amount':
        expenses = sorted(expenses.items(), key=lambda item: item[1])
    # invalid input, prompt user
    else:
        print('Invalid sorting type! Try again')
    # return expenses organized by amount or item type back to the user.
    return expenses


def export_expenses(expenses, expense_types, file):
    """Exports the given expense types from the given expenses dictionary to the given file.

    Do not append to the file. If the function is called again, make sure it overwrites what was previously on the
    file instead of appending to it.

    Iterates over the given expenses dictionary, filters based on the given expense types (a list of strings),
    and exports to a file.  Skips any expense type in the given list of expense types that doesn't exist.

    If the expenses argument is the dictionary {"food": 5000, "rent": 1000, "coffee": 5, "clothes": 58.92}
    and the expense_types argument is the list of strings ‘coffee, clothes, rent’, exports a file containing:
    coffee: 5
    clothes: 58.92
    rent: 1000

    If the expenses argument is the dictionary {"food": 5000, "rent": 1000, "coffee": 5, "clothes": 58.92}
    and the expense_types argument is the list of strings ‘coffee, clothes, sports’, exports a file containing:
    coffee: 5
    clothes: 58.92

    Note, the specified expense type 'sports' does not exist in the expenses dictionary, so it is ignored.

    If an item is duplicated in the given expense types, don’t worry about it, just export the data as is.
    You should not deduplicate the expense types.

    This function doesn’t return anything.
    """

    # TODO insert your code
    output_line = ""
    out = []

    # Iterating over the given expense file, filters based on the given expense types (a list of strings),
    for item in expense_types:
        try:
            if expenses[item]:
                # just to clarify this is appending to the out empty list not the overall file since it will overwrite
                # everything
                out.append(item)
        except Exception as e:
            pass
    # organizing the file in to a dictionary before exporting it on a separate file
    for key in out:
        output_line += "\n" + key + ": " + str(expenses[key])
    output_string = output_line[0:-2]
    print(output_line)
    f = open(file, "a")

    # and exports to a file. Skips any expense type in the given list of expense types that doesn't exist.
    f.write(output_line)
    f.close()


def main():
    # import expense files and store in dictionary
    expenses = {}
    import_expenses(expenses, 'expenses.txt')
    import_expenses(expenses, 'expenses_2.txt')

    # for testing purposes, uncomment the following line
    # print(expenses)

    while True:

        # print welcome and options
        print('\nWelcome to the expense management system!  What would you like to do?')
        print('1: Get expense info')
        print('2: Add an expense')
        print('3: Deduct an expense')
        print('4: Update an expense')
        print('5: Sort expenses')
        print('6: Export expenses')
        print('0: Exit the system')

        # get user input
        option_input = input('\n')

        # try and cast to int
        try:
            option = int(option_input)

        # catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            # check options
            if option == 1:

                # get expense type and print expense info
                expense_type = input('Expense type? ')
                print(get_expense(expenses, expense_type))

            elif option == 2:

                # get expense type
                expense_type = input('Expense type? ')

                # try and get amount to add and cast to float
                try:
                    amount = float(input('Amount to add? '))

                # catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # add expense
                    add_expense(expenses, expense_type, amount)

            elif option == 3:

                # get expense type
                expense_type = input('Expense type? ')

                # try and get amount to deduct and cast to float
                try:
                    amount = float(input('Amount to deduct? '))

                # catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # deduct expense
                    deduct_expense(expenses, expense_type, amount)

            elif option == 4:

                # get expense type
                expense_type = input('Expense type? ')

                # try and get amount to update expense to
                try:
                    amount = float(input('Amount to update expense to? '))

                # catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # update expense
                    update_expense(expenses, expense_type, amount)

            elif option == 5:

                # get sort type
                sort_type = input('What type of sort? (\'expense_type\' or \'amount\') ')

                # sort expenses
                print(sort_expenses(expenses, sort_type))

            elif option == 6:

                # get filename to export to
                file_name = input('Name of file to export to? ')

                # get expense types to export
                expense_types = []

                while True:
                    expense_type = input("What expense type you want to export? Input N to quit: ")
                    if expense_type == "N":
                        break

                    expense_types.append(expense_type)

                # export expenses
                export_expenses(expenses, expense_types, file_name)

            elif option == 0:

                # exit expense system
                print('Good bye!')
                break

            # corner case
            else:
                print("Invalid option.")


if __name__ == '__main__':
    main()
