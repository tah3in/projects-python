from PIL import ImageGrab
import sys , os

listorg=[]
print(os.listdir())
for i in os.listdir():
    try:
        i,Format=i.split(".")
        listorg.append(int(i))
    except:
        continue

for i in range(1000000):
    if i not in listorg:
        sc = ImageGrab.grab()
        sc.save(f"{i}.png")
        break

