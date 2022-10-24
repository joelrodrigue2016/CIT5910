import random

"""
General strategy:

The following are the functions that we will use to build our program and them we will combine them, use them and run them 
through the main function.
➔ shuffle(bricks)d

➔ check_tower_blaster(tower) d

➔ get_top_brick(brick_pile) d

➔ deal_initial_bricks(main_pile) d

➔ add_brick_to_discard(brick, discard) d

➔ find_and_replace(new_brick, brick_to_be_replaced, tower, discard)d

➔ computer_play(tower, main_pile, discard)d

"""

""" These are the required functions"""


def shuffle_bricks(bricks):
    """
    Shuffle the bricks (represented as a list) to start the game.
    This function does not return anything, and we are using oner of the allowed libraries(random)
    to shuffle the bricks randomly.
    """
    random.shuffle(bricks)


def check_tower_blaster(tower):
    """
    Given a tower (the user’s or the computer’s list), determine if stability has been achieved.
    Remember that stability means that the bricks are in ascending order.
    This function returns a boolean value, True or false.
    """

    expected_value = tower.copy()
    expected_value.sort()

    if tower == expected_value:
        return True
    # if not the expected value return the boolean value False.
    else:
        return False


def get_top_brick(brick_pile):
    """
    Remove the top brick from any pile of bricks. This can be the main_pile, discard, or your
    tower or the computer's tower. In short, the first element of any list.
     So, it is used at the start of game play for dealing bricks. This same function will also be
     used during each player’s turn to take the top brick from either the discarded brick pile or
     from the main pile. This function must return an integer.
    """
    return int(brick_pile.pop(0))


def deal_initial_bricks(main_pile):
    """Start the game by dealing two sets of 10 bricks each."""

    # The method of returning 2 things from a function is to make a tuple out of the return values.
    computer_pile = list()
    player_pile = list()
    # Start the game by dealing two sets of 10 bricks each.
    for time in range(10):
        computer_pile.insert(0, main_pile.pop(0))
        player_pile.insert(0, main_pile.pop(0))

    return computer_pile, player_pile


def add_brick_to_discard(brick, discard):
    """
    Add the brick (represented as an integer) to the top of the discard pile (which is a list).
    This function does not return anything.
    """
    discard.insert(0, brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """
    Find the brick to be replaced (represented by an integer) in the tower and replace it with
    new_brick.
    The replaced brick then gets put on top of the discard pile.
    Check and make sure that the brick_to_be_replaced is truly a brick in the hand. If the
    user accidentally typed a brick number incorrectly, just politely tell them to try again and
    leave the hand unchanged.

"""

    try:
        tower[tower.index(brick_to_be_replaced)] = new_brick
        add_brick_to_discard(brick_to_be_replaced, discard)
        return True
    ## if failed, print the warning and turn False
    except:

        print("-------------------------------------")
        print("Wrong brick number, please try again")
        print("-------------------------------------")
        return False


def computer_play(tower, main_pile, discard):
    """
    Strategy for the computer

    The computer on its own will build a set of bricks going from 1 through 50.
    Anything beyond 50 will be discarded and then. When the discarded pile becomes
    greater than the main pile, it will go straight to the main pile.

    The computer will take the top discarded brick and replace one of the bricks from the
    main pile with the discarded pile, very similar to the way it is shown in the actual
    online game.

    On the other hand if the pile happens to be smaller, then the computer will take the immediate brick that is
    larger and swap it with the discarded brick. These parameters can be changed by the programmer by making the set
    smaller (less competitive) or larger(more competitive)



    """

    if tower[0] > 50:
        ## replace and discard the top brick
        if discard[0] <= 50:
            find_and_replace(get_top_brick(discard), tower[0], tower, discard)
        # Try going back to the main pile if the top is too large
        else:
            new_brick = get_top_brick(main_pile)
            # put its top brick to the tower top if it is less than 51
            if new_brick <= 50:
                find_and_replace(new_brick, tower[0], tower, discard)
            else:
                add_brick_to_discard(new_brick, discard)

    else:
        ## take the brick from the top of the discarded pile,
        new_brick = get_top_brick(discard)

        i = 1
        while tower[i - 1] < tower[i]:
            i += 1
            if i == 9:
                break

        if new_brick > max(tower[:i]):

            find_and_replace(new_brick, tower[i], tower, discard)

        else:
            j = 0
            ##find and replace the first larger one
            while True:
                if new_brick < tower[j]:
                    find_and_replace(new_brick, tower[j], tower, discard)
                    break
                j += 1


# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*


def get_the_correct_input():
    """This function ensures that the input is an integer since by default it is always a string
       Also the game keeps running even if the user puts in the wrong value
    """

    while True:
        try:
            return int(input(":- "))
        except Exception as e:
            print("Please input an integer number!!")


def take_discarded_pile(tower, discard):
    """Return true if the pile of bricks is taken"""

    new_brick = get_top_brick(discard)

    while True:
        print("Your tower is:", tower)
        ##prints the retrived brick and the instruction
        print("****************************************************************************************")
        print("The top of the discarded pile is: " + str(new_brick))
        print("Please, carefully enter the number of the brick in your tower you want to replace,")
        print("You may also input 0 to see the top brick of the main pile:")
        print("****************************************************************************************")
        scanner = get_the_correct_input()

        if scanner != 0:
            if find_and_replace(new_brick, scanner, tower, discard):
                return True
        else:
            add_brick_to_discard(new_brick, discard)
            return False


def take_main_pile(tower, main_pile, discard):
    """Execute the player's action on the main_pile, no return"""
    new_brick = get_top_brick(main_pile)
    while True:
        print("Your tower is:", tower)
        print("The top of the main pile is: " + str(new_brick))
        print("Please enter the integer number of the brick in your tower you want to replace,")
        print("or enter 0 to place it on the top of the discard pile:\n")
        scanner = get_the_correct_input()

        if scanner != 0:

            if find_and_replace(new_brick, scanner, tower, discard):
                break


        else:
            print("There is no change on your tower in this move.")
            add_brick_to_discard(new_brick, discard)
            break


def player_play(tower, main_pile, discard):
    """ Presents the game to the player"""

    print("----------------------------------------------------------------------------------------")
    print("YOUR TURN")
    if not take_discarded_pile(tower, discard):
        take_main_pile(tower, main_pile, discard)
    # show results of the tower
    print("Now your tower is:", tower)
    print("Now the top of discard pile is", discard[0])


def check_bricks(main_pile, discard):
    """starts a new pile if none exist"""
    if len(main_pile) == 0:
        shuffle_bricks(discard)
        main_pile[0:] = discard
        discard.clear()
        add_brick_to_discard(get_top_brick(main_pile), discard)


def instructions():
    # game instructions
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||   TOWER BLASTER   |||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("")
    print("-General instructions")
    print("- A Tower Blaster game starts with a pile of 60 bricks, each numbered 1 to 60Think of the numbers on")
    print("the bricks as the width of the bricks. The objective is to be the first player to arrange the 10 bricks in")
    print("your tower from lowest to highest (because the tower will be unstable otherwise).")
    print("The bricks in the pile are shuffled at the start and both the user and the computer are dealt 10 bricks")
    print("from the main pile. As a player receives each brick, they must place it on top of their current tower in")
    print("the order it is received. Yes, initially your tower is likely to be unstable.")
    print("After the first 10 bricks are dealt, there will be 40 bricks remaining in the main pile. The top brick of the")
    print("main pile is turned over to begin the discarded brick pile.")
    print("")
    print("On each player’s turn, the player chooses to pick up the top brick from the discard pile or to pick up the")
    print("top brick from the main pile. The top brick from the discard pile is known. In other words, the discard")
    print("file is ‘face up’ and everyone knows how wide the top brick is. The main pile is ‘face down’. Choosing")
    print("the top brick from the main pile can be risky because the player does not know what the brick is and the")
    print("brick cannot be put back down onto the main pile.")
    print("")
    print("Once a player chooses a brick, either from the discard pile or the main pile, the player decides where in")
    print("the tower to put the brick. The tower is always 10 bricks high, so placing a brick means that an existing")
    print("brick in the tower is removed and replaced with the new brick.")
    print("If the player takes a brick from the main pile (the one that is ‘face down’), the player can reject it and")
    print(
        "place it in the discard pile. This means that nothing in that player’s tower changes during that turn. If the")
    print(
        "player takes a brick from the discard pile (the one that is ‘face up’), the player MUST place it into the tower.")
    print("The first player to get their 10 bricks in order wins.")


"""This is the main function where everything will be run through"""


def main():
    instructions()
    # empty list for the discarded bricks
    discard = []
    # main pile consist of 60 bricks even though for the purpose of the game only 10 are shown at random
    main_pile = list(range(1, 61))
    # now we shuffle the piles at random with the shuffle function that was created previously
    shuffle_bricks(main_pile)  # range 1:60
    computer_tower, player_tower = deal_initial_bricks(main_pile)
    add_brick_to_discard(get_top_brick(main_pile), discard)

    print("Game starts now!!!!")

    while True:
        ##computer's move and evaluation
        check_bricks(main_pile, discard)
        print("----------------------------------------------------------------------------------------")
        print("Computer's turn...")
        computer_play(computer_tower, main_pile, discard)
        if check_tower_blaster(computer_tower):
            print("SORRY, YOU LOST, BETTER LUCK NEXT TIME ")
            break

        ##player's move and evaluation
        check_bricks(main_pile, discard)
        player_play(player_tower, main_pile, discard)
        if check_tower_blaster(player_tower):
            print("CONGRATULATIONS!!!!!! YOU WON!!")
            break

    ##print the computer's tower
    print("The computer's tower now is:", computer_tower)


if __name__ == "__main__":
    main()
