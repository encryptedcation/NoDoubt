import discord
import os
import requests
import base64
import random

async def gutenDex(queries, author, channel):
    name = "Project Gutenberg"
    url="https://www.gutenberg.org/"
    icon_url= "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Project_Gutenberg_logo.svg/1200px-Project_Gutenberg_logo.svg.png"
    
    if queries == '0':
        url = f"http://gutendex.com/books?page={str(random.randrange(1,100))}"
    else:
        url = f'http://gutendex.com/books?search={queries}'
        
    req = requests.get(url)
  
    if req.status_code == requests.codes.ok:
        req = req.json()
        content = (req["results"])
        titles = []
        links = {}
      
        for item in content:
          
          mytitle = item['title']
          mylinks = item['formats']
          titles.append(mytitle)
          links[mytitle] = mylinks
          
        res = ''
        if len(titles) == 0:
            await channel.send('**Sorry. No results found.**')
        else:
            for i in  range(len(titles)):
                res += f'{i+1}. {titles[i]}\n'
            embed = discord.Embed(title = "Available Books", description = res)
            embed.set_author(name = name, url = url, icon_url = icon_url)
            await channel.send(embed=embed)
            n = await client.wait_for('message', check=check(author), timeout=30)
            n = int(n.content)
            printstr  = ''
            
        for x in links[titles[n-1]]:
            printstr+= f'{x} : {links[titles[n-1]][x]}\n'
        embed2 = discord.Embed(title = titles[n-1], description = printstr)
        embed2.set_author(name = name, url = url, icon_url = icon_url)
        await channel.send(embed=embed2)

    else:
        channel.send("Project Gutenberg not available :(")

def resources():
    url = "https://api.github.com/repos/aflah02/SemWiseResourcesIIIT/contents/README.md"
    req = requests.get(url)

    if req.status_code == requests.codes.ok:
        req = req.json()
        content = base64.b64decode(req["content"]).decode("utf-8")
    else:
        content = "404 Repository Not Found"

    return content


def courses():
    content = resources()
    headings = []

    for x in content.splitlines():
        if x[0:3] == "###":
            if "Special" not in x:
                headings.append(x[4:].strip())

    return headings


def getCourseContent(course):
    content = resources()
    if course in courses():
        lines = content.splitlines()
        start = 0
        resourceList = []
        for i in range(len(lines)):
            if course in lines[i] and "###" in lines[i]:
                start = i
        resourceList.append(lines[start])
        start += 1
        while True:
            if lines[start][0:1] != "#":
                resourceList.append(lines[start])
                start += 1
            else:
                break
        return resourceList
    else:
        return [
            "Invalid Course Name. Use only the course names mentioned when you run `$resources`"
        ]


def xkcd():
    url = f"https://xkcd.com/{random.randrange(0, 2500)}/info.0.json"
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        title = req['title']
        transcript = req["alt"]
        image = req['img']
        return title, transcript, image
    else:
        return "xkcd is temporarily down :("

def b99Quotes():
    url = "https://brooklyn-nine-nine-quotes.herokuapp.com/api/v1/quotes/random"
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        content = req["Data"]["QuoteText"]
    else:
        content = "Quotes system is temporarily down :("
    return content

def check(author):
    def inner_check(message): 
        if message.author != author:
            return False
        try: 
            int(message.content) 
            return True 
        except ValueError: 
            return False
    return inner_check

def mydef(word):
  url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
  req = requests.get(url)
  if req.status_code == requests.codes.ok:
      req = req.json()
      content = req[0]["meanings"][0]['definitions'][0]['definition']
      return content
  else:
      content = "Definition not available."
      return content

def memes():
    url = "https://meme-api.herokuapp.com/gimme/wholesomememes"
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        meme_heading = req['postLink']
        title = req['title']
        author = req['author']
        image = req["url"]
        return meme_heading, image, author, title
    else:
        return 'Sorry. Memes are currently unavailable. Must suffer a memeless existence.'


class MyClient(discord.Client):

    
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
        await self.change_presence(activity = discord.Game(name="$help"))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("$resources"):
            title="SemWiseResourcesIIIT"
            url="https://api.github.com/repos/aflah02/SemWiseResourcesIIIT/contents/README.md"
            if len(message.content.split()) == 1:
                embed = discord.Embed(
                    title=title,
                    url=url,
                    description=
                    ("Here are the following courses for which resources are present. To access resources for a specific course, type `$resources <coursename>`\n\n"
                     + '\n'.join(courses())))

            elif len(message.content.split()) >= 2:
                embed = discord.Embed(
                    title=title,
                    url=url,
                    description=('\n'.join(
                        getCourseContent(' '.join(
                            message.content.split()[1:])))))
            embed.set_author(
                name="aflah02",
                url="https://github.com/aflah02",
                icon_url=
                "https://avatars.githubusercontent.com/u/72096386?v=4")
            await message.channel.send(embed=embed)
                
        if message.content.startswith("$xkcd"):
            res = xkcd()
            embed = discord.Embed(
              title=res[0],
              description=res[1])
            embed.set_image(url=res[2])
            embed.set_author(name="xkcd", url = "https://xkcd.com", icon_url = "https://camo.githubusercontent.com/59039af436c3ada34ebad55ae1afa3664926c8f520ae81e177844cbadedfbcc7/68747470733a2f2f776562636f6d6963736875622e636f6d2f75706c6f6164732f776562636f6d6963732f786b63642d3132383078313032342e706e67")
            await message.channel.send(embed=embed)
          
        if message.content.startswith('$b99'):
            await message.channel.send("_" + b99Quotes() + "_")
          
        if message.content.startswith('$getbook'):
            x = message.content.split()
            
            if len(x) == 1:
                await gutenDex(queries= '0', author=message.author, channel=message.channel)
           
            else:
                quer = x[1:]
                quer = str('%20'.join(quer))
                await gutenDex(queries=quer, author=message.author, channel=message.channel)
              
        if message.content.startswith("$memes"):
            res = memes()
            embed = discord.Embed(
              title=res[0],
              description=f'title: {res[3]} \n author: {res[2]}')
            embed.set_image(url=res[1])
            await message.channel.send(embed=embed)
            
        if message.content.startswith("$help"):
            help = '''
            1. `$memes`: Gets random wholesome memes from Reddit.
            2. `$xkcd`: Gets a random XKCD comic.
            3. `$resources`: Gets list of courses for which resources are available from Aflah's Github repo. Use `$resources <coursename>` to get resources for the specific course.
            4. `$b99`: Gets a random dialogue from Brooklyn Nine Nine.
            5. `$getbook`: Gets 32 random books from Project Gutenberg. Select a book by entering its number to get the links for the book.
                Note: You can use `$getbook <bookname>` to find a specific book.
            6. `$define <word>:` Gets the definition of the word.
            7. `$help`: Returns this menu.
            '''
            embed = discord.Embed(title = 'Help',
                description=help)
            await message.channel.send(embed=embed)
          
        if message.content.startswith("$define"):
            content = message.content.split()
            my_word = content[1]
            res = mydef(my_word)
            embed = discord.Embed(
              title=my_word,
              description = f'_{res}_'
            )
            await message.channel.send(embed=embed)

          
client = MyClient()
client.run(os.getenv("TOKEN"))