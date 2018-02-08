'''
main_module.py
BB413F8F-F461-9047-AEAC-64285FF120FE7DAD1E31-A4AE-49DD-8DBD-3384085F855C

'''
from urllib import request
import json
import api_handler
import output_handler 

#Dictionary of possible outputs, sent to the output_handler module 
DICTIONARY = {
    'ACCOUNT': output_handler.Account(),
    'GUILD': output_handler.Guild(),
    
    }


def handle_outputs(result: dict, element: str) -> None:
    '''
    Prints all outputs given by results/search criteria 
    '''
    DICTIONARY[element].print_info(result)
    
    
def print_menu() -> str:
    '''
    Prints out the menu for the user 
    '''
    print('\nGW2 Navigation Menu: ')
    print('  1. Account\n  2. Guild\n  3. End Program')
    
MENU_DICT = {
    1: 'ACCOUNT', 
    2: 'GUILD',
    3: 'END'
    }
    
def menu() -> str:
    '''
    Menu made of dictionaries that the user can choose from to view something specific on 
    their account
    '''
    try:
        api_key = get_api_key()
        print_menu() 
        
        browse = True
        while browse == True:
            try:
                user_response = int(input('\nChoose an item in the menu: '))
                print() 
                result = api_handler.get_response(api_handler.build_search_url(api_key))
                if user_response == 3:
                    print('Exiting the program... Goodbye!')
                    quit() 
                else:
                    handle_outputs(result, MENU_DICT[user_response]) 
                
                
            except KeyError:
                print('Please enter a valid number listed in the menu above.')
    except ValueError:
        print('Please enter a valid API key.')
    

def get_api_key() -> str: 
    '''
    Gets API key from user 
    '''
    user_api_key = input('Enter your API key: ').strip() 
    return user_api_key

def welcome_message() -> str:
    '''
    Prints out a welcome message to the user
    '''
    print("Welcome to Emerz's GW2 API Handler (alpha)!\n") 

if __name__ == '__main__':
    welcome_message() 
    menu()
    
    
    
    
    
    
    
    