from random import randint
from time import sleep


def clear_output():
    """
    Clears the output in the console
    :return: none
    """
    for i in range(50):
        print("\n")


def display_end(win, play_time:
    """
    Display the end of the game screen
    :param win: if the player won or not (bool)
    :param play_time: total amount of the time it took to play the game
    :return: none
    """
    if win:
        clear_output()
        print("Congradulations! You Won\n")
        print("It took you " + play_time + " to play the game")


def ask_question(question):
    """
    Ask the user a question
    :param question: question to ask the user (str)
    :return: response
    """
    clear_output()
    response = input(question)
    return response


class Bot:
    """
    Class for the battle bots.
    """

    def __init__(self, type):
        """
        Inits the bot class
        :param type: type of bot given by the user (int)
        :return: none
        """
        self.bot_type = type
        if type == 1:
            self.health = 100
            self.speed = 4
            self.attack_damage = 20
        elif type == 2:
            self.health = 150
            self.speed = 10
            self.attack_damage = 35
        elif type == 3:
            self.health = 75
            self.speed = 2
            self.attack_damage = 13

    def attack(self, other_bot):
        """
        Attacks the other bot
        :param other_bot: other bot currently in the fight
        :return: if the bot was dead
        """
        other_bot.health -= self.attack_damage
        clear_output()
        print("You attacked the enemy bot!\n")
        print("Other Bot's Health:", other_bot.health)
        print("\nThe bot will make its move in 4 seconds")
        sleep(4)
        if other_bot.health <= 0:
            return True
        else:
            return False

    def defend(self, other_bot):
        """
        Defends against an attack from the other bot
        :param other_bot: other bot currently in the fight
        :return: if we died
        """
        block_amount = randint(0, 35)
        self.health -= other_bot.attack_damage - block_amount
        clear_output()
        print("You defended against the attack from the other bot!\n")
        print("Your Bot's Health:", self.health)
        print("Other Bot's Inital Attack:", )
        if self.health <= 0:
            return True
        else:
            return False




