
from DAO import DAO 
from User import User
class dispatcher:
    INDENT = '---------------------------------------------------\n'
    FIELDS=['id','first_name', 'second_name', 'phone']
    dao_object = DAO()
    while True:
        choice_number = input(f'{INDENT}\nPlease will choice number:\n 1.Save User.\n 2.Search user.\n 3.Exit from program.\nInput: ')
        match choice_number:
           #save User
           case '1':
             first_name = input(f"{INDENT}\nPlease input {FIELDS[1]}: ")
             second_name = input(f"Please input {FIELDS[2]}: ")
             phone = input(f"Please input {FIELDS[3]} number: ")
             user = User(first_name,second_name,phone)#create USER
             dao_object.save_user(user)
             print(f"{INDENT}User {first_name} {second_name} was saved.\n{INDENT}")
           #search user  
           case '2': 
              choise_number = int(input(f"{INDENT}1.Searching by {FIELDS[1]}.\n2.Searching by {FIELDS[2]}.\n3.Searching by {FIELDS[3]} number.\n{INDENT}Input: "))
              name = input(f'{INDENT}Please input serching word for searching: ')
              dao_object.search_user(name,choise_number)
              input_number = input(f'{INDENT}Please will choice number:\n 1.Change User.\n 2.Delete user.\n 3.Back on menu.\nInput: ')
              #submenu
              match input_number:
                 #Change user
                 case '1':
                    id = int(input(f'{INDENT}Please input user\'s id who you want to change: '))
                    choice_number = int(input(f"1.Change {FIELDS[1]}.\n2.Change {FIELDS[2]}.\n3.Change {FIELDS[3]} number.\n{INDENT}Input: "))
                    data_for_replace = input(f"{INDENT}Please input new {choice_number} for the user: ")
                    dao_object.change_user(id, choice_number, data_for_replace)
                 #dalete user   
                 case '2': 
                    id = int(input(f'{INDENT}Please input user\'s id who you want to delete: '))
                    dao_object.mark_indexes(dao_object.delete_user(id))
                    print(f"{INDENT}User with id = {id} was deleted.")
                 #back in main menu   
                 case '3': continue
           #exit      
           case '3':
              break  


        

        
