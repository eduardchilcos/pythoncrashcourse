'''usernames = ['Vlad', 'Mihai', 'Gabriel', 'Eduard', 'admin']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")'''

'''users = []
if users:
    print("There are users.")
else:
    print("We need to find some users!")'''

current_users = ['Vasile', 'Gheorghe', 'Ion', 'Mitrita', 'Iorgu']

new_users = ['David', 'Matei', 'Luca', 'Vasile', 'Gheorghe']

for user in current_users:
    if user in new_users:
        print(f"Sorry {user} already exists. You will need a new username.")
    else: 
        print(f"The username {user} is available.")