##### Not Financial Advice

# Creating a Telegram Bot to Trigger Bybit Trades

In this project, we'll be creating a Telegram bot that listens to a specific channel for messages. When it receives a message with a specific format, the bot will trigger a trade on Bybit, a cryptocurrency exchange.

To achieve this, we'll be using the 'Telethon' library to create the Telegram bot and the 'Pybit' library to interact with the Bybit API. 

Here are the high-level steps we'll be following:

1. Prepare environment
1. Create a Telegram API Key on 'https://my.telegram.org/auth'.
1. Create a Bybit API Key on 'https://www.bybit.com/app/user/api-management' 
1. Create a 'config.ini' file with the correct input data.
1. Install the necessary libraries (Pybit, Telethon etc.) from requirements.txt
1. Create a client so that the code continues to listen to the channel.
1. Get money hopefully :)

That's the basic outline of what we'll be doing. Of course, there are many details and nuances to each step, but this should give you a good idea of what to expect. Let's get started!

### Prepare environment

1. Download Python from their website. Make sure you have version 3.11 and within the installer choose "ADD TO PATH" <- VERY IMPORTANT! 
1. Download Visual Studio Code from their website. 
1. Download this project as a ZIP.
1. Unzip the project
1. Import it into the IDE (VS Code).
1. Download the Python dependency if nessecary.
1. Create a Virtual environment with VENV if you want for a clean approach <-- optional

### Create the 'config.ini' file
Before we can start, you have to create your own 'config.ini' file. This file protects the developer from pushing valuable API information to the public. 

```
[Telegram]
# no need for quotes
# you can get telegram development credentials in telegram API Development Tools
api_id = 
api_hash = 

# use full phone number including + and country code
phone = 
username = 

#Telegram channel that the script listens to
tg_channel = FOR EXAMPLE (https://t.me/+wdGMdh-9q9Nwerw3)

[bybit]

api_key =
api_secret = 

# Leverage for longing/shorting
buyLeverage = 5
sellLeverage = 5

# Do you want to keep the position open perpetually or with a timer to snipe the Rose fan base? 
# Values are <True> or <False> Capital letter is important. 
withTimer = True

# 60 == 1 minute, 120 == 2 minutes etc. Time in seconds.
seconds_to_keep_trade_open = 10

# 1.0 = 100%, 0.5 = 50% ---> Keep this number float, so there won't be any data issues.
portfolioPercentage = 0.2

# Use 0 if you don't want any predefined SL or TP
# Percentage of TP and SL on token price. So if ETH price = 1000, and TP = 1.1 TP price => 1100. For stopLoss it could be 0.9 => 900
# FOR THE BUY TRADES

takeProfit_long = 1.1
stopLoss_long = 0.9

# Percentage of TP and SL on token price. So if ETH price = 1000, and TP = 0.9 TP price => 900. For stopLoss it could be 1.1 => 1100
# FOR THE SELL TRADES

takeProfit_short = 0.9
stopLoss_short = 1.1

```

### Create a Telegram API Key
In this paragraph I will show how to create an API key on Telegram:


1. Log-in on 'https://my.telegram.org/auth' 
2. Click on 'API Development Tools'
3. Give your bot a nice name. 
4. Copy your API-Key and API-Hash to the corresponding fields in the config.ini file.
5. We've gathered all information we need from Telegram.

### Create a Bybit API Key
In this paragraph I will show how to create an API key on Telegram:

1. Log-in on (https://www.bybit.com/app/user/api-management) 
2. Click on 'Create New Key'. 
3. We are going to use the API for API transaction
4. Give Read-Write permissions
5. Optionally, you can give your IP Address up, for extra security (from https://whatismyipaddress.com/)
6. Select the permissions corresponding the image below.
7. Copy your API-Key and API-Hash to the corresponding fields in the config.ini file.
8. We've gathered all information we need from Telegram.

<img src="images\bybitAPI_perms.png">

### Fill the 'config.ini' file with the correct input data.
We are almost there!

if you followed up with the steps above, both the API-keys and secrets should be filled. The next step is to also fill the remaining telegram information. You can also edit all the other preferences. For example, the bot will use 20% of the USDT available for one trade.

### Install the necessary libraries (Pybit, Telethon etc.) from requirements.txt
Run the following command in your terminal: 

```
pip install -r requirements.txt
``` 
You can of course choose to create a virtual environment first for a clean install. 

### Run the python code 'TelegramChatListener'
As the title states, run the code. You might want to start with a test group in your config.ini and try it yourself.

