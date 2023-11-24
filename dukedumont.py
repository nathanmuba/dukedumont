import time


current_color = 0


def greenlight():
    timer = 5
    print("The current light color is green")
    while timer != 0:
        print(f"The current light color is green and the time left is {timer} ")
        time.sleep(1)
        timer -= 1
    current_color = 1
    
def yellowlight():
    timer = 3
    print("The current light color is yellow")
    while timer != 0:
        print(f"The current light color is yellow and the time left is {timer} ")
        time.sleep(1)
        timer -= 1
    current_color = 2
        
def redlight():
    timer = 4
    print("The current light color is red")
    while timer != 0:
        print(f"The current light color is red and the time left is {timer} ")
        time.sleep(1)
        timer -= 1
    current_color = 0
    


def stoplight(current_color):
    dukedumont = {0:greenlight(),
                  1:yellowlight(),
                  2:redlight()}
    if current_color in dukedumont:
       return dukedumont[current_color]
   
    
while True:
    stoplight(current_color)