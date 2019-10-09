print("""
start:->to start the car
stop:->to stop the car
quit:->to quit the program
""")
started = False
stopped = False
command=input("Enter command : ")
while(command != 'quit'):
    if(command == 'start'):
        if(started == False):
            print(f'car is started : ')
            started=True
            stopped=False
        else:
            print(f'car is already started')
    elif(command == 'stop' ):
        if(stopped == False):
            print(f'car is stopped')
            started = False
            stopped = True
        else:
            print(f'car is already stoped')
    else:
        print("in valid command : ")
    command=input()