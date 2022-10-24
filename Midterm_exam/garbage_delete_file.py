# expenses.py
def import_expenses(expenses, file):
    file1 = open(file, "r")
    for line in file1:
        line = line.strip()
        elem = line.split(":")
        if len(elem) < 2 or not elem[1].strip().isdigit():
            continue
        else:
            if elem[0] in expenses:
                expenses[elem[0]] += float(elem[1])
            else:
                expenses[elem[0]] = float(elem[1])
    # print(expenses)


def get_expense(expenses, expense_type):
    try:
        if expenses[expense_type] is None:
            pass
        else:
            return expenses[expense_type]
    except KeyError:
        print("The expense does not exist")
        return None


def add_expense(expenses, expense_type, value):
    try:
        if expenses[expense_type] is None:
            pass
        else:
            expenses[expense_type] += value
    except KeyError:
        expenses[expense_type] = value
    # print(expenses)


def deduct_expense(expenses, expense_type, value):
    try:
        if expenses[expense_type] is None:
            print("you did not deduct anything")
        else:
            if value > expenses[expense_type]:
                print("Input value is greater than existing total")
            else:
                expenses[expense_type] -= value
    except KeyError:
        print("The expense type does not exist")
    print(expenses)


def update_expense(expenses, expense_type, value):
    # expenses is the file whereas expense_type and value represent the items inside the file expenses.txt
    try:

        if expense_type in expenses:
            expenses[expense_type] = value

        else:
            print("requested expense type does not exist")


    except Exception as e:
        print("The expense does not exist")
    print(expenses)


def sort_expenses(expenses, sorting):
    # sort by keys if sorting is expense_type
    if sorting == 'expense_type':
        expenses = sorted(expenses.items())
    # sort by value if sorting
    elif sorting == 'amount':
        expenses = sorted(expenses.items(), key=lambda item: item[1])
    # invalid input, prompt user
    else:
        print('Invalid sorting type! Try again')
    # return expenses dict to user

    return expenses


def export_expenses(expenses, expense_types, file):
    output_string = ""
    out = []
    for item in expense_types:
        try:
            if expenses[item]:
                out.append(item)
        except KeyError:
            pass

    for key in out:
        output_string += "\n" + key + ": " + str(expenses[key])
    output_string = output_string[0:-2]
    print(output_string)
    f = open(file, "a")
    f.write(output_string)
    f.close()


def main():
    # import expense file and store in dictionary
    expenses = {}
    import_expenses(expenses, 'expenses.txt')
    import_expenses(expenses, 'expenses_2.txt')

    while True:
        # print welcome and options
        print('\nWelcome to the expense management system! What would you like to do?')
        print('1: Get expense info')
        print('2: Add an expense')
        print('3: Deduct an expense')
        print('4: Sort expenses')
        print('5: Export expenses')
        print('0: Exit the system')

        # get user input
        option_input = input('\n')

        # try and cast to int
        try:
            option = int(option_input)
        # catch ValueError
        except ValueError:
            print("Invalid option.")

        if option == 1:
            # get expense type and print expense info
            expense_type = input('Expense type? ')
            print(get_expense(expenses, expense_type))
        elif option == 2:
            # get expense type
            expense_type = input('Expense type? ')
            # get amount to add and cast to float
            amount = float(input('Amount to add? '))
            # add expense
            add_expense(expenses, expense_type, amount)
        elif option == 3:
            # get expense type
            expense_type = input('Expense type? ')
            # get amount to deduct and cast to float
            amount = float(input('Amount to deduct? '))
            # deduct expense
            deduct_expense(expenses, expense_type, amount)
        elif option == 4:
            # get sort type
            sort_type = input('What type of sort? (\'expense_type\' or \'amount\')')
            # sort expenses
            print(sort_expenses(expenses, sort_type))
        elif option == 5:
            # get filename to export to
            file_name = input('Name of file to export to?')
            # get expense types to export
            expense_types = []
            while True:
                expense_type = input("What expense type you want to export? Input N to quit:")
                if expense_type == "N":
                    break
                expense_types.append(expense_type)
                # export expenses
            export_expenses(expenses, expense_types, file_name)
        elif option == 0:
            # exit expense system
            print('Good bye!')
            break


if __name__ == '__main__':
    main()
