
def get_player_id(discord_username, mydb_connection):
    query = "SELECT players.player_id FROM players WHERE players.discord_username = %s"
    cursor = mydb_connection.cursor()
    cursor.execute(query, (discord_username,))

    print("Getting result")
    result = cursor.fetchone()
    print("Result is", result)