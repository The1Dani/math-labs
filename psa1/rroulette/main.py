from random import choice

def rroulette(chamber:list):
    return 0 if choice(chamber) == 0 else 1

def calc_alive(chamber:list, reps:int):

    dead = 0

    for _ in range(reps):
        dead += 1 if rroulette(chamber) == 1 else 0

    avg = (1 - dead/reps)*100
    print(f"Average wins: {avg:.2f}% ~{round(avg)}%\n")

def main():

    reps = 1_000_000

    # 6 barrel chamber with one fired and two bullets
    chamber = [0, 0, [1, 1], 0]
    print("6 barrel one fired two adj not spinned")
    calc_alive(chamber, reps)
    
    #? if we spin the barrel we would return to the original state and the chamber 
    #? before it was fired so we have to add the shot to the chamber (empty space)

    chamber.append(0)
    print("6 barrel one fired two adj spinned")
    calc_alive(chamber, reps)


    #? If the bullets are not adjecent to each other and the first shot did not kill us
    chamber = [0, 1, 0, 1, 0]
    print("6 barrel one fired two not adj not spinned")
    calc_alive(chamber, reps)

    #? If the bullets are not adjecent and we spin the barrel
    chamber.append(0)
    print("6 barrel one fired two not adj spinned")
    calc_alive(chamber, reps)

    ################## 5 barrel scenarios

    #? 5 barrel chamber with one fired and two bullets adjacent
    chamber = [0, 0, [1, 1]]
    print("5 barrel one fired two adj not spinned")
    calc_alive(chamber, reps)

    #? 5 barrel chamber with one fired and spinned
    chamber.append(0)
    print("5 barrel one fired two adj spinned")
    calc_alive(chamber, reps)

    #? 5 barrel chamber with one fired and two bullets not adjacent
    chamber = [0, 1, 0, 1]
    print("5 barrel one fired two not adj not spinned")
    calc_alive(chamber, reps)

    #? 5 barrel chamber with one fired and spinned
    chamber.append(0)
    print("5 barrel one fired two not adj spinned")
    calc_alive(chamber, reps)


if __name__ == "__main__":
    main()
    