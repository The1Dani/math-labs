from random import randint, choice


class Gun:

    def __init__(self, chamber_size:int, load:int, sidebs=False) -> None:
        self.chamber_size = chamber_size
        self.chamber = [False] * chamber_size
        self.loaded = load

        # Load the gun
        if not sidebs:
            [self.load_arb() for _ in range(load)]
            # self.rand_spin()
        else:
            for i in range(load if load < chamber_size else chamber_size):
                self.chamber[i] = True
            self.rand_spin()

    def load_arb(self):

        if  all(not i for i in self.chamber):
            self.chamber[choice(range(self.chamber_size))] = True

        next_bul_pos = choice(range(self.chamber_size))


        if (next_bul_pos + 1 > self.chamber_size - 1) or (next_bul_pos - 1 < 0):
            self.load_arb()
        else:
            cond = self.chamber[0] and next_bul_pos == self.chamber_size - 1 or self.chamber[self.chamber_size - 1] and next_bul_pos == 0
                

            if (self.chamber[next_bul_pos] or (self.chamber[next_bul_pos + 1] or self.chamber[next_bul_pos - 1])) and cond:
                self.load_arb()
                
            else:
                self.chamber[next_bul_pos] = True

    def rand_spin(self):
        [self.spin() for _ in range(randint(1, self.chamber_size)) ]

    def spin(self):
        #? This rotates the chamber one time meaning the last goes to the first
        # self.chamber = self.chamber[-1:] + self.chamber[:-1]
        # print(self.chamber[-1:], self.chamber[:-1])
        self.chamber = self.chamber[-1:] + self.chamber[:-1]

    def fire(self):
        if self.chamber[0]:
            self.chamber[0] = False
            self.loaded -= 1
            self.spin()
            return True
        else:
            self.spin()
            return False
    
    
    def __str__(self) -> str:
        return f"Gun Chamber: {list(map(int, self.chamber))}, Loaded: {self.loaded}"

def experiment(chamber_size, bullets, sidebs:bool , spin:bool):
    gun = Gun(chamber_size, bullets, sidebs)
    if not gun.fire():
        gun.rand_spin() if spin else None
        if not gun.fire():
            return True
        else:
            return False
    return experiment(chamber_size, bullets, sidebs, spin)


def main():
    c = 0
    r = 100_000

    #! experiment(Chamber_size, Bullets, Side_by_Side, Spin)

    for _ in range(r):
        if experiment(6, 2, True, False):
            c += 1

    print(f"6 barrel 2 adj dont spin {round(c/r * 100)}%")
    
    c = 0

    for _ in range(r):
        if experiment(6, 2, True, True):
            c += 1
    
    print(f"6 barrel 2 adj do spin {round(c/r * 100)}%")
    
    print()    

    c = 0

    for _ in range(r):
        if experiment(6, 2, False, False):
            c += 1
    
    print(f"6 barrel 2 not sbs dont spin {round(c/r * 100)}%")

    c = 0

    for _ in range(r):
        if experiment(6, 2, False, True):
            c += 1

    print(f"6 barrel 2 not sbs do spin {round(c/r * 100)}%")

    print()

    c = 0

    for _ in range(r):
        if experiment(5, 2, True, False):
            c += 1
    
    print(f"5 barrel 2 adj dont spin {round(c/r * 100)}%")

    c = 0

    for _ in range(r):
        if experiment(5, 2, True, True):
            c += 1
    
    print(f"5 barrel 2 adj do spin {round(c/r * 100)}%")

    print()

    c = 0

    for _ in range(r):
        if experiment(5, 2, False, False):
            c += 1
        
    print(f"5 barrel 2 not sbs dont spin {round(c/r * 100)}%")

    c = 0

    for _ in range(r):
        if experiment(5, 2, False, True):
            c += 1
    
    print(f"5 barrel 2 not sbs do spin {round(c/r * 100)}%")

    print()



if __name__ == "__main__":
    
    # for _ in range(10):
    #     gun = Gun(6, 2)
    #     print(gun)
    
    main()
    