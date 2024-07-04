import mysql.connector

from player import Player
from character import Character, CharacterClass, Race, race_enum_mapping, class_enum_mapping


def create_tables(cursor, mydb):
    # Create the players table
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                player_id INT AUTO_INCREMENT PRIMARY KEY,
                player_name VARCHAR(255) NOT NULL,
                discord_username VARCHAR(255) NOT NULL
            )
        """)

    # Create the characters table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS characters (
            character_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            race ENUM('Human', 'Elf', 'Dragonborn', 'Aasimar') NOT NULL,
            class ENUM('Rogue', 'Wizard', 'Barbarian', 'Paladin') NOT NULL,
            player_id INT,
            FOREIGN KEY (player_id) REFERENCES players(player_id)
        )
    """)

    # Create the "bag_of_holding" table if it doesn't exist
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS bag_of_holding (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    item VARCHAR(255) NOT NULL,
                    quantity INT NOT NULL DEFAULT 1,
                    description VARCHAR(255)
                )
            """)

    mydb.commit()
    print("All tables were created successfully")

# def setup_characters(character, cursor, mydb):
#     mysql_race = race_enum_mapping[character.race]
#     mysql_char_class = class_enum_mapping[character.char_class]
#
#     cursor.execute("""
#         INSERT INTO characters (name, race, class, player_id)
#         VALUES (%s, %s, %s, %s)
#     """, (character.name, mysql_race, mysql_char_class, character.player_id))
#
#     mydb.commit()
#
#     print('Inserted Character')
#

# def setup_player(player, cursor, mydb):
#     cursor.execute("""
#         INSERT INTO players (player_name, discord_username)
#         VALUES (%s, %s)
#     """, (player.player_name, player.discord_username))
#
#     mydb.commit()
#
#     print('Inserted Player')
