import newfight as f

player = f.player("Jake", hp=100, spd=5, df=5, atk=5)
print(player.equipped)
bow = f.weapon.ranged(name="bow")