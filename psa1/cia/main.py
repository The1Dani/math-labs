from PIL import Image
import random

im = Image.open("danger_zone.png")

def is_red(x:int, y:int):

    return bool(im.getpixel((x, y))[0])

def carlo(n=1_000):
    
    hits = 0

    for _ in range(n):
        x = random.randint(0, im.size[0] - 1)
        y = random.randint(0, im.size[1] - 1)
        if is_red(x, y):
            hits += 1
    return hits / n

def main():
    exp = int(input("Enter the number of experiments: "))
    print(f"{carlo(exp)*42:.2f} sqare miles")

if __name__ == "__main__":
    main()