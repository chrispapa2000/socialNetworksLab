import random
import matplotlib.pyplot as plt

def flip_coin():
        r = random.randint(0,1)
        if r==0:
            return -1
        else:
            return 1

def main():
    k = 1000000
    x = []
    y = []
    count = 0
    fig, ax = plt.subplots()
    ax.grid()
    for i in range(k):
        count+=flip_coin()
        y.append(count)
        x.append(i)
        plt.plot(x,y)
        plt.pause(0.0000000001)

    plt.plot(x,y)
    plt.show()


if __name__=='__main__':
    main()
