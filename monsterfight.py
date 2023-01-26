class battle:
  def monster_battle(monsterhealth,monster_attackdamage):
    from pcolors import colors as c, backgrounds as b
    #example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
    import random as r
    monsterhealth2 = monsterhealth
    while monsterhealth > 0:
    #monster fight
      print(f"{c.y}{b.b}BATTLE:{c.d}{b.d}")
      deathpit_choice2 = input("Attack, Capture, or Items: ")
      player_attackdamage = r.randint(10, 20)
      player_health = 100
      if deathpit_choice2.casefold() == "attack":
        print("You swimg at the monster and it loses some health")
        monsterhealth = monsterhealth - player_attackdamage
        print("Enemy Health: "+ str(monsterhealth))
        pass
      if deathpit_choice2.casefold() == "capture":
        if monsterhealth >= 40:
          print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once. Twice. But then the ball explodes and the monster pops out.")
          print("Enemy Health: "+ str(monsterhealth))
          pass
        if monsterhealth < 40:
          print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once. Twice. Three times! You caught a Cave Monster!")
          break
      if deathpit_choice2.casefold() == "items":
        if monsterhealth == monsterhealth2:
          print("You pull a crowbar out of your ass and beat the shit out of the monster")
          monsterhealth = monsterhealth-80
          print("Enemy Health: "+ str(monsterhealth))
          break
        if monsterhealth < monsterhealth2:
          print("You reach into the air but nothing happens. What did you expect to happen? Did you think you would pull a crowbar out your butt?")
      if deathpit_choice2.casefold() == "devmode":
        dev_input = input("Dev: ")
        if dev_input == "RESET":
          monsterhealth = monsterhealth2
          print(monsterhealth)
          pass
        if dev_input == "EXIT":
          break
        if dev_input == "DAMAGE+":
          player_attackdamage = r.randint(20,30)
          print(player_attackdamage)
        if dev_input == "DAMAGE-":
          player_attackdamage = r.randint(5,10)
        if dev_input == "HARD":
          #Not a feature yet
          monster_attackdamage = monster_attackdamage + 10
        if dev_input == "EASY":
          #Not a feature yet
          monster_attackdamage -= 5
        if dev_input == "STATS":
          print(" M.H.: ", str(monsterhealth), "\n", "M.A.D.:", str(monster_attackdamage), "\n", "P.A.D.:", str(player_attackdamage), "\n", "P.H.:", str(player_health))
    #outside of fight
    print("That was an awesome fight! Good job taking that monster down!")