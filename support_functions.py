from random import randint


def roll_dice(user_input):
    user_input = user_input.replace("roll", "").strip()
    # FIXME doesn't work if the user has a negative modifier
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


def display_holding(mydb_connection):

    cursor = mydb_connection.cursor()
    cursor.execute("SELECT * FROM bag_of_holding")
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "Nothing in the Bag of Holding"
    msg = "The bag of holding has:"
    for row in rows:
        msg += f"\n- {row[1]}"

    return msg


def add_item_holding(arguments, mydb_connection):
    cursor = mydb_connection.cursor()

    cursor.execute("INSERT INTO bag_of_holding (item) VALUES (%s)", [arguments])
    mydb_connection.commit()
    return f"{arguments} Added"


def remove_item_holding(arguments, mydb_connection):
    cursor = mydb_connection.cursor()
    cursor.execute("DELETE FROM bag_of_holding WHERE item = %s", [arguments])
    mydb_connection.commit()
    return f"{arguments} Removed"


