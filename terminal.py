import os 
from termcolor import cprint
import pyfiglet
import time

def ascii_art(title):
     ascii_art = pyfiglet.figlet_format(title)
     print(ascii_art)

def clear_the_screen():
     os.system('cls' if os.name == 'nt' else 'clear')

def main():
     
     title = "Moritz344"
     ascii_art(title)
     

     cprint("Welcome to my terminal.","blue")
     print()
     cprint("Type 'help' to view a list of available commands.","green")
     print()
     while True:
          x = input("> ")

          if x == "help":
               print()
               print("Hello I never thought some would use this but here we are thanks for using my terminal.")
               print()
               print("Journey")
               print("- My Coding Journey")
               print()
               print("whoami")
               print("- Who am I?")
               print()
               print("help")
               print("- help me please")
               print()
               print("clear")
               print("- clear this terminal")
               print()
               print("projects")
               print("- Yeah I built some stuff")
               print()
               print("exit")
               print("- get me out of this trash")
               print()
               print()
               print("html")
               print("- HTML")
               print()

          elif x == "clear":
               
               os.system("cls" if os.name == "nt" else "clear")
               main()
          elif x == "dic":
               Dic = {}
               Dic["a"] = 1
               Dic["b"] = 2
               Dic["c"] = 3
               cprint("you probably mean:","grey")
               print("Dictionary:")
               print(Dic)
          elif x == "Journey":
               print("At the age of 14, I embarked on my coding journey. Following a brief hiatus post-introductory Python learning, I returned to coding, immersing myself in daily learning sessions, largely comprising tutorial consumption. This phase led me into the depths of tutorial hell, from which I eventually emerged, finding newfound enjoyment in independent project development. In addition, I delved into the realm of Linux, hacking, and Bash programming, spurred by my exploration of a dedicated book. Subsequently rekindling my interest in Python, I embarked on the creation of various small-scale projects, including a terminal, to-do list, Flappy Bird clone, and Guess the Number game.")
               print()
          elif x == "whoami":
               print("I am a 16-year-old guy who enjoys coding and video editing. I manage two YouTube channels: one primarily focused on coding-related content, and the other where I share random content. With Currently around 400 subscribers. Additionally, I possess fundamental knowledge of Python and Bash.")
               print()
          elif x == "exit":
               print("Goodbye! ")
               break
          elif x == "projects":
               print("I post my projects on my github.https://github.com/Moritz344?tab=repositories")
               print()
          elif x == "html":
               print("Currently learning html and then css and then Javascript.")
               print()
          elif x != Command_error:
               cprint("command not found...","red")


Command_error = ["Journey","projects","exit","clear","whoami","dic","help"]
if __name__ == "__main__":
     clear_the_screen()
     main()