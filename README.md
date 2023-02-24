# Creating a Telegram Bot to Trigger Bybit Trades

In this project, we'll be creating a Telegram bot that listens to a specific channel for messages. When it receives a message with a specific format, the bot will trigger a trade on Bybit, a cryptocurrency exchange.

To achieve this, we'll be using the 'Telethon' library to create the Telegram bot and the 'Pybit' library to interact with the Bybit API. 

Here are the high-level steps we'll be following:

1. Create a Telegram API Key on 'https://my.telegram.org/auth'.
1. Create a Bybit API Key on 'https://www.bybit.com/app/user/api-management' 
1. Create a 'config.ini' file with the correct input data.
1. Install the necessary libraries (Pybit, Telethon etc.) from requirements.txt
1. Create a client so that the code continues to listen to the channel.
1. Get rich :)

That's the basic outline of what we'll be doing. Of course, there are many details and nuances to each step, but this should give you a good idea of what to expect. Let's get started!

### Create the 'config.ini' file
Before we can start, you have to create your own 'config.ini' file. This file protects the developer from pushing valuable API information to the public. 


### Create a Telegram API Key
In this paragraph I will show how to create an API key on Telegram:

1. Log-in on 'https://my.telegram.org/auth' 
1. Click on 'API Development Tools'
1. Give your bot a nice name.

<img src="path/to/image.jpg">