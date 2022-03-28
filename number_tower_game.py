'''
This is Number Tower Game.
'''
import random


def setup_bricks():
    """Creates a main pile of 60 bricks.
    Creates a discard pile of 0 bricks.
    Returns main pile and discard pile
    """
    # set the number of cards
    num_of_cards = 60

    # creates a deck of 60 cards and set it to main_pile
    main_pile = create_deck(num_of_cards)

    # creates an empty list and set it to discard_pile
    discard_pile = []

    # return the tuple
    return main_pile, discard_pile


def shuffle_bricks(bricks):
    """Shuffle the given bricks
    """
    random.shuffle(bricks)


def check_bricks(main_pile, discard_pile):
    """
    Check if there are any bricks left in the given main pile of bricks.
    If not, shuffle the discard pile and move those bricks to the main pile.
    Then turn over the top brick to be the start of the new discard pile.
    """

    # check if the main_pile is empty
    if len(main_pile) == 0:

        # shuffle the discard_pile
        shuffle_bricks(discard_pile)

        # extend the discard_pile to the main_pile
        main_pile.extend(discard_pile)

        # clear the discard_pile
        discard_pile.clear()

        # get the top brick of the main_pile
        top_brick = get_top_brick(main_pile)

        # add the top brick to the empty discard_pile
        add_brick_to_discard(top_brick, discard_pile)


def check_tower_blaster(tower):
    """Checks if stability of the given tower is achieved (bricks in ascending order).
    Returns True if the tower is in ascending order.
    Return False if it is not.
    """

    # creates a sorted tower of the given tower.
    sorted_tower = sorted(tower)

    # if the given tower is the same as the sorted tower, return True. Otherwise return False.
    if tower == sorted_tower:
        return True
    else:
        return False


def get_top_brick(brick_pile):
    """
    Removes and returns the top brick from the given pile of bricks
    """
    return brick_pile.pop(0)


def deal_initial_bricks(main_pile):
    """
    Deal two sets of 10 bricks each from the given main pile.
    Returns a tuple containing two lists, the first one representing the computer's hand,
    and the second one representing the user's hand.
    """
    tower1 = []
    tower2 = []

    # iterate 10 times
    for i in range(10):
        # get the top of the main_pile and insert it to the index=0 in the tower 1.
        tower1.insert(0, get_top_brick(main_pile))
        # get the top of the main_pile and insert it to the index=0 in the tower 2.
        tower2.insert(0, get_top_brick(main_pile))

    return tower1, tower2


def add_brick_to_discard(brick, discard_pile):
    """
    Add the given brick to the top(first) of the given discard pile.
    """
    discard_pile.insert(0, brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard_pile):
    """
    Find the given brick to be replaced in the given tower and replace it with the given new brick.
    Check and make sure that the given brick to be replaced is truly a brick in the given tower.
    The given brick to be replaced then gets put on top of the given discard pile.
    Returns True if the given brick is replaced, otherwise returns False.
    """

    # check if the given brick to be replaced exists in tower
    if brick_to_be_replaced in tower:
        # set the index of the brick_to_be_replaced
        index = tower.index(brick_to_be_replaced)

        # remove that brick from the tower
        tower.pop(index)

        # insert the new brick to the index
        tower.insert(index, new_brick)

        # put the replaced brick to the discard pile and return True.
        discard_pile.insert(0, brick_to_be_replaced)
        return True

    # return False if the given brick to be replaced does NOT exist in tower
    else:
        return False


def computer_play(tower, main_pile, discard_pile):
    """
    Controls the computer play.
    1. If the top brick of the discard pile seems useful, use that brick and replace bricks.
    2. If the top brick of the discard pile doesn't seem useful, check the top brick of the main pile.
    3. If the top brick of the main pile seems useful, use that brick, otherwise skip the turn.
    4. Returns the new computer's tower.
    """

    # set the top brick of the discard pile
    top_discard = see_top_brick(discard_pile)

    # check if the top brick of the discard pile is useful by using the brick_is_useful function
    # if it is useful, use that brick and place it to the expected position by using the find_position_and_replace function
    if brick_is_useful(top_discard, tower):

        # get the top brick of the discard pile
        new_brick = get_top_brick(discard_pile)
        print("The computer picked {} from the discard pile.".format(str(new_brick)))

        # find the position of the new brick and replace.
        find_position_and_replace(new_brick, tower, discard_pile, "discard")
        print("The computer replaced a brick.")

    # if the top brick of the discard pile doesn't seem useful,
    # check the top brick of the main pile and check if that brick is useful.
    else:

        # get the top brick of the main pile
        new_brick = get_top_brick(main_pile)
        print("The computer picked from the main pile.")

        # check if the top brick of the main pile is useful by using the brick_is_useful function
        # if it is useful, use that brick and place it to the expected position by using the find_position_and_replace function
        if brick_is_useful(new_brick, tower):
            find_position_and_replace(new_brick, tower, discard_pile, "main")
            print("The computer replaced a brick.")

        # if the top brick of the discard pile doesn't seem useful,
        # discard the top brick of the main pile and skip the turn.
        else:
            add_brick_to_discard(new_brick, discard_pile)
            print("The computer skipped the turn.")

    print()

    # returns the computer's tower
    return tower


# Personal functions

def print_instruction():
    """
    Prints the welcome message and how to play the game.
    Ask the user to press any key to start the game.
    """
    # print the welcome message
    print("Welcome to Tower Blaster!")

    # print the instruction
    print("-----how to play-----")
    print("You are going to build a tower using bricks numbered from 1 to 60.")
    print("Arrange 10 bricks in your tower from lowerst to highest.")
    print("You are playing with the computer. The first player to get their 10 bricks in order wins.")
    print("In each turn you can choose to pick up the top brick from the discard pile or to pick up the top brick from the main pile.")
    print("Once you choose a brick, you can decide which brick in the tower to replace with the new brick.")
    print("")

    # ask the user to press any key to start the game.
    input("Press any key to start!: ")
    print()


def see_top_brick(brick_pile):
    """
    Returns the top brick from the given pile of bricks
    """
    return brick_pile[0]


def get_position(brick):
    """
    Returns the expected position (0-9) of the given brick
    by calculating the relative position of the given brick in the tower.
    The smaller number should be in higher(earlier) position of the tower,
    and the bigger number should be in lower(later) position of the tower.
    For example, for the brick that is 1-6, return the position of 0,
    for the brick that is 7-12, return the position of 1, and so on.
    """
    # the range of the number of the all bricks
    num_range = 60

    # the number of the bricks in one tower
    num_tower = 10

    # iterate i from 1 to 10
    for i in range(1, num_tower + 1):

        # if the number of the given brick is equal or smaller than i * num_range / num_tower
        if brick <= i * num_range / num_tower:

            # i-1 is the relative position and return it
            position = i - 1
            return position


def brick_is_useful(new_brick, tower):
    """
    Decide if the given brick is useful for the given tower
    by checking if the tower needs the new brick in the position that the given brick would be placed
    or the tower already has a good brick in that position and doesn't need the new brick.
    Return True if the the given brick is useful.
    Return False if the the given brick is not useful.
    """
    # set the position where the new brick would be placed in the tower, using the get_position function.
    position = get_position(new_brick)

    # get what brick is currently in that position.
    current_brick = tower[position]

    # check if the current brick is in the right position using the get_position function.
    # return False if the current brick is already in the right position, because there is no need to replace with the new brick.
    if position == get_position(current_brick):
        return False

    # if the current brick is not in the right position, that means the new brick is useful, therefore return True
    else:
        return True


def find_position_and_replace(new_brick, tower, discard_pile, pile_name):
    """
    Finds the right position for the given new brick using the get_position function
    and replace the current brick to the new brick in the given tower.
    """

    # get the expected position for the given new brick
    position = get_position(new_brick)

    # replace the current brick in that position to the new brick
    find_and_replace(new_brick, tower[position], tower, discard_pile)


def user_play(tower, main_pile, discard_pile):
    """
    Manages the user's play.
    Asks the user if they want to use the discard brick or check the main pile.
    If they want to check the main pile, show the top brick of the main pile and ask if they want to use the main brick or skipp the turn.
    If they decide to use either of the discard brick or the main brick, place that brick to where the user want to place in the tower.
    """

    # print the current tower
    print_user_tower(tower)

    # set the top brick of the discard pile and print it
    top_discard = see_top_brick(discard_pile)
    print("The top brick on the discard pile is " + str(top_discard))

    # ask the user if they want to use the top brick of the discard pile or check the main pile.
    # gets True if they want discard pile, Flase if they want main pile.
    user_input1 = ask_discard_or_main()

    # if the user wants to use the top brick of the discard pile
    if user_input1:
        # ask the user where they want to place the brick and place it there
        place_brick_where_user_wants(top_discard, tower, discard_pile, "discard")

    # if the user wants to check the top brick of the main pile
    else:
        # get the top brick of the main pile and print it
        top_main = get_top_brick(main_pile)
        print("You picked {} from main pile.".format(str(top_main)))

        # ask the user if they want to use the brick or skip the turn
        user_input2 = ask_yes_or_no("Do you want to use this brick? Type 'Y' or 'N' to skip turn: ")

        # if the user wants to use the brick
        if user_input2:

            # ask the user where they want to place the brick and place it there
            place_brick_where_user_wants(top_main, tower, discard_pile, "main")

        # if the user wants to skip the turn
        else:

            # add the top brick of the main pile to the discard pile
            add_brick_to_discard(top_main, discard_pile)

            # print that the user skipped the turn
            print("You skipped the turn.")

    # print the result
    print_user_tower(tower)
    print()


def ask_discard_or_main():
    """
    Asks the user if they want to use the top brick of the discard pile or check the main pile.
    Returns True if the user wants to use the top brick of the discard pile.
    Returns False if the user wants to check the top brick of the main pile.
    """

    # keep asking until we get the expected answer, D or M.
    while True:
        # ask the question and get the user input
        user_input = input("Type 'D' to take the discard brick, 'M' for a mystery brick, or 'H' for help: ")

        # return True if the user inputs 'd' or 'D'
        if user_input.lower() == 'd':
            return True

        # return False if the user inputs 'm' or 'M'
        elif user_input.lower() == 'm':
            return False

        # print help message if the user inputs 'h' or 'H'
        elif user_input.lower() == 'h':
            print("-----help-----")
            print("Type 'D' to use the top brick of the discard pile.")
            print("Type 'M' to check the top brick from the main pile and see if that brick is useful to you.")
            print("You can also discard the main brick and skipp the turn if the top brick is not useful to you.")
            print("--------------")

        # print the message if the user inputs something else.
        else:
            print("Invalid input. Try again.")


def ask_yes_or_no(prompt):
    """
    Prints the given prompt message and asks the user to input either Yes or No.
    Returns True if they say Yes.
    Returns False if they say No.
    Keeps asking until they input valid input.
    """

    # keep asking until we get the expected input
    while True:
        user_input = input(prompt)

        # return true if the user inputs 'y' or 'Y'
        if user_input.lower() == 'y':
            return True

        # return False if the user inputs 'n' or 'N'
        elif user_input.lower() == 'n':
            return False

        # print the message if the user inputs something else.
        else:
            print("Invalid input. Try again.")


def place_brick_where_user_wants(new_brick, tower, discard_pile, pile_name):
    """
    Asks the user where they want to place the brick.
    1. Find that place and replace the current brick to the given new brick.
    2. Remove the replaced brick from the given tower and add to the given discard pile.
    """

    # keep asking until we get the needed information from the user input.
    while True:

        # ask the user which brick to replace
        user_input = input("Where do you want to place this brick? Type a brick number to replace in your tower: ")

        # if the input is a number
        if user_input.isnumeric():
            brick_to_be_replaced = int(user_input)

            # check if the brick exists in the tower and replace it with the new brick
            if find_and_replace(new_brick, brick_to_be_replaced, tower, discard_pile):
                print("You replaced {} with {}.".format(brick_to_be_replaced, str(new_brick)))
                break
            # if the brick doesn't exist in the tower, print the message and go back to the while loop.
            else:
                print("Brick not found in the tower. Try again.")

        # if the user input is not a number, print the message and go back to the while loop.
        else:
            print("Invalid input. Please input numeric number.")


def print_result(count_turn, tower_computer, tower_user):
    """
    Prints the result of the game and the number of turns made.
    """
    if check_tower_blaster(tower_computer):
        print("You lost! The computer won.")
        print_computer_tower(tower_computer)
        print_user_tower(tower_user)
    if check_tower_blaster(tower_user):
        print("Congrats! You won!")
        print_computer_tower(tower_computer)
        print_user_tower(tower_user)

    # print the number of turns made
    print("There were {} turns made in this game.".format(count_turn))


def print_user_tower(tower):
    """
    Prints the given user's tower.
    """
    print("Your tower:\t     ",  tower)


def print_computer_tower(tower):
    """
    Prints the given computer's tower.
    """
    print("Computer's tower:", tower)


def create_deck(num_of_cards):
    """
    Creates a deck of the given number.
    """
    decks = []
    for i in range(1, num_of_cards + 1):
        decks.append(i)
    return decks


def main():

    # sets a flag
    playing = True

    # while the flag is true, starts a new game
    while playing:
        # print welcome message and instruction
        print_instruction()

        # counter to count turns
        count_turn = 0

        # set up the main pile and the discard pile
        main_pile, discard_pile = setup_bricks()

        # shuffle the main pile.
        shuffle_bricks(main_pile)

        # set up the computer's tower and the user's tower
        tower_computer, tower_user = deal_initial_bricks(main_pile)
        print_computer_tower(tower_computer)
        print_user_tower(tower_user)

        # get the top brick of the main pile and add to the discard pile
        add_brick_to_discard(get_top_brick(main_pile), discard_pile)
        print()

        # repeat the turn until either the computer or the user completes the tower
        while True:

            # check the main pile and the discard pile
            check_bricks(main_pile, discard_pile)

            print("COMPUTER'S TURN")

            # the computer's turn to play
            computer_play(tower_computer, main_pile, discard_pile)

            # break the while loop if the computer's tower is completed
            if check_tower_blaster(tower_computer):
                break

            # check the main pile and the discard pile
            check_bricks(main_pile, discard_pile)

            print("NOW IT'S YOUR TURN!")

            # the user's turn to play
            user_play(tower_user, main_pile, discard_pile)

            # increment the turn counter
            count_turn += 1

            # break the while loop if the user's tower is completed
            if check_tower_blaster(tower_user):
                break

        # print the game result
        print_result(count_turn, tower_computer, tower_user)
        print("")

        # ask the user if they want to play the game again
        # if they say yes, pass and start the game again
        if ask_yes_or_no("Do you want to play again? Type 'Y' to play again or 'N' to finish: "):
            pass

        # if they say no, print the message and end the while loop
        else:
            print("The game is now finished! See you!")
            playing = False
        print("")


if __name__ == "__main__":
    main()
