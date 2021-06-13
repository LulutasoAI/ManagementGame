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
        loading("lenting a miniplantfarm")
        money = money-900000
        loading("your have {} Yen now.".format(self.money))
        self.assets.append("minipfarmlent")
        time.sleep(1)
        loading("buying 1000 plants")
        self.assets.append("plant")
        self.money = self.money- 100000
        checkmoney(self.money)
        self.plantcounter = 1
        self.stockcounter = 0
        self.plantlimit = 3
        self.stockpl = 0
        monthchecking = {"minipfarmlent":-50000,}
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
