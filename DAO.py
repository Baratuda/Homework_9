import csv 
import pandas as pd
from User import *
FIELDS=['id','first_name', 'second_name', 'phone']
FILE_NAME = 'database.csv'
INDENT = '---------------------------------------------------\n'
data = pd.read_csv(FILE_NAME, index_col=0)
class DAO:
   #This method seves the user 
   def save_user(self, user):
        with open(FILE_NAME,'a', encoding="utf-8") as file:
          csvwriter = csv.DictWriter(file, fieldnames = FIELDS)
          csvwriter.writerow({FIELDS[0]:data.shape[0],#creates a unique id by adding +1 to the id of the last user in the database
                              FIELDS[1]:user.get_first_name(), 
                              FIELDS[2]:user.get_second_name(), 
                              FIELDS[3]:user.get_phone_number})
   #This method removes the user     
   def delete_user(self,id):
     data = pd.read_csv(FILE_NAME, index_col=0)
     return data.drop(data.index[id]) 
   
   #This method searches the user  
   def search_user(self, search_world, choice_number):
     data = pd.read_csv(FILE_NAME, index_col=0)#read file
     data = data[data[FIELDS[choice_number]] == search_world]#search in file by search_world
     serching_results = data.loc[data.index, FIELDS[1:]].values#save results in array
     #Output our results
     j=0
     for i in serching_results:
       print(f"{INDENT}{FIELDS[1]}: {i[0]} {i[1]};\n{FIELDS[3]}: {i[2]}\n{FIELDS[0]}:{data.index[j]}\n{INDENT}")
       j+=1

   #This method changes the user
   def change_user(self,id, choice_number, data_for_replace):
     data.loc[data.index[id], FIELDS[choice_number]] = data_for_replace#change the user
     data.to_csv(FILE_NAME)#save this changing in our file.

   #helper method
   #This method is necessary to change user IDs in order after deleting one of the users.
   def mark_indexes(self,data):
     result = data.loc[:, FIELDS[1:]].values#save our users in array
     data = pd.DataFrame(result, columns = FIELDS[1:])#save users in DATA Frame (mark our ids)
     data.to_csv(FILE_NAME)#save result in file  

