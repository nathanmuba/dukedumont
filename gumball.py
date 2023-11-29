import time

class GumballMachine:
    def __init__(self,numgumball):
        self.state = 'No Coin'
        self.numgumball = numgumball
        
        
    def check_coin(self):
        if self.state == 'No Coin':
            print(f"There is no coin. Number of gumballs is still {self.numgumball}")
            self.state = 'Has Coin'
        elif self.state == 'Has Coin':
            print("You got a coin! Please insert it into the Gumball Machine")
        elif self.state == 'Releasing':
            print("The Gumball is being released.")
        else:
            return False
            
    def turn_crank(self):
        if self.state =='No Coin':
            print("We cannot turn the crank for there is no coin.")
        elif self.state =='Has Coin':
            print("The coin has been inserted and you can turn the crank.")
            self.numgumball -= 1
            self.state = 'Releasing'
            time.sleep(1)
            print(f"We turned the crank. The number of gumballs in the machine is {self.numgumball}.")
            if self.numgumball == 0:
                print("There are no more gumballs can you please refill")
        elif self.state == 'Releasing':
            print("The gumball has been released")
            self.state = 'No Coin'
        else:
            return False
    def refill(self, count):
        self.numgumball += count
        print(f"The number of gumballs has been refilled by {count} to be {self.numgumball}")
    
    


# Example usage:
gumball_machine = GumballMachine(numgumball=5)
print(gumball_machine)

gumball_machine.check_coin()
gumball_machine.turn_crank()

gumball_machine.check_coin()
gumball_machine.turn_crank()

gumball_machine.refill(10)
print(gumball_machine)

gumball_machine.check_coin()
gumball_machine.turn_crank()

            