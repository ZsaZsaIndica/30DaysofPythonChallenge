# import necesary libraries
import json

# greet the user and ask if they want to create a contact
contact_creation_greeting = input("Howdy! Shall we create a contact? Type yes or no: ")

# user accepts and inputs name and phone number
if contact_creation_greeting == 'yes':
  the_name = input("Enter contact name: ")
  the_phone_number = input("Enter contact phone number: ")
  # creation of dictionary to hold key value pairs of contact info
  my_contacts = {"name": the_name, "phone number": the_phone_number}
  # checkpoint
  print(my_contacts)
  print(type(my_contacts))
# user declines to create a contact. print a farewell greeting
elif contact_creation_greeting == 'no':
  print('ok, maybe next time')

# trasnform the data recieved into json object is called Serialization
json_contacts = json.dumps(my_contacts)
# open and write to a file using the "with statement"
with open('contact_Viv.json', "w") as outfile:
  outfile.write(json_contacts)
