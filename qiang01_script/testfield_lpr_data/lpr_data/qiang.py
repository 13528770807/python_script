#!/usr/bin/python3
import shutil
import sys


class Place:
    def __init__(self, num):
        self.num = num
        self.place1 = './license_plate/ZABC255/lp_database.txt'
        self.place2 = './license_plate/ZB53Y11/lp_database.txt'
        self.place3 = './license_plate/ZC796YR/lp_database.txt'
        self.place4 = './license_plate/ZD8789H/lp_database.txt'
        self.place5 = './license_plate/HC05EV8/lp_database.txt'
        self.placeAll = './license_plate/All/lp_database.txt'
        self.destination = '../lpr_config/'

    def change(self):
        if self.num == '1':
            print('禁止通行车辆:浙ABC255')
            shutil.copy(self.place1, self.destination)
        elif self.num == '2':
            print('禁止通行车辆:浙B53Y11')
            shutil.copy(self.place2, self.destination)
        elif self.num == '3':
            print('禁止通行车辆:浙C796YR')
            shutil.copy(self.place3, self.destination)
        elif self.num == '4':
            print('禁止通行车辆:浙D8789H')
            shutil.copy(self.place4, self.destination)
        elif self.num == '5':
            print('禁止通行车辆:沪C05EV8')
            shutil.copy(self.place5, self.destination)
        else:
            print('全部通行')
            shutil.copy(self.placeAll, self.destination)


if __name__ == "__main__":
    num = sys.argv[1]
    p = Place(num)
    p.change()
