position_int = int(input("Input a position between 1 and 10: "))

def Move_Right(postition):
    return postition+1

def Move_Left(position):
    return position-1
    
new_position = position_int

while True:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

    character = input("Input your choice: ")
    if character not in 'rl':
        print("New position is: ",new_position)
        break
    elif character in 'r':
        new_position = Move_Right(new_position)
    elif character in 'l':
        new_position = Move_Left(new_position)

    print("New position is: ",new_position)