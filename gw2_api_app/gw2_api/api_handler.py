'''
api_handler.py
'''
import json 
import urllib.parse
import urllib.request 

GW2_API_KEY = 'BB413F8F-F461-9047-AEAC-64285FF120FE7DAD1E31-A4AE-49DD-8DBD-3384085F855C'
GW2_BASE_URL = 'https://api.guildwars2.com/v2/account?access_token='
GW2_WORLDS_URL = 'https://api.guildwars2.com/v2/worlds?id='
GW2_GUILDS_URL = 'https://api.guildwars2.com/v2/guild/'
GW2_GET_GUILDNAME_URL = 'https://api.guildwars2.com/v2/guild/search?name='

def build_search_url(api_key: str): #GW2_API_KEY: str) -> str: 
    '''
    Takes input from the user to build a search URL to access information about the given API key
    
    '''
    return GW2_BASE_URL + api_key 

def search_worlds(world_id: str) -> dict: 
    '''
    Creates a URL to search for a world and its information by world_id
    '''
    return GW2_WORLDS_URL + world_id

def search_guilds(guild_id: str) -> dict: 
    '''
    Creates a URL to search for a guild by guild_id 
    '''
    return GW2_GUILDS_URL + str(guild_id)

def get_guild_id(guild_name: str):
    '''
    Returns a guild's id 
    '''
    guild_name = guild_name.replace(' ', '%20')
    
    return GW2_GET_GUILDNAME_URL + guild_name

def get_response(search_url: str) -> dict:
    '''
    Takes a URL as a parameter and outputs a python dictionary 
    '''
    response = None

    try:
        response = urllib.request.urlopen(search_url)
        return json.load(response)

    except urllib.error.HTTPError:
        print('ERROR: urllib.error.HTTPError found')
        
    finally:
        if response != None:
            response.close()