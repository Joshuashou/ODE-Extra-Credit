import numpy as np
import matplotlib.pyplot as plt


def Benfords(n, exponent):
    bins = [0] * 10  # Bin array holding counts for each digit
    num = 1
    for i in range(n):
        num *= exponent
        digit = int(str(num)[0])
        bins[digit] += 1
    return bins


if __name__ == '__main__':
    benford_2 = Benfords(1000, 2)
    plt.plot(benford_2)
    plt.title("First digit for 2^n")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    axis = plt.subplot()
    axis.set_xlim(1, 9)
    plt.show()

    benford_3 = Benfords(1000, 3)
    plt.plot(benford_3)
    plt.title("First digit for 3^n")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    axis = plt.subplot()
    axis.set_xlim(1, 9)
    plt.show()

    benford_13 = Benfords(1000, 13)
    plt.title("First digit for 13^n")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.plot(benford_13)
    axis = plt.subplot()
    axis.set_xlim(1, 9)
    plt.show()

    benford_19 = Benfords(1000, 19)
    plt.plot(benford_19)
    plt.title("First digit for 19^n")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    axis = plt.subplot()
    axis.set_xlim(1, 9)
    plt.show()

#End