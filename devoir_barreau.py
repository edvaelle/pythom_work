import random
import sys

def antre() -> int:
    num = input("mete on nonb ant 0 e 500: ")
    if num.isdigit() and (int(num) >=0 and int(num) <=500):
        return int(num)
    else:
        print("antre on bon nonb...\n") 
        return antre() 

def random_number() -> int:
    return random.randint(0, 500)

def kontinye(value: int=2)-> bool:
    ch = input("eskew vle kontinye (1: kontinye; 2: kite): ")
    if ch.isdigit(): return True if int(ch)==1 else False
    return kontinye()

def run():
    const = True
    luck = 5
    while const:
        print("-"*70)
        if luck > 0:
            random_num = random_number()
            user_input = antre()
            if user_input < random_num:
                print(f"nonb lan se: {random_num} - ou chwazi {user_input} - nonb ou chwazi a two piti.")
            elif user_input > random_num:
                print(f"nomb lan se: {random_num} - ou chwazi {user_input} - nonb ou chwazi a two gran.")
            elif user_input == random_num:
                print(f"nomb lan se: {random_num} - ou chwazi {user_input} - ou genyen")
                luck = 5
                r = kontinye()
                if r: continue
                else: sys.exit()
            luck -= 1
            print(f"ou rete {luck} chans.\n".format())
        else: 
            const = False

run()