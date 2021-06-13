#import soemthing
import asyncio
import time
import random
import sys
import numpy as np
import string
money = 5100000
stockprice = 5000000
assets = []
tmpassets = []
stockvalue = 0
investment = 0
factorypl = 0
androidpl = 0
month = 1
def checkmoney(money):
    M = money/1000000
    left = M%1000000
    print("You have {} M and {} Yen now.".format(M,left))
    #print("You have {} Yen now.".format(money))
def loading(message):
    punkt = "."
    for a in range(3):
        print("{}{}".format(message,punkt))
        punkt = punkt + punkt
        time.sleep(0.5)
def namegen():
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    c = ""
    for _ in range(3):
        b = alphabet_list[random.randint(0,len(alphabet_list)-1)]
        c = c+b
    return c

print("you have {} Yen".format(money))
loading("lenting a miniplantfarm")
money = money-900000
loading("your have {} Yen now.".format(money))
assets.append("minipfarmlent")
time.sleep(1)
loading("buying 1000 plants")
assets.append("plant")
money = money- 100000
checkmoney(money)
plantcounter = 1
stockcounter = 0
plantlimit = 3
stockpl = 0
monthchecking = {"minipfarmlent":-50000,}
while True:
    print("Month {}".format(month))
    print("You have {} plants".format(plantcounter*1000))
    print("Stock profit in total... {}".format(stockpl))
    print("Factory profit in total...{}".format(factorypl))
    print("You have {} Yens of stocks".format(int(investment)))
    checkmoney(money)
    if money >= 100000000000:
        print("Game clear")
        x = input("do you have something to say as a capitalist?")
        sys.exit()
    if money >= 100000:
        try:
            op = input("what would you do... 1 = expand plants -100000 Yen , 2, huge investment - 10000000 Yen, 3 = buy stocks -{} Yen, 4= buy a house to hold plants -1000000, 5 = employ an android -3000000".format(stockprice))
            op = int(op)
        except:
            op = 0
        if op == 1:
            if plantcounter >= plantlimit:
                loading("Too many Plants")
                pass
            else:
                loading("buying 1000 plants")
                money = money - 100000
                checkmoney(money)
                plantcounter += 1
        elif op == 2:
            loading("buying a new factory")
            assets.append("factory")
            money = money -10000000
            plantcounter += 15
            plantlimit += 20
            factorypl -= 10000000
        elif op == 3:
            loading("buying stocks for {} Yen".format(stockprice))
            assets.append("stocks")
            money = money - stockprice
            stockcounter += 1
            stockvalue = int(stockvalue + stockprice)
            investment = investment + stockprice
        elif op == 4:
            loading("buying a house")
            assets.append("house")
            money = money - 1000000
            plantcounter += 5
            plantlimit += 2
        elif op == 5:
            loading("employing an android")
            name = namegen()
            loading("Her Name is {}".format(name))
            money = money -3000000
            androidpl -= 3000000
            monthchecking["{}".format(name)] = random.randint(-400000,500000)
            assets.append("{}".format(name))
        else:
            pass
    if money < 0:
        print("you are broke")
        we = input("do you have something to say before the end?")
        sys.exit()
    else:
        pass

    month += 1
    time.sleep(1)

    loading("monthly check")
    recession = random.randint(1,1000)
    for check in assets:

        if check == "factory":
            income = random.randint(-4000000,5000000)
            factorypl += income
        elif check =="stocks":
            luck = random.randint(-5,6)
            rate = luck/100
            if luck >= 0:
                income = ((stockvalue/stockcounter)*(np.abs(rate)))
                stockfluc = stockvalue*np.abs(rate)
            else:
                income = -((stockvalue/stockcounter)*(np.abs(rate)))
                stockfluc = -(stockvalue*np.abs(rate))
            income = int(income)
            if recession == 1:
                loading("Oh no! recession occurred your assets are in danger!!!")
                income = -(stockvalue/stockcounter)
            stockvalue = int(stockvalue + stockfluc)
            firstthirds = int(money * 0.3)
            if firstthirds > 5000000:
                stockprice = firstthirds
            else:
                stockprice = 5000000
            stockpl = stockpl + income

        elif check == "house":
            income = -20000
            pass
        elif check == "plant":
            income = 52000*plantcounter
            unluck = random.randint(0,1)
            if unluck == 1:
                reduction = plantcounter * 0.1
                plantcounter -= 1 + int(reduction)
                loading("{} of plants died".format((1+int(reduction))*1000))
        else:
            income = int(monthchecking["{}".format(check)])
        money = money + income
        if income >= 0:
            print("a {} gives you {} monthly, your money became {} Yen".format(check, income, money))
        else:
            print("{} costs you {} monthly, your money became {} Yen".format(check, income, money))

    """    if month%3 == 0:
            if check == "minipfarmlent":
                tmpassets.append(check)
            else:
                pass
        else:
            tmpassets.append(check)
    assets = tmpassets"""
