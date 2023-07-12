import random
import time

E_accuracy = 90
player_level = 1
bread_number = 5
defense = 7
strength = 6
E_wepon = 8
bread = 20
hP = 100
limit = hP
e_HP = 50
speed = 7

wepon = int(input("choose a weapon, 1 = baseball bat, 2 = slingshot, "))
if wepon == 1:
  wepon = 18
  accuracy = 100
elif wepon == 2:
  wepon = 21
  accuracy = 75
elif wepon == 3:
  wepon = 100
  accuracy = 90
print("you enconter a wild raccoon")
raccon_level = 1
raccon_experince = (raccon_level * 4) / 2
stats = [7, 6, 5]
while not e_HP <= 0:
  while not e_HP <= 0:
    print("")
    print("HP -", hP, "/ 100")
    options = int(input("1 = attack, 2 = heal, 3 = run"))

    if options == 1:
      crit = random.randrange(1, 11)
      attack_power = random.randrange(wepon + strength - 5, wepon + strength)
      if crit >= 9:
        attack_power = attack_power + 10
        crit_T_F = True
      else:
        crit_T_F = False
      accuracy_miss = random.randrange(1, 101)
      if accuracy >= accuracy_miss:
        attack_power = attack_power - stats[1]
        print("")
        print("you attacked the wild raccoon")
        sec = 1
        time.sleep(sec)
        if crit_T_F == True:
          print("Crit")
        print("the raccoon suffered", attack_power, "damage")
        sec = 1
        time.sleep(sec)
        e_HP = e_HP - attack_power
        if e_HP <= 0:
          print("")
          print("the raccoon faints")
          print("you win")
          sec = 1
          time.sleep(sec)
        
        break
      elif accuracy < accuracy_miss:
        print("")
        print("you attack the wild raccoon")
        sec = 1
        time.sleep(sec)
        print("you miss")
        sec = 1
        time.sleep(sec)
        break
    elif options == 2:
      print("")
      healing = int(input("1 = breadx%s, 2 = options" % (bread_number)))
      if healing == 1 and bread_number == 0:
        print("")
        print("out of healing item")
        sec = 1
        time.sleep(sec)
        break
      elif healing == 1:
        hP = hP + bread
        HP_recover = bread
        if hP > limit:
          h = hP - limit
          hP = hP - h
          HP_recover = bread - h
        bread_number -= 1
        print("")
        print("you eat the bread")
        sec = 1
        time.sleep(sec)
        print("you recover", HP_recover, "HP")
        sec = 1
        time.sleep(sec)
        break
      elif healing == 2:
        print("")
    elif options == 3:
      print("")
      print("you try to run")
      sec = 1
      time.sleep(sec)
      print("the raccoon won't let you")
      sec = 1
      time.sleep(sec)
      break
  if e_HP > 0:
    enemy_crit = random.randrange(1, 11)
    E_attack_power = random.randrange(E_wepon + stats[0] - 2,
                                      E_wepon + stats[0] + 4)
    if enemy_crit >= 10:
      E_attack_power = E_attack_power + 10
      E_crit_T_F = True
    else:
      E_crit_T_F = False
    E_accuracy_miss = random.randrange(1, 101)
    if E_accuracy >= E_accuracy_miss:
      E_attack_power = E_attack_power - defense
      print("")
      print("the raccoon scratches you")
      sec = 1
      time.sleep(sec)
      if E_crit_T_F == True:
        print("Crit")
      print("you suffered", E_attack_power, " damage")
      time.sleep(sec)
      hP = hP - E_attack_power
      if hP <= 0:
        print("")
        print("you ran out of HP")
        print("you lose")
        break
    elif E_accuracy < E_accuracy_miss:
      print("")
      print("the raccoon lunges for you")
      sec = 1
      time.sleep(sec)
      print("you dodge swiftly")
      sec = 1
      time.sleep(sec)
if hP > 0:
  print("")
  print("you gained", raccon_experince, "XP")
  sec = 1
  time.sleep(sec)
  print("")
  print("another raccoon emerges")
  raccon_level = 2
  Bite_attack = False
  stats = [8, 6, 7]
  e_HP = 100
  while not e_HP <= 0:
    while not e_HP <= 0:
      print("")
      print("HP -", hP, "/ 100")
      options = int(input("1 = attack, 2 = heal, 3 = run"))

      if options == 1:
        crit = random.randrange(1, 11)
        attack_power = random.randrange(wepon + strength - 5, wepon + strength)
        if crit >= 9:
          crit_T_F = True
          attack_power = attack_power + 10
        else:
          crit_T_F = False
        accuracy_miss = random.randrange(1, 101)
        if accuracy >= accuracy_miss:
          attack_power = attack_power - stats[1]
          print("")
          print("you attacked the wild raccoon")
          sec = 1
          time.sleep(sec)
          if crit_T_F == True:
            print("Crit")
          print("the raccoon suffered", attack_power, "damage")
          e_HP = e_HP - attack_power
          sec = 1
          time.sleep(sec)
          break
          if e_HP <= 0:
            print("")
            print("the raccoon faints")
            print("you win")
            sec = 1
            time.sleep(sec)
         
          break
        elif accuracy < accuracy_miss:
          print("")
          print("you attack the wild raccoon")
          sec = 1
          time.sleep(sec)
          print("you miss")
          sec = 1
          time.sleep(sec)
          break
      elif options == 2:
        print("")
        healing = int(input("1 = breadx%s, 2 = options" % (bread_number)))
        if healing == 1 and bread_number == 0:
          print("")
          print("out of healing item")
          sec = 1
          time.sleep(sec)
          break
        elif healing == 1:
          hP = hP + bread
          HP_recover = bread
          if hP > limit:
            h = hP - limit
            hP = hP - h
            HP_recover = bread - h
          bread_number -= 1
          print("")
          print("you eat the bread")
          sec = 1
          time.sleep(sec)
          print("you recover", HP_recover, "HP")
          sec = 1
          time.sleep(sec)
          break
        elif healing == 2:
          print("")
      elif options == 3:
        print("")
        print("you try to run")
        sec = 1
        time.sleep(sec)
        print("the raccoon won't let you")
        sec = 1
        time.sleep(sec)
        break
    if e_HP > 0:
      enemy_crit = random.randrange(1, 11)
      E_attack_power = random.randrange(E_wepon + stats[0] - 2,
                                      E_wepon + stats[0] + 2)
      E_accuracy_miss = random.randrange(1, 101)
      Bite_chance = random.randrange(1,101)
      if Bite_chance <= 40 and Bite_attack == False:
        Bite_attack = True
        print("")
        print("The raccoon prepares for an attack")
        time.sleep(sec)
      elif Bite_attack == True:
        E_attack_power = E_attack_power + 20
        E_accuarcy_miss = E_accuracy_miss - 30
        Bite_attack = False
      if enemy_crit >= 9 and Bite_attack == False:
        E_attack_power = E_attack_power + 10
        crit_T_F = True
      elif Bite_attack == False:
        crit_T_F = False
      if E_accuracy >= E_accuracy_miss and Bite_attack == False:
        E_attack_power = E_attack_power - defense
        print("")
        print("the raccoon scratches you")
        time.sleep(sec)
        if crit_T_F == True and Bite_attack == False:
          print("Crit")
        print("you suffered", E_attack_power, " damage")
        time.sleep(sec)
        hP = hP - E_attack_power
        if hP <= 0:
          print("")
          print("you ran out of HP")
          print("you lose")
          break
      elif E_accuracy < E_accuracy_miss and Bite_attack == False:
        print("")
        print("the raccoon lunges for you")
        time.sleep(sec)
        print("you dodge swiftly")
        sec = 1
        time.sleep(sec)
  if hP > 0:
    print("")
    print("you gained", raccon_experince, "XP")
    print("you leveled up to level 2")
    sec = 1.5
    time.sleep(sec)
    print("HP increased by 10")
    limit = 110
    hP = limit
    time.sleep(sec)
    print("strength increased by 5")
    strength = strength + 5
    time.sleep(sec)
    print("defense increased by 5")
    defense = defense + 5
    time.sleep(sec)
    print("speed increased by 4")
    speed = speed + 4
    time.sleep(sec)
    print("New skill unlocked, Magic")
    FP = 15
    magic = 10
    time.sleep(sec)
    print("Learned Fire bomb")
    Fire_Bomb = [40, 20]
    time.sleep(sec)
    print("A pair of raccoons emerage and try to attack you")
    raccon_level = 1
    stats_2 = [8, 6, 9]
    e_HP_A = 125
    e_HP_B = 125
    sec = 1
    burn_B = False
    burn_A = False
#third fight
    while not e_HP_A <= 0 or not e_HP_B <= 0:
      while not e_HP_A <= 0 or not e_HP_B <= 0:
        print("")
        print("HP -", hP, "/ 110     FP -", FP, "/ 15")
        options = int(input("1 = attack, 2 = heal, 3 = run"))
        if options == 1:
          print("")
          fighting = int(input("1 = weapon, 2 = magic, 3 = options"))
          if fighting == 1:
            print("")
            fight_choice = int(input("1 = raccoon A, 2 = raccoon B"))
            if fight_choice == 1 and e_HP_A <= 0:
              print("")
              print("raccoon A is already unconscious")
              break
            elif fight_choice == 2 and e_HP_B <= 0:
              print("")
              print("raccoon B is already unconscious")
              break
            crit = random.randrange(1, 11)
            attack_power = random.randrange(wepon + strength, wepon + strength + 5)
            if crit >= 9:
              crit_T_F = True
              attack_power = attack_power + 10
            accuracy_miss = random.randrange(1, 101)
            if accuracy >= accuracy_miss:
              attack_power = attack_power - stats_2[1]
              print("")
              print("you attacked the wild raccoons")
              time.sleep(sec)
              if fight_choice == 1:
                print("raccoon A suffered", attack_power, "damage")
                e_HP_A = e_HP_A - attack_power
                time.sleep(sec)
                if e_HP_A <= 0:
                  print("")
                  print("raccoon A faints")
                  time.sleep(sec)
                  break
                break
              elif fight_choice == 2:
                print("raccoon B suffered", attack_power, "damage")
                e_HP_B = e_HP_B - attack_power
                sec = 1
                time.sleep(sec)
                if e_HP_B <= 0:
                  print("")
                  print("raccoon B faints")
                  time.sleep(sec)
                break
            elif accuracy < accuracy_miss:
              if fight_choice == 1:
                print("")
                print("you attack raccoon A")
                time.sleep(sec)
                print("you miss")
                time.sleep(sec)
              elif fight_choice == 2:
                print("")
                print("you attack raccoon B")
                time.sleep(sec)
                print("you miss")
                time.sleep(sec)
              break
          elif fighting == 2:
            print("")
            M_choice = int(input("1 = Fire bomb(5 FP) "))
            if M_choice and FP < 5:
              print()
              print("Not enough FP")
              time.sleep(sec)
              break
            if M_choice == 1:
              print("")
              fight_choice = int(input("1 = raccoon A, 2 = raccoon B"))
              if fight_choice == 1 and e_HP_A <= 0:
                print("")
                print("raccoon A is already unconscious")
                time.sleep(sec)
                break
              elif fight_choice == 2 and e_HP_B <= 0:
                print("")
                print("raccoon B is already unconscious")
                time.sleep(sec)
                break
              if fight_choice == 1:
                magic_power = random.randrange(Fire_Bomb[0] + magic, Fire_Bomb[0] + magic + 20)
                burn_chance = random.randrange(1, 101)
                if burn_chance <= Fire_Bomb[1]:
                  burn_A = True
                else:
                  burn_A = False
                print("")
                print("you attack raccoon A")
                time.sleep(sec)
                print("raccoon A suffered",magic_power,"damage")
                FP = FP - 5
                time.sleep(sec)
                if burn_A == True:
                  print("")
                  print("raccoon A got burned")
                  time.sleep(sec)
                e_HP_A = e_HP_A - magic_power
                if e_HP_A <= 0:
                  print("")
                  print("raccoon A fainted")
                  time.sleep(sec)
                break
              elif fight_choice == 2:
                magic_power = random.randrange(Fire_Bomb[0] + magic, Fire_Bomb[0] + magic + 20)
                burn_chance = random.randrange(1, 101)
                if burn_chance <= Fire_Bomb[1]:
                  burn_B = True
                else:
                  burn_B = False
                print("")
                print("you attack raccoon B")
                time.sleep(sec)
                print("raccoon B suffered",magic_power,"damage")
                FP = FP - 5
                time.sleep(sec)
                if burn_B == True:
                  print("")
                  print("raccoon B got burned")
                  time.sleep(sec)
                e_HP_B = e_HP_B - magic_power
                if e_HP_B <= 0:
                  print("")
                  print("raccoon B fainted")
                  time.sleep(sec)
                break
          elif fighting == 3:
            print("")
        elif options == 2:
          print("")
          healing = int(input("1 = breadx%s, 2 = options" % (bread_number)))
          if healing == 1 and bread_number == 0:
            print("")
            print("out of healing item")
            sec = 1
            time.sleep(sec)
            break
          elif healing == 1:
            hP = hP + bread
            HP_recover = bread
            if hP > limit:
              h = hP - limit
              hP = hP - h
              HP_recover = bread - h
            bread_number -= 1
            print("")
            print("you eat the bread")
            sec = 1
            time.sleep(sec)
            print("you recover", HP_recover, "HP")
            sec = 1
            time.sleep(sec)
            break
          elif healing == 2:
            print("")
        elif options == 3:
          print("")
          print("you try to run")
          time.sleep(sec)
          print("the raccoons won't let you")
          time.sleep(sec)
          break
          print("")
      if e_HP_A > 0 or e_HP_B > 0:
        enemy_crit_A = random.randrange(1, 11)
        enemy_crit_B = random.randrange(1, 11)
        E_attack_power_A = random.randrange(stats_2[0] + E_wepon, stats_2[0] + E_wepon + 10)
        E_attack_power_B = random.randrange(stats_2[0] + E_wepon, stats_2[0] + E_wepon + 10)
        E_speed_A = random.randrange(stats_2[2], stats_2[2] + 7)
        E_speed_B = random.randrange(stats_2[2], stats_2[2] + 7)
        if enemy_crit_A >= 10:
          E_attack_power_A = E_attack_power_A + 10
          E_crit_T_F_A = True
        else:
          E_crit_T_F_A = False    
        if enemy_crit_B >= 10:
          E_attack_power_B = E_attack_power_B + 10
          E_crit_T_F_B = True
        else:
          E_crit_T_F_B = False
        if (E_speed_A >= E_speed_B and not e_HP_A <= 0) or (e_HP_B <= 0):
          E_accuracy_miss = random.randrange(1, 101)
          if E_accuracy >= E_accuracy_miss:
            E_attack_power_A = E_attack_power_A - defense
            print("")
            print("raccoon A scratches you")
            time.sleep(sec)
            if E_crit_T_F_A == True:
              print("Crit")
            print("you suffered", E_attack_power_A, " damage")
            time.sleep(sec)
            hP = hP - E_attack_power_A
            if hP <= 0:
              print("")
              print("you ran out of HP")
              print("you lose")
              break
          elif E_accuracy < E_accuracy_miss:
            print("")
            print("raccoon A lunges for you")
            time.sleep(sec)
            print("you dodge swiftly")
            time.sleep(sec)
#raccon B's turn from raccon A's turn
          if not e_HP_B <= 0:
            E_accuracy_miss = random.randrange(1, 101)
            if E_accuracy >= E_accuracy_miss:
              E_attack_power_B = E_attack_power_B - defense
              print("")
              print("raccoon B scratches you")
              time.sleep(sec)
              if E_crit_T_F_B == True:
                print("Crit")
              print("you suffered", E_attack_power_B, " damage")
              time.sleep(sec)
              hP = hP - E_attack_power_B
              if hP <= 0:
                print("")
                print("you ran out of HP")
                print("you lose")
                break
            elif E_accuracy < E_accuracy_miss:
              print("")
              print("raccoon B lunges for you")
              time.sleep(sec)
              print("you dodge swiftly")
              time.sleep(sec)
        elif (E_speed_B > E_speed_A and not e_HP_B <= 0) or (e_HP_A <= 0):
          E_accuracy_miss = random.randrange(1, 101)
          if E_accuracy >= E_accuracy_miss:
            E_attack_power_B = E_attack_power_B - defense
            print("")
            print("raccon B scratches you")
            time.sleep(sec)
            if E_crit_T_F_B == True:
              print("Crit")
            print("you suffered", E_attack_power_B, " damage")
            time.sleep(sec)
            hP = hP - E_attack_power_B
            if hP <= 0:
              print("")
              print("you ran out of HP")
              print("you lose")
              break
          elif E_accuracy < E_accuracy_miss:
            print("")
            print("raccon B lunges for you")
            time.sleep(sec)
            print("you dodge swiftly")
            time.sleep(sec)
#raccon A's turn from raccon B's turn
          if not e_HP_A <= 0:
            E_accuracy_miss = random.randrange(1, 101)
            if E_accuracy >= E_accuracy_miss:
              E_attack_power_A = E_attack_power_A - defense
              print("")
              print("raccoon A scratches you")
              time.sleep(sec)
              if E_crit_T_F_A == True:
                print("Crit")
              print("you suffered", E_attack_power_A, " damage")
              time.sleep(sec)
              hP = hP - E_attack_power_A
              if hP <= 0:
                print("")
                print("you ran out of HP")
                print("you lose")
                break
            elif E_accuracy < E_accuracy_miss:
              print("")
              print("raccoon A lunges for you")
              time.sleep(sec)
              print("you dodge swiftly")
              time.sleep(sec)
        if burn_A == True and not e_HP_A <= 0:
          time.sleep(sec)
          print("")
          print("raccoon A took damage from the burn")
          e_HP_A = e_HP_A - 5
          burn_A = False
          time.sleep(sec)
          if e_HP_A <= 0:
            print("")
            print("raccoon A fainted")
            time.sleep(sec)
        elif burn_B == True and not e_HP_B <= 0:
          print("")
          print("raccoon B took damage from the burn")
          e_HP_B = e_HP_B - 5
          burn_B = False
          time.sleep(sec)
          if e_HP_B <= 0:
            print("")
            print("raccoon B fainted")
            time.sleep(sec)
    if hP > 0:
      print("")
      print("you gained", raccon_experince, "XP")
      time.sleep(sec)
      print("")
      print("raccon A and raccon B droped 3 bread and 3 fast food")
      bread_number = bread_number + 3
      fast_food = 3
      fast_food_recovery = 10
      time.sleep(sec)
      print("")
      print("you leveled up to level 3")
      print("HP increased by a tremendous amount")
      limit = 130
      hP = limit
      sec = 1.5
      time.sleep(sec)
      print("strength increased by 5")
      strength = strength + 5
      time.sleep(sec)
      print("defense increased by 3")
      defense = defense + 5
      time.sleep(sec)
      print("speed increase by 3")
      speed = speed + 3
      time.sleep(sec)
      print("FP increased by 5")
      FP = 20
      magic = magic + 5
      time.sleep(sec)
      print("Learned 'defense up'")
      defense_up = [40, 20]
      sec = 1
      time.sleep(sec)
      print("A huge raccoon apears")
      time.sleep(sec)
      e_HP = 300
      e_HP_A = 50
      e_HP_B = 50
      stats_3 = [17, 9, 7]
      burn = False
      burn_A = False
      burn_B = False
      raccon_A = False
      raccon_B = False
      cutscene = False
      cutscene_1 = False
      defense_up_T_F = False
    while not e_HP <= 0:
      while not e_HP <= 0:
        print("")
        print("HP -", hP, "/ 130     FP -", FP, "/ 20")
        options = int(input("1 = attack, 2 = heal, 3 = run"))
        if options == 1:
          print("")
          fighting = int(input("1 = weapon, 2 = magic, 3 = options"))
          if fighting == 1:
            print("")
            if raccon_A == False and raccon_B == False:
              fight_choice = int(input("1 = raccon boss"))
            elif raccon_A == True or raccon_B == True:
              fight_choice = int(input("1 = raccon boss, 2 = raccoon A, 3 = raccon_B"))
              
            if fight_choice == 2 and e_HP_A <= 0 and raccon_A == True:
              print("")
              print("raccoon A is already unconscious")
              break
            elif fight_choice == 3 and e_HP_B <= 0 and raccon_A == True:
              print("")
              print("raccoon B is already unconscious")
              break
            crit = random.randrange(1, 11)
            attack_power = random.randrange(wepon + strength, wepon + strength + 10)
            if crit >= 9:
              crit_T_F = True
              attack_power = attack_power + 10
            else:
              crit_T_F = False
            accuracy_miss = random.randrange(1, 101)
            if accuracy >= accuracy_miss:
              if fight_choice == 1:
                attack_power = attack_power - stats_3[1]
                print("")
                print("you attack the huge raccoon")
                time.sleep(sec)
                print("the raccoon suffered", attack_power, "damage")
                e_HP = e_HP - attack_power
                time.sleep(sec)
                if e_HP <= 0:
                  print("")
                  print("the raccoon faints")
                  time.sleep(sec)
                  break
                break
              elif fight_choice == 2 and raccon_A == True:
                attack_power = attack_power - stats_2[1]
                print("")
                print("you attack raccoon A")
                time.sleep(sec)
                print("raccoon A suffered", attack_power, "damage")
                e_HP_A = e_HP_A - attack_power
                time.sleep(sec)
                if e_HP_A <= 0:
                  print("")
                  print("raccoon A faints")
                  raccon_A = False
                  time.sleep(sec)
                  break
                break
              elif fight_choice == 3 and raccon_B == True:
                attack_power = attack_power - stats_2[1]
                print("")
                print("you attack raccoon B")
                time.sleep(sec)
                print("raccoon B suffered", attack_power, "damage")
                e_HP_B = e_HP_B - attack_power
                time.sleep(sec)
                if e_HP_B <= 0:
                  print("")
                  print("raccoon B faints")
                  raccon_B = False
                  time.sleep(sec)
                  break
                break
            elif accuracy < accuracy_miss:
              if fight_choice == 1:
                print("")
                print("you attack the huge raccoon")
                time.sleep(sec)
                print("you miss")
                time.sleep(sec)
              elif fight_choice == 2 and raccon_A == True:
                print("")
                print("you attack raccoon A")
                time.sleep(sec)
                print("you miss")
                time.sleep(sec)
              elif fight_choice == 3 and raccon_B == True:
                print("")
                print("you attack raccoon B")
                time.sleep(sec)
                print("you miss")
                time.sleep(sec)
              break
          elif fighting == 2:
            print("")
            M_choice = int(input("1 = Fire bomb(5 FP), 2 = defense up(3 FP)"))
            if M_choice == 1 and FP < 5:
              print()
              print("Not enough FP")
              time.sleep(sec)
              break
            elif M_choice == 2 and FP < 3:
              print()
              print("Not enough FP")
              time.sleep(sec)
              break
            elif M_choice == 2 and FP >= 3:
              protective_fail = random.randrange(1, 101)
              if protective_fail > defense_up [1]:
                print("")
                print("you cast a protective sheild")
                time.sleep(sec)
                FP = FP - 3
                defense = defense + defense_up[0]
                defense_up_T_F = True
              elif protective_fail <= defense_up[1]:
                print("")
                print("you cast a protective sheild")
                time.sleep(sec)
                FP = FP -3
                print("but it didn't work")
                time.sleep(sec)
              break
            elif M_choice == 1 and FP >= 5:
              print("")
              if raccon_A == False and raccon_B == False:
                fight_choice = int(input("1 = huge raccoon"))
              elif raccon_A == True or raccon_B == True:
                fight_choice = int(input("1 = huge raccoon, 2 = raccon_A, 3 = raccon_B"))
              if fight_choice == 2 and e_HP_A <= 0 and raccon_A == True:
                print("")
                print("raccoon A is already unconscious")
                time.sleep(sec)
                break
              elif fight_choice == 3 and e_HP_B <= 0 and raccon_B == True:
                print("")
                print("raccoon B is already unconscious")
                time.sleep(sec)
                break
              if fight_choice == 1:
                magic_power = random.randrange(Fire_Bomb[0] + magic, Fire_Bomb[0] + magic + 20)
                burn_chance = random.randrange(1, 101)
                if burn_chance <= Fire_Bomb[1]:
                  burn = True
                else:
                  burn = False
                print("")
                print("you attack the huge raccoon")
                time.sleep(sec)
                print("the huge raccoon suffered",magic_power,"damage")
                FP = FP - 5
                time.sleep(sec)
                if burn == True:
                  print("")
                  print("the huge raccoon got burned")
                  time.sleep(sec)
                e_HP = e_HP - magic_power
                if e_HP <= 0:
                  print("")
                  print("the huge raccoon fainted")
                  time.sleep(sec)
                break
              elif fight_choice == 2 and raccon_A == True:
                magic_power = random.randrange(Fire_Bomb[0] + magic, Fire_Bomb[0] + magic + 20)
                burn_chance = random.randrange(1, 101)
                if burn_chance <= Fire_Bomb[1]:
                  burn_A = True
                else:
                  burn_A = False
                print("")
                print("you attack raccoon A")
                time.sleep(sec)
                print("raccoon A suffered",magic_power,"damage")
                FP = FP - 5
                time.sleep(sec)
                if burn_A == True:
                  print("")
                  print("raccoon A got burned")
                  time.sleep(sec)
                e_HP_A = e_HP_A - magic_power
                if e_HP_A <= 0:
                  print("")
                  print("raccoon A fainted")
                  raccon_A = False
                  time.sleep(sec)
                break
              elif fight_choice == 3 and raccon_B == True:
                magic_power = random.randrange(Fire_Bomb[0] + magic, Fire_Bomb[0] + magic + 20)
                burn_chance = random.randrange(1, 101)
                if burn_chance <= Fire_Bomb[1]:
                  burn_B = True
                else:
                  burn_B = False
                print("")
                print("you attack raccoon B")
                time.sleep(sec)
                print("raccoon B suffered",magic_power,"damage")
                FP = FP - 5
                time.sleep(sec)
                if burn_B == True:
                  print("")
                  print("raccoon B got burned")
                  time.sleep(sec)
                e_HP_B = e_HP_B - magic_power
                if e_HP_B <= 0:
                  print("")
                  print("raccoon B fainted")
                  raccon_B = False
                  time.sleep(sec)
                break
          elif fighting == 3:
            print("")
        elif options == 2:
          print("")
          healing = int(input("1 = breadx%s, 2 = fast foodX%s, 3 = options" % (bread_number, fast_food)))
          if healing == 1 and bread_number == 0:
            print("")
            print("out of healing item")
            sec = 1
            time.sleep(sec)
            break
          elif healing == 1:
            hP = hP + bread
            HP_recover = bread
            if hP > limit:
              h = hP - limit
              hP = hP - h
              HP_recover = bread - h
            bread_number -= 1
            print("")
            print("you eat the bread")
            sec = 1
            time.sleep(sec)
            print("you recover", HP_recover, "HP")
            sec = 1
            time.sleep(sec)
            break
          elif healing == 2 and fast_food == 0:
            print("")
            print("out of healing item")
            sec = 1
            time.sleep(sec)
            break
          elif healing == 2:
            hP = hP + fast_food_recovery
            HP_recover = fast_food_recovery
            if hP > limit:
              h = hP - limit
              hP = hP - h
              HP_recover = fast_food_recovery - h
            fast_food -= 1
            print("")
            print("you eat the fast food")
            sec = 1
            time.sleep(sec)
            print("you recover", HP_recover, "HP")
            sec = 1
            time.sleep(sec)
          elif healing == 3:
            print("")
        elif options == 3:
          print("")
          print("you try to run")
          time.sleep(sec)
          print("the raccoons won't let you")
          time.sleep(sec)
          break
          print("")
      if e_HP <= 150 and cutscene_1 == False:
        time.sleep(sec)
        print("")
        print("the raccon begins to hiss")
        time.sleep(sec)
        print("two more raccoons emerage")
        time.sleep(sec)
        raccon_A = True
        raccon_B = True
        cutscene = True
        cutscene_1 = True
        hP = limit
        fast_food = fast_food + 3
      if (e_HP_A > 0 or e_HP_B > 0) and cutscene == False:
        enemy_crit = random.randrange(1, 11)
        enemy_crit_A = random.randrange(1, 11)
        enemy_crit_B = random.randrange(1, 11)
        E_attack_power = random.randrange(stats_3[0] + E_wepon, stats_3[0] + E_wepon + 10)
        E_attack_power_A = random.randrange(stats_2[0] + E_wepon, stats_2[0] + E_wepon + 10)
        E_attack_power_B = random.randrange(stats_2[0] + E_wepon, stats_2[0] + E_wepon + 10)
        E_speed_A = random.randrange(stats_2[2], stats_2[2] + 7)
        E_speed_B = random.randrange(stats_2[2], stats_2[2] + 7)
        E_accuracy_miss = random.randrange(1, 101)
        Bite_chance = random.randrange(1,101)
        if Bite_chance <= 40 and Bite_attack == False:
          Bite_attack = True
          print("")
          print("The raccoon prepares for an attack")
          time.sleep(sec)
        elif Bite_attack == True:
          E_attack_power = E_attack_power + 20
          E_accuarcy_miss = E_accuracy_miss - 30
          Bite_attack = False
        if enemy_crit >= 9 and Bite_attack == False:
          E_attack_power = E_attack_power + 20
          crit_T_F = True
        elif Bite_attack == False:
          crit_T_F = False
        if E_accuracy >= E_accuracy_miss and Bite_attack == False:
          E_attack_power = E_attack_power - defense
          if E_attack_power < 0:
            E_attack_power = 1
          print("")
          print("the huge raccoon scratches you")
          time.sleep(sec)
          if crit_T_F == True and Bite_attack == False:
            print("Crit")
          print("you suffered", E_attack_power, " damage")
          time.sleep(sec)
          hP = hP - E_attack_power
          if hP <= 0:
            print("")
            print("you ran out of HP")
            print("you lose")
            break
        elif E_accuracy < E_accuracy_miss and Bite_attack == False:
          print("")
          print("the huge raccoon lunges for you")
          time.sleep(sec)
          print("you dodge swiftly")
          sec = 1
          time.sleep(sec)
        if enemy_crit_A >= 10:
          E_attack_power_A = E_attack_power_A + 10
          E_crit_T_F_A = True
        else:
          E_crit_T_F_A = False    
        if enemy_crit_B >= 10:
          E_attack_power_B = E_attack_power_B + 10
          E_crit_T_F_B = True
        else:
          E_crit_T_F_B = False
        if raccon_A == True or raccon_B == True:
          if (E_speed_A >= E_speed_B and not e_HP_A <= 0) or (e_HP_B <= 0):
            E_accuracy_miss = random.randrange(1, 101)
            if E_accuracy >= E_accuracy_miss:
              E_attack_power_A = E_attack_power_A - defense
              if E_attack_power_A < 0:
                E_attack_power_A = 1
              print("")
              print("raccoon A scratches you")
              time.sleep(sec)
              if E_crit_T_F_A == True:
                print("Crit")
              print("you suffered", E_attack_power_A, " damage")
              time.sleep(sec)
              hP = hP - E_attack_power_A
              if hP <= 0:
                print("")
                print("you ran out of HP")
                print("you lose")
                break
            elif E_accuracy < E_accuracy_miss:
              print("")
              print("raccoon A lunges for you")
              time.sleep(sec)
              print("you dodge swiftly")
              time.sleep(sec)
#raccon B's turn from raccon A's turn
            if not e_HP_B <= 0:
              E_accuracy_miss = random.randrange(1, 101)
              if E_accuracy >= E_accuracy_miss:
                E_attack_power_B = E_attack_power_B - defense
                if E_attack_power_B < 0:
                  E_attack_power_B = 1
                print("")
                print("raccoon B scratches you")
                time.sleep(sec)
                if E_crit_T_F_B == True:
                  print("Crit")
                print("you suffered", E_attack_power_B, " damage")
                time.sleep(sec)
                hP = hP - E_attack_power_B
                if hP <= 0:
                  print("")
                  print("you ran out of HP")
                  print("you lose")
                  break
              elif E_accuracy < E_accuracy_miss:
                print("")
                print("raccoon B lunges for you")
                time.sleep(sec)
                print("you dodge swiftly")
                time.sleep(sec)
          elif (E_speed_B > E_speed_A and not e_HP_B <= 0) or (e_HP_A <= 0):
            E_accuracy_miss = random.randrange(1, 101)
            if E_accuracy >= E_accuracy_miss:
              E_attack_power_B = E_attack_power_B - defense
              if E_attack_power_B < 0:
                E_attack_power_B = 1
              print("")
              print("raccon B scratches you")
              time.sleep(sec)
              if E_crit_T_F_B == True:
                print("Crit")
              print("you suffered", E_attack_power_B, " damage")
              time.sleep(sec)
              hP = hP - E_attack_power_B
              if hP <= 0:
                print("")
                print("you ran out of HP")
                print("you lose")
                break
            elif E_accuracy < E_accuracy_miss:
              print("")
              print("raccon B lunges for you")
              time.sleep(sec)
              print("you dodge swiftly")
              time.sleep(sec)
#raccon A's turn from raccon B's turn
            if not e_HP_A <= 0:
              E_accuracy_miss = random.randrange(1, 101)
              if E_accuracy >= E_accuracy_miss:
                E_attack_power_A = E_attack_power_A - defense
                if E_attack_power_A < 0:
                  E_attack_power_A = 1
                print("")
                print("raccoon A scratches you")
                time.sleep(sec)
                if E_crit_T_F_A == True:
                  print("Crit")
                print("you suffered", E_attack_power_A, " damage")
                time.sleep(sec)
                hP = hP - E_attack_power_A
                if hP <= 0:
                  print("")
                  print("you ran out of HP")
                  print("you lose")
                  break
              elif E_accuracy < E_accuracy_miss:
                print("")
                print("raccoon A lunges for you")
                time.sleep(sec)
                print("you dodge swiftly")
                time.sleep(sec)
        if burn == True and not e_HP <= 0:
          time.sleep(sec)
          print("")
          print("the huge raccoon took damage from the burn")
          e_HP = e_HP - 5
          burn = False
          time.sleep(sec)
          if e_HP <= 0:
            print("")
            print("the huge raccoon fainted")
            time.sleep(sec)
        elif burn_A == True and not e_HP_A <= 0:
          time.sleep(sec)
          print("")
          print("raccoon A took damage from the burn")
          e_HP_A = e_HP_A - 5
          burn_A = False
          time.sleep(sec)
          if e_HP_A <= 0:
            print("")
            print("raccoon A fainted")
            raccon_A = False
            time.sleep(sec)
        elif burn_B == True and not e_HP_B <= 0:
          print("")
          print("raccoon B took damage from the burn")
          e_HP_B = e_HP_B - 5
          burn_B = False
          time.sleep(sec)
          if e_HP_B <= 0:
            print("")
            print("raccoon B fainted")
            time.sleep(sec)
            raccon_B = False
      cutscene = False
      if defense_up_T_F == True:
        defense = defense - defense_up[0]
        defense_up_T_F = False