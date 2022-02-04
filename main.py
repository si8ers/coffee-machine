class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def state(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print('${} of money'.format(self.money))
        print()

    def make_coffee(self, water, milk, beans, money):
        if self.water >= water and self.milk >= milk and self.beans >= beans and self.cups > 0:
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= 1
            self.money += money
            print('I have enough resources, making you a coffee!')
        else:
            print('Sorry, not enough water!')
        print()

    def get_action_buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        buy = input()
        if buy == '1':
            # espresso
            self.make_coffee(250, 0, 16, 4)
        elif buy == '2':
            # latte
            self.make_coffee(350, 75, 20, 7)
        elif buy == '3':
            # cappuccino
            self.make_coffee(200, 100, 12, 6)

    def get_action_fill(self):
        print('Write how many ml of water you want to add:')
        self.water += int(input())
        print('Write how many ml of milk you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans you want to add:')
        self.beans += int(input())
        print('Write how many disposable coffee cups you want to add:')
        self.cups += int(input())

    def get_action_take(self):
        print('I gave you ${}'.format(self.money))
        self.money = 0
        print()

    def get_action(self):
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        if action == 'buy':
            self.get_action_buy()
        elif action == 'fill':
            self.get_action_fill()
        elif action == 'take':
            self.get_action_take()
        elif action == 'remaining':
            self.state()
        else:
            return False
        return True

cm = CoffeeMachine()
go = True
while go:
    go = cm.get_action()
