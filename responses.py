from random import choice

from constants import COMMAND_HELP_MSG
from support_functions import roll_dice, remove_item_holding, add_item_holding, display_holding


def get_response(user_input, mydb_connection, message_author):
    command = user_input.split(" ")[0]
    arguments = " ".join(user_input.split(" ")[1:])

    match command:
        case "hello":
            return "Hello! I'm Mitch"
        case "roll":
            return roll_dice(user_input)
        # case "update":
        #     return update_character(arguments, mydb_connection)
        # case "create":
        #     return create_character(arguments, mydb_connection, message_author)
        case "bag":
            return display_holding(mydb_connection)
        case "hold" | "add":
            return add_item_holding(arguments, mydb_connection)
        case "remove":
            return remove_item_holding(arguments, mydb_connection)
        case "help":
            return COMMAND_HELP_MSG
        case _:
            return choice(["Mitch died", "Go ask Darque", "You don't know what you're saying"])
