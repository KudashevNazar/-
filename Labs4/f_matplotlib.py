import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def save_plot(values, filename="plot.png"):
    plt.plot(values)
    plt.title("Графік")
    plt.savefig(filename)
    plt.close()
    return filename