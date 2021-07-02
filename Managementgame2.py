#import soemthing
import asyncio
import time
import random
import sys
import numpy as np
import string

class Managementgame():

    def __init__(self):
        self.money = 5100000
        self.stockprice = 5000000
        self.assets = []
        self.tmpassets = []
        self.stockvalue = 0
        self.investment = 0
        self.factorypl = 0
        self.androidpl = 0
        self.month = 1
        print("you have {} Yen".format(self.money))
        self.loading("lenting a miniplantfarm")
        self.money = self.money-900000
        self.loading("your have {} Yen now.".format(self.money))
        self.assets.append("minipfarmlent")
        time.sleep(1)
        self.loading("buying 1000 plants")
        self.assets.append("plant")
        self.money = self.money- 100000
        self.checkmoney(self.money)
        self.plantcounter = 1
        self.stockcounter = 0
        self.plantlimit = 3
        self.stockpl = 0
        self.monthchecking = {"minipfarmlent":-50000,}
    def checkmoney(self,money):
        M = money/1000000
        left = M%1000000
        print("You have {} M and {} Yen now.".format(M,left))
        #print("You have {} Yen now.".format(money))
    def loading(self,message):
        punkt = "."
        for a in range(3):
            print("{}{}".format(message,punkt))
            punkt = punkt + punkt
            time.sleep(0.5)
    def namegen(self):
        alphabet_string = string.ascii_lowercase
        alphabet_list = list(alphabet_string)
        c = ""
        for _ in range(3):
            b = alphabet_list[random.randint(0,len(alphabet_list)-1)]
            c = c+b
        return c
    def main(self):

        print("you have {} Yen".format(self.money))
        self.loading("lenting a miniplantfarm")
        self.money = self.money-900000
        self.loading("your have {} Yen now.".format(self.money))
        self.assets.append("minipfarmlent")
        time.sleep(1)
        self.loading("buying 1000 plants")
        self.assets.append("plant")
        self.money = self.money- 100000
        self.checkmoney(self.money)
        self.plantcounter = 1
        self.stockcounter = 0
        self.plantlimit = 3
        self.stockpl = 0
        self.monthchecking = {"minipfarmlent":-50000,}
        while True:
            print("Month {}".format(self.month))
            print("You have {} plants".format(self.plantcounter*1000))
            print("Stock profit in total... {}".format(self.stockpl))
            print("Factory profit in total...{}".format(self.factorypl))
            print("You have {} Yens of stocks".format(int(self.investment)))
            self.checkmoney(self.money)
            if self.money >= 100000000000:
                print("Game clear")
                x = input("do you have something to say as a capitalist?")
                sys.exit()
            if self.money >= 100000:
                try:
                    op = input("what would you do... 1 = expand plants -100000 Yen , 2, huge investment - 10000000 Yen, 3 = buy stocks -{} Yen, 4= buy a house to hold plants -1000000, 5 = employ an android -3000000".format(stockprice))
                    op = int(op)
                except:
                    op = 0
                if op == 1:
                    if self.plantcounter >= self.plantlimit:
                        self.loading("Too many Plants")
                        pass
                    else:
                        self.loading("buying 1000 plants")
                        self.money = self.money - 100000
                        self.checkmoney(self.money)
                        self.plantcounter += 1
                elif op == 2:
                    self.loading("buying a new factory")
                    self.assets.append("factory")
                    self.money = self.money -10000000
                    self.plantcounter += 15
                    self.plantlimit += 20
                    self.factorypl -= 10000000
                elif op == 3:
                    self.loading("buying stocks for {} Yen".format(self.stockprice))
                    self.assets.append("stocks")
                    self.money = self.money - self.stockprice
                    self.stockcounter += 1
                    self.stockvalue = int(self.stockvalue + self.stockprice)
                    self.investment = self.investment + self.stockprice
                elif op == 4:
                    loading("buying a house")
                    self.assets.append("house")
                    self.money = self.money - 1000000
                    self.plantcounter += 5
                    self.plantlimit += 2
                elif op == 5:
                    self.loading("employing an android")
                    name = self.namegen()
                    self.loading("Her Name is {}".format(name))
                    self.money = self.money -3000000
                    self.androidpl -= 3000000
                    self.monthchecking["{}".format(name)] = random.randint(-400000,500000)
                    self.assets.append("{}".format(name))
                else:
                    pass
            if self.money < 0:
                print("you are broke")
                we = input("do you have something to say before the end?")
                sys.exit()
            else:
                pass

            self.month += 1
            time.sleep(1)

            self.loading("monthly check")
            recession = random.randint(1,1000)
            for check in self.assets:

                if check == "factory":
                    income = random.randint(-4000000,5000000)
                    self.factorypl += income
                elif check =="stocks":
                    luck = random.randint(-5,6)
                    rate = luck/100
                    if luck >= 0:
                        income = ((self.stockvalue/self.stockcounter)*(np.abs(rate)))
                        stockfluc = self.stockvalue*np.abs(rate)
                    else:
                        income = -((self.stockvalue/self.stockcounter)*(np.abs(rate)))
                        stockfluc = -(self.stockvalue*np.abs(rate))
                    income = int(income)
                    if recession == 1:
                        self.loading("Oh no! recession occurred your assets are in danger!!!")
                        income = -(self.stockvalue/self.stockcounter)
                    self.stockvalue = int(self.stockvalue + self.stockfluc)
                    firstthirds = int(self.money * 0.3)
                    if firstthirds > 5000000:
                        self.stockprice = firstthirds
                    else:
                        self.stockprice = 5000000
                    self.stockpl = self.stockpl + income

                elif check == "house":
                    income = -20000
                    pass
                elif check == "plant":
                    income = 52000*self.plantcounter
                    unluck = random.randint(0,1)
                    if unluck == 1:
                        reduction = self.plantcounter * 0.1
                        self.plantcounter -= 1 + int(reduction)
                        self.loading("{} of plants died".format((1+int(reduction))*1000))
                else:
                    income = int(self.monthchecking["{}".format(check)])
                self.money = self.money + income
                if income >= 0:
                    print("a {} gives you {} monthly, your money became {} Yen".format(check, income, self.money))
                else:
                    print("{} costs you {} monthly, your money became {} Yen".format(check, income, self.money))

            """    if month%3 == 0:
                    if check == "minipfarmlent":
                        tmpassets.append(check)
                    else:
                        pass
                else:
                    tmpassets.append(check)
            assets = tmpassets"""
M = Managementgame()
M.main()
