# NoDoubt
Made by @cation03 (Ananya Goyal, 2021011) and @sociallyencrypted (Mehul Arora, 2021066).


NoDoubtBot is a discord bot with various resources to help you with your academic life, and gives you bite sized memes aand quotes to help you relax when you're tired!

## Resources
- [GutenDex API](http://gutendex.com/)
- [XKCD-API](https://xkcd.com/json.html)
- [SemWiseResourcesIIIT by aflah02](https://github.com/aflah02/SemWiseResourcesIIIT)
- [Brooklyn Nine Nine Quotes](https://github.com/Labocania/Brooklyn-99-Quotes-Api)
- [Discord.py: API Wrapper for Discord Bots](https://discordpy.readthedocs.io/en/stable/)
- [Meme-API](https://github.com/D3vd/Meme_Api)
- [Dictionary-API](https://dictionaryapi.dev/)

## Demo Server
You can test the bot on a [demo server](https://discord.gg/fEhhTAsuXA) we have created.

## Commands

1. `$memes`: Gets random wholesome memes from Reddit.
2. `$xkcd`: Gets a random XKCD comic.
3. `$resources`: Gets list of courses for which resources are available from Aflah's Github repo. Use `$resources <coursename>` to get resources for the specific course.
4. `$b99`: Gets a random dialogue from Brooklyn Nine Nine.
5. `$getbook`: Gets 32 random books from Project Gutenberg. Select a book by entering its number to get the links for the book. Note: You can use `$getbook <bookname>` to find a specific book.
6. `$define`: (Use `$define <word>`) Returns the definition of the word.
7. `$help`: Returns this menu.


## Note
API token has to be stored in a `.env` file as an environment variable called `TOKEN`

## Installation

- Create an account on the [Discord Developer Portal](https://discord.com/developers).
- Create a new Application.
- Create a new bot from the Bot tab.
- Create a server on discord to test your bot.
- On the Developer Portal, go to OAuth2 -> URL Generator.
- Click `bot` in the Scopes section, and `Send Messages`, `Send Messages in Threads`, `Send TTS Messages`, `Embed Links`, and `Attach Files` in the Permissions section.
- Use the generated link to add the bot to your server.
- Copy the API token for the bot from the Token section in the Bot tab.
- Save the token as `TOKEN=<insert token here>` in a `.env` file in your working directory.
- Install the prerequisite libraries:
    - `python3 -m pip install -U discord.py`
    - `python3 -m pip install requests`
- Run bot.py.
- Message `$help` in a channel in your server to get the list of commands.

## Thanks
We would like to thank @aflah02 for allowing us to use his resources repository in our project.