# The oracle is a discord bot for DND

## Setup

1. Register a new application and bot through the discord developer portal
2. Invite the bot to your server via Oauth2
3. Clone the repository
4. Create a  ```.env``` file with the following contents
    ```
    # .env
    DISCORD_TOKEN=<discord access token>
    DISCORD_GUILD=<server name>
    ```
5. (Optional) Create and launch a python virutal environment

    Linux/Mac

    ```bash
    python3 -m venv <virtual-environment-name>
    source <virtual-environment-name>/bin/activate
    ```

    Windows

    ```power shell
    python3 -m venv <virtual-environment-name>
    set .\<virtual-environment-name>\Scripts\activate.bat
    ```

6. Install dependencies ```pip3 install -r requirements.txt```
7. Run the bot ```python3 bot.py```

## Commands

Roll a D20  
```?roll```  
Generate a swear/insult  
```?swear```  
Summon a monster  
```?monster```  
Generate an encounter  
```?encounter```  
Choose someone from the party at random  
```?who```  
Show a description for an entity  
```?describe <entity>```  
Ask the 8 ball a question  
```?8ball```
List the avaiable encounters and monsters
```?list <monsters|encounters>  