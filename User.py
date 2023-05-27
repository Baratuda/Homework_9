class User:
   __first_name = ""
   __second_name = ""
   __phone_number = ""
   
   def __init__(self, first_name, second_name, phone_number):
      User.__first_name = first_name
      User.__second_name = second_name
      User.__phone_number = phone_number

   def get_first_name(self):
      return  User.__first_name

   def set_first_name(self, name):
      User.__first_name = name    

   def get_second_name(self):
      return  User.__second_name

   def set_second_name(self, name):
      User.__second_name = name   

   def get_phone_number(self):
      return  User.__phone_number

   def set_phone_number(self, number):
      User.__phone_number = number         
   

         