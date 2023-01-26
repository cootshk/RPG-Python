from pcolors import colors as c, backgrounds as b
#example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
import random as r
from monsterfight import battle
import time as t
print("Wanna play my game?")
game_choice = input("Please say yes... ")
if game_choice.casefold() == "yes":
  while True:
    print("Scene: You enter the cave. There is a fork in the tunnel that splits off into 2 directions: right and left. Where do you go?")
    player_choice1 = input("Right or Left: ")
    if player_choice1.casefold() == "right":
      #dragon cave
      print("You walk into a damp cave and hear water dripping somewhere off in the distance. The dark starts to loom. Do you continue?")
      dragoncave_choice1 = input("Continue? ")
      if dragoncave_choice1.casefold() == "yes":
        print("A small light apears in the distance. You head to towards it and your eyes start to ajust to the new light. You look around and skeletons of the people that came before, lay on the ground. You see the light comes from a torch on the wall. Do you want to pick it up?")
        torch_choice = input("Will you take it? ")
        if torch_choice.casefold() == "yes":
          print("You pick up the torch. The fire grows bright and illuminates the whole room. You get a better view of the skeletons and see some carried sword with golden handles and others carried chests with gems and gold. You jump to gather the riches but stop when you realize it will only weigh you down. You wonder, 'When does this cave end?' Do you dare continue?")
          dragoncave_choice2 = input("Do you dare: ")
          if dragoncave_choice2.casefold() == "yes":
            print("You walk forward slowly. After a short walk, you hear a snarling sound and a massive cave opens in front of you.")
            print("A dragon is laying on the ground in front of you, sleeping.")
            dragonfight_choice1 = input("Do you wish to fight it? ")
            if dragonfight_choice1.casefold() == "yes":
              print(f"{c.g}{b.b}[Dragon fight here]{c.d}{b.d}")
              t.sleep(2)
              print("Uhh...Well...")
              t.sleep(2)
              print("I... kinda.. haven't coded it yet...")
              t.sleep(3)
              print("I should probably add it right?")
              t.sleep(4)
              print("Would you like me to add it?")
              dragonfight_choice2 = input()
              if dragonfight_choice2.casefold() == "yes":
                print("Okay, I'll work on it. Give me a sec...")
                t.sleep(r.randint(2,4))
                print(".")
                t.sleep(r.randint(2,4))
                print("..")
                t.sleep(r.randint(2,4))
                print("...")
                t.sleep(3)
                print("Okay, it's done. Let's run it.")
                t.sleep(4)
                print("You run at the dragon and it wakes up with a jolt. It bares its teeth and moves towards you.")
                battle.monster_battle(200,20)
              if dragonfight_choice2.casefold() == "no":
                print("Fine then. Bye")
                break
              print("Wow, that was an intense fight. Phew, you are lucky you are alive. I hope you have fun!")
              break
            if dragonfight_choice1.casefold() == "no":
              print("Well it is your loss. I had coded a crazy boss fight that took forever to code, but you didn't want to do it. You know what? I'm going to remove it from the game for everybody because you said no. Bam! I just deleted it all. Nobody will ever get to play it because you were either too scared or you just were messing with me. Well, I hope you had fun.")
              break
          if dragoncave_choice2.casefold() == "no":
            print("You turn around to leave the cave but the ground rumbles and a wall of stone sildes down from the roof, trapping you in the cave. You turn the other way and another wall slides down. You are trapped.")
            secret2 = input()
            if secret2.casefold() == "continue":
              print("You found a secret! I have no idea how though...")
              print("A passage opens in the wall to your left, right next to a large skeleton.")
              secret2_choice = input("Do you want to continue?")
              if secret2_choice.casefold() == "yes":
                print("You walk in through the passage. You take a tentative step forward and nothing happens, so you keep on walking. The opening shuts behind you, but your helpful torch allows you to see. You walk into a small room with a large golden chest in the middle.")
                secret2_choice2 = input("Do you open the chest? ")
                if secret2_choice2.casefold() == "yes":
                  print("You got an acheivement! Since I can't give you and ingame one, past this, I will give you a high-five in person if you got this.")
                if secret2_choice2.casefold() == "no":
                  print("What the fuck! You were so close and you just decided to fucking say NO! What the FUCK! AHHHHHHH! You deserve to die! I'm going to code your death right here ready?")
                  print("Traps in the walls appears and closed in on you. This is the end of the player.")
            break
        if torch_choice.casefold() == "no":
          print("You continue walking. The light from the torch fades as you walk farther away. Suddenly, you lose all sight, and the darkness consumes you.")
          break
      if dragoncave_choice1.casefold() == "no":
        print("You leave the cave.")
        break
    if player_choice1.casefold() == "left":
      #death pit
      print("You walk down a dark cave. Suddenly, you lose all vision and you continue walking blindly. You hear the sound of water splashing in the distance. You think, 'There may be something down this path,'")
      deathpit_choice1 = input("Have you seen enough?  ")
      if deathpit_choice1.casefold() == "no":
        print("You walk and here a sound to your right. You look over and see some horrendous creature crawl out of the ground. It growls and picks it self up so that it stands in a hunched over stance. Suddenly it runs at you like it wants to kill you. What do you do?")
        battle.monster_battle(80,10)
#hopefully outside of code
if game_choice.casefold() == "no":
  print("Well... I dont know what to do with you.")
  secret = input("")
  if secret.casefold() == "secret":
    print("You got an achievement! Since I can't give you and ingame one, past this, I will give you a high-five in person if you got this.")
print("THE END")