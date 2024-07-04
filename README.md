# Mitch Bot
A Discord bot built with discord.py for rolling dice and managing Dungeons & Dragons campaigns. It will also connect to a local MySQL database to manage different elements of your campaign.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
  - [Dice Rolling](#dice-rolling)
  - [Character Management (Work in Progress)](#character-management-work-in-progress)
- [Contributing](#contributing)
- [License](#license)
  
## Installation

1. Make sure you have Python 3.12 or later installed.
2. Clone the repository: `git clone https://github.com/rdmoustafa/mitch.git`
3. Navigate to the project directory: `cd mitch`
4. Install the required dependencies `pip install -r requirements.txt`. This will install discord.py and pandas.
5. Create a new Discord bot and obtain the bot token from the Discord Developer Portal.
6. Create a `.env` file in the project directory 
   1. Add your bot token: `DISCORD_BOT_TOKEN=your-bot-token-here`

   _For the following, include them if you have different values to the default_
   
   2. Add your MySQL Server host: `DB_HOST=your-host-name-here`. It will be localhost by default
   3. Add your database name: `DATABASE=your-database-name-here`. It will be dungeons_and_dragons by default
   4. Add your username: `DB_USER=your-username-here`. It will be root by default
   5. Add your password: `DB_PASSWORD=your-password-here`. It will be empty by default

## Usage
1. Run the bot: `python main.py`
2. Invite the bot to your Discord server using the provided invite link 
3. Use the available commands in your server's text channels or direct messages.

## Commands

### Dice Rolling

- `#roll 2d6` - Rolls two six-sided dice and displays the result.
- `#roll 4d8+2` - Rolls four eight-sided dice, adds 2 to the total, and displays the result.

### Character Management (Work in Progress)


## Contributing

Contributions are welcome! If you find any issues or have suggestions for new features, please open an issue on the GitHub repository. If you'd like to contribute code, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Open a pull request against the main repository.

## License

This project is licensed under the MIT License.
