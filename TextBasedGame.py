# Mitchell Fontaine
# DEC/2022
# IT-140

# Function showing the goal of the game and move commands
def show_instructions():
   #print a main menu and the commands
   print("Witch Text Adventure Game")
   print("Collect 6 items to win the game, or you and your family will be killed by the Witch.")
   print("Be careful not to enter the Dining Room before gathering all the items")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")

# A dictionary for the Witch text game
# The dictionary links a room to other rooms.
# And contains an item in each room except the Living Room
rooms = {
        'Living Room': {'South': 'Garden', 'East': 'Study', 'West': 'Basement', 'North': 'Kitchen'},
        'Study': {'West': 'Living Room', 'item': 'Bourbon'},
        'Garden': {'West': 'Cellar', 'North': 'Living Room', 'item': 'Peaches'},
        'Cellar': {'East': 'Garden', 'item': 'Poison'},
        'Basement': {'East': 'Living Room', 'North': 'Spice Room', 'item': 'Flour'},
        'Spice Room': {'South': 'Basement', 'item': 'Sugar'},
        'Kitchen': {'South': 'Living Room', 'East': 'Dining Room', 'item': 'Oven'},
        'Dining Room': {'West': 'Kitchen', 'item': 'Witch'}
}

# Dictionary of items in game
items = ['Bourbon', 'Peaches', 'Oven', 'Poison', 'Sugar', 'Flour']

# Player Location Function
def player_loc():
    print('---------------------------')
    print('You are in the {}'.format(current_room))
    print('----------------------------')
    print('Inventory:', inventory)
    if current_room != 'Living Room' and rooms[current_room]['item'] not in inventory:
        print('You see the', rooms[current_room]['item'] + '.')
    print('---------------------------')

# inventory which is empty initially
inventory = []

# Directions
directions = ['North', 'South', 'East', 'West']

# Start Player in Great Hall
current_room = 'Living Room'
player_move = ''

# show player game instructions
show_instructions()

# This is the Main Game Loop
while True:
    player_loc()
    player_move = input('Enter your move: ').split()
    if player_move[0] == 'go':
        if len(player_move) != 2:
            print('Invalid command!')
        elif player_move[1] in rooms[current_room]:
            current_room = rooms[current_room][player_move[1]]
            if current_room == 'Dining Room':
                print("You haven't collected all the items and baked the poisonous pie!")
                print("The Witch has caught you and cooked you and your family into pies!")
                break
        elif player_move[1] not in directions:
            print('Invalid command!')
        elif player_move[1] not in rooms[current_room]:
            print("Can't go that way!")
        else:
            print('Invalid command!')
    elif player_move[0] == 'get':
        if len(player_move) == 1:
            print('Invalid command!')
        elif player_move[1] in rooms[current_room]['item'] and rooms[current_room]['item'] not in inventory:
            inventory.append(rooms[current_room]['item'])
            print(rooms[current_room]['item'], 'received!')
            if len(inventory) == 6:
                print('You got all the ingredients and baked a delicious and poisonous Peach Bourbon Pie and fed it to the aweful Witch!')
                print('The Witch falls over in agony and dies after tasting the best pie ever made.')
                print('You saved your family and won the game!!!')
                break
        elif player_move[1] not in rooms[current_room]['item']:
            if player_move[1] in items:
                print("Can't get", player_move[1] + '!')
            else:
                print('Invalid command!')
        else:
            print('Invalid command!')
    else:
        print('Invalid command!')