from random import choice, randint


def get_response(user_input, mydb_connection, message_author):
    command = user_input.split(" ")[0]
    arguments = " ".join(user_input.split(" ")[1:])

    if command == "hello":
        return "Hello! I'm Mitch"
    elif command == "roll":
        return roll_dice(user_input)
    elif command == "update":
        return update_character(arguments, mydb_connection)
    elif command == "create":
        return create_character(arguments, mydb_connection, message_author)
    elif command == "hold":
        return add_item_holding(arguments, mydb_connection)
    else:
        return choice(["Mitch died", "Go ask Darque", "You don't know what you're saying"])
    # Here is where you add the rest of your logic for the responses


def roll_dice(user_input):
    user_input = user_input.replace("roll", "").strip()
    split_input = [x.strip() for x in user_input.split("+")]

    dice_rolled = []
    total_rolls = []
    modifiers = []

    for i in split_input:
        if "d" not in i:
            modifiers.append(int(i))
            continue

        times = 1
        dice = i[1:]
        if i[0] != "d":
            dice_to_roll = i.split("d")
            times = int(dice_to_roll[0].strip())
            dice = dice_to_roll[1].strip()

        dice = int(dice)
        valid_dice = [4, 6, 8, 10, 12, 20, 100]

        if dice in valid_dice:
            for _ in range(times):
                dice_rolled.append(dice)
                total_rolls.append(randint(1, dice))
        else:
            return f"Something went wrong with your dice roll. Please try again."

    if not dice_rolled:
        return f"You didn't roll any dice. Please try again."

    return (f"Outcome: {sum(total_rolls) + sum(modifiers)} \n"
            f"You rolled {dice_rolled} for {total_rolls}")


def create_character(user_input, mydb_connection, message_author):
    print(user_input)
    print(message_author)

    cursor = mydb_connection.cursor()

    arguments = user_input.split(" ")
    name = arguments[0]
    race = arguments[1]
    char_class = arguments[2]
    level = arguments[3]

    # print(f"player id: {player_id}")

    return "Character created."


def update_character(user_input, mydb_connection):
    print(user_input)

    cursor = mydb_connection.cursor()

    return "Updated Character"


def add_item_holding(arguments, mydb_connection):
    print(arguments)
    return "Item Not Added"
