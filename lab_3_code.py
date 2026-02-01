import random, time
import matplotlib.pyplot as plt

temps = []
for t in range (10):
    temp = 25 + random.uniform(-1, 1)
    temps.append(temp)
    with open("temps.txt", "a") as f:
        f.write(f"{temp}\n")
    time.sleep(0.5)

plt.plot(temps)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")     
plt.title("Temperature over Time")
plt.show()   