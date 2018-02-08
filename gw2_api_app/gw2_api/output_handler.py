'''
Created on Jan 31, 2018

@author: Emery
'''
import api_handler

class Account: 
    def __init__(self):
        pass
        
    def account_years(self, results: dict) -> str:
        '''
        Converts hours to years
        '''
        SEC_TO_YR = (365*24*60*60) #days*hours*minutes*seconds
        account_hours = int(results['age'])
        years = round(10*(account_hours/SEC_TO_YR), 3)
        return str(years) + ' years'
        
    
    def account_created_on(self, results: dict) -> str: 
        '''
        Displays date in format: XXXX/XX/XXX (year/month/day)
        '''
        account_created = results['created']
        account_creation_date = account_created[:10]
        return account_creation_date
    
    def world_info(self, results: dict):
        world_id = str(results['world'])
        world_results = api_handler.get_response(api_handler.search_worlds(world_id))
        world_name = world_results['name']
        world_population = world_results['population']
        return world_name + '\nWorld Population: ' + world_population
        
    
    def print_info(self, results: dict) -> str: 
        '''
        Gets account information and prints it to the terminal
        
        '''
        account_name = results['name']
        account_games = results['access']
        commander = results['commander']
        fractal_level = results['fractal_level']
        wvw_rank = results['wvw_rank']
        
        
        
        print('Account name:', account_name)
        print('Account age:', self.account_years(results))
        print('Home World:', self.world_info(results))
        print('Account guilds:', Guild.get_guild_names(self, results['guilds']))
        print('Account created on:', self.account_created_on(results))
        print('Account games:', account_games)
        print('Commander:', commander)
        print('Fractal level:', fractal_level)
        print('WvW rank:', wvw_rank)
        
    def character_info(self, results: dict) -> str: 
        pass 
    
class Guild:
    def __init__(self):
        pass
    
    def get_guild_names(self, guild_ids: list):
        guild_list = []
        for guild in guild_ids: 
            guild_results = api_handler.get_response(api_handler.search_guilds(guild))
            guild_name = guild_results['name']
            guild_list.append(guild_name)
        return guild_list 
    
    def print_info(self, results: dict):
        guild_ids = results['guilds']
        guild_list = self.get_guild_names(guild_ids)
        self.guild_menu(guild_list) 
        
    def print_guilds(self, guild_dict: dict) -> str:
        '''
        Prints out a list of all guilds the user is in 
        '''
        for key, value in guild_dict.items():
            print('  ' + str(key) + '. ' + value)
        
    def get_guild(self, guild_list):
        '''
        Prompts user for a specific guild to get info on
        '''
        guild_dict = {}
        print('Guild list: ')
        for num in range(1, len(guild_list)+1):
            guild_dict[num] = guild_list[num-1]
        self.print_guilds(guild_dict)
        user_choice = int(input('\nWhich guild would you like to get information on: '))
        return guild_dict[user_choice] 
        
    def guild_menu(self, guild_list):
        '''
        Controls what guild's info to view
        '''
        chosen_guild = self.get_guild(guild_list)
        
        #get id of chosen guild
        guild_id = api_handler.get_response(api_handler.get_guild_id(chosen_guild))
        print(chosen_guild, guild_id) 
        
        #print guild information
        
        
        
        
    
        
        
        
        
        
        
        
        
        
    
    
    
        
    
    