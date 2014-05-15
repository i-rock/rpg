import random

cap = 256 #damage multiplier cap {{2^x}}
# stamina cap = cap/2
# magicpower cap = none
# mblock = 0-100% block rate

damage = 0
spellpower = 1
level = 0
magicpower = 2
vigor = 0
vigor2 = 0
attack = 0
battlepower = 0
level = 1
damagemult = 0
crit = random.randint(1,cap/8)

friendly = True
magic = True

# enemy stats
magicdefense = 1
attackdefense = 0
# enemy stamina = maxhp/(cap*2) + cap/16 if > 40 then 40

blockvalue = 0



if crit is 1:
	damagemult = damagemult + 2

if friendly is True:
	if magic is True: #player magic damage
		damage = spellpower * 4 + (level * magicpower * spellpower / (cap/8))
		damage = damage + ((damage / 2) * damagemult)
		damage = (damage * random.randint(cap-cap/8-1,cap-1) / cap) + 1
		damage = (damage * (cap - 1 - magicdefense) / cap) + 1
	else: #player physical damage
		if vigor >= cap/2:
			vigor2 = cap - 1
		else:
			vigor2 = vigor * 2
			attack = battlepower + vigor2
		damage = battlpower + ((level * level * attack) / cap) * 3/2
		damage = damage + ((damage / 2) * damagemult)
		damage = (damage * random.randint(cap-cap/8-1,cap-1) / cap) + 1
		damage = (damage * (cap - 1 - attackdefense) / cap) + 1
		
else: #monster
	if magic is True:
		damage = spellpower * 4 + (level * (magicpower * 3/2) * spellpower/ (cap/8))
	else:
		#random number is vigor
		damage = level * level * (battlepower * 4 + random.randint(56,63)) / cap

print damage