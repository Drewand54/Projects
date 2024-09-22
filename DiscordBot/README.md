# DrewBot
#### Video Demo: https://youtu.be/yXhT7lDyYxM
#### Description:


# Start: I had to create a bot in the discord developer portal and give it administrative commands. I had to install a program called nextcord in VS Code to get access to some discord functions and bot commands. Their documentation was extremely helpful in creating my project. I also had to install asyncio which gave me access to async and await which were very important when waiting for data to return from APIs.


# config.py: This holds my discord bot access token. I left it out in my final submission, but that is all the config is used for.


# main.py: This contains many imports and instantiates my intents and bot. In this file I create my bot command (! in this case), I send myself a notification when my bot is online, and I load my cogs file. The main.py file is the file that gets run, but all my commands are contained in my cogs folder, in basic.py. This is just for organization purposes.


# !info: This returns a list of all the commands that the bot can execute as well as instructions for how to use them. This is what every user should start with when learning what the bot can do.


# !ping: This is the first command I wrote. I needed to make sure my bot could receive messages and send some of its own.


# !video: First, I read the documentation of youtube's API call. It returns a JSON, so I had to import JSON and find out how to open JSON files in python. The API took in a video search as its parameter and I was able to limit the results to just 1 video. I used *args to collect all the info typed after the !video command in order to find what the user wanted to search. If there were spaces, I replaced them with +'s, and put that into the API, returning the top video. This first command created the layout I would use for most of the other commands on this list.


# !photo: I used pexel's API to return an image based on a search. This works very similarly to Youtube's API.


# !music: Spotify's API was very complicated. They removed all the old documentation they used to have containing their examples, as well as an easy way to obtain your access key. I spent a long time searching for their old documentation and eventually found it through many videos and images online. The access key refreshes every hour, so I made sure to check and retrieve mine every time the command was called. I struggled to combine search query filters, but found out that they are separated via %20. Once I had that, I was able to form my API call. I then searched the user's message to determine whether or not they used an artist name (Checking for the keyword 'BY'). If it was there, I called using a title and artist, if it was not provided, I called the API with only a title, the drawback being less accuracy in finding the song you want. (Bones, for example, is the name of a song by Imagine Dragons and by Crumb). The API did not return a link, but rather a song ID. I combined this with a spotify url and returned that to the user.


# !stock: I found a stock API that when given a symbol, returns current data regarding that stock. I picked the data that I wanted and formed a discord embed. This embed creates a nice format for the information to be returned in. I checked the first character of the change percent to see if it was '-' or not. If the stock was down (contained '-'), the embed was red, otherwise, it was green (I didn't need to check if it was 0 because stocks are always classified as either up or down).


# !weather: This API took in a city and returns a lot of data on the weather. I chose a few I thought were important, embedded them, and returned it to the user. I had to take in multiple arguments for this call because not all cities are one word. For example, I live in Phoenix, but others might be from New York City.


# !define: This dictionary API returns a lot of information about a word including its definition, origin, example, pronunciation, and parts of speech. This call was more difficult than I at first thought because a word can have more than 1 part of speech. For example the word well, has 5. I took the length of the parts of the speech list and looped over that amount, embedding the info I wanted. That way, I could include all of the parts of speech of any word, regardless of how many it had. (This is key as words have very different meanings based on their part of speech. The noun well is a hole in the ground filled with a liquid while it's adjective is to be in good health)


# !wiki: This API searches wikipedia. If there is an article that matches what the user typed, it will return the link to it.


# Passive anti-cursing: This was not a command that the user had to type, but instead a listener. It checks the content of every message sent by anyone on the server. If the message contains a word in a curseWords list, then that message is to be deleted. This was very difficult to create. I could not use the *args parameter like I used before because it did not save the id of the message. In other words, while it returned a string which I can check, I had no way of deleting the message. I had to use the message parameter instead. This was not perfect either though, since if the message.content couldn't be checked, it would result in an error. Such was the case for objects sent to the server. The bot returned objects rather than messages like users. This would create an error and skip any info that the bot tried to send. To get around this, I had to check if the message was sent by a person, or the bot (I did this by checking their ID's). If it was sent by the bot, the listener would just return. If it was sent by a person, then and only then would its content be checked.


# Design choices: I decided to delete the user's command once the bot returns the information. This keeps the messaging space tidy and less cryptic looking. Embed colors were largely determined by their purpose. I thought stock colors should match whether they are up or down. Information being yellow and Youtube being red also made sense to me. I was debating whether or not to add the !music function considering Youtube has almost every song available. I decided to add it because spotify audio files are bigger and sound better than Youtube's compressed versions, and because many people might prefer sharing just music back and forth rather than finding good youtube clips.

