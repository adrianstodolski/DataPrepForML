import csv
import os
import pandas as pd
from matplotlib import pyplot as plt


# Dataset:
x = [10, 20, 33, 29, 17, 18, 45, 2, 26, 5, 18, 22, 28]
y1 = [7.03, 3.46, 2.66, 8.22, 9.31, 4.41, 1.56, 8.77, 10.31, 7.83, 2.21, 3.34, 4.43]
y2 = [1.71, 2.82, 3.93, 4.84, 5.75, 6.66, 7.57, 8.48, 9.39, 7.24, 6.13, 7.11, 8.12]
y3 = [9.96, 6.77, 8.76, 5.97, 8.98, 2.99, 3.88, 6.77, 1.45, 9.32, 7.21, 1.38, 2.11]
y4 = [2, 2, 2, 2, 2, 2, 2, 11, 2, 2, 2, 2, 11]
x4 = [2.22, 3.33, 4.44, 5.55, 6.66, 7.77, 8.88, 9.99, 10.11, 10.12, 13.01, 14.20, 11.12]

# Dictionaries:
dictionaries_ds = {"y1": y1, "y2": y2, "y3": y3, "y4": y4}
dictionaries_x = {"x": x, "y1": y1, "y2": y2, "y3": y3, "y4": y4}
dictionaries_x4 = {"x4": x4, "y1": y1, "y2": y2, "y3": y3, "y4": y4}

# Pandas DataFrames
dataframe_ds = pd.DataFrame(
    dictionaries_ds, index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
)
dataframe_x = pd.DataFrame(
    dictionaries_x, index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
)
dataframe_x4 = pd.DataFrame(
    dictionaries_x4, index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
)

# Definitions
def mean_cal(dataframe: pd.DataFrame) -> pd.Series:
    """ Calculates mean value.
    Args:
        dataframe: pandas DataFrame.
    Returns: 
        Mean value of pandas DataFrame.
    """
    mean_cal = dataframe.mean().round(2)
    return mean_cal


def std_cal(dataframe: pd.DataFrame) -> pd.Series:
    """ Calculates standard deviation value. 'Ddof' means delta degrees of freedom.
    Args:
        dataframe: Pandas DataFrame.
    Returns: 
        Standard deviation value of pandas DataFrame.
    """
    std_cal = dataframe.std(ddof=0).round(2)
    return std_cal


def variance_cal(dataframe: pd.DataFrame) -> pd.Series:
    """ Calculates variance value of pandas DataFrame.
    Args:
        dataframe: Pandas DataFrame.
    Returns: 
        Variance value of pandas DataFrame.
    """
    variance_cal = dataframe.var().round(1)
    return variance_cal


def correlation_cal(dataframe: pd.DataFrame) -> pd.DataFrame:
    """ Calculates Pearson correlation coefficient value of DataFrame.
    Args:
        dataframe: Pandas DataFrame.
    Returns:
        Pearson correlation coefficient value of pandas DataFrame.
    """
    correlation_cal = dataframe.corr(method="Pearson").round(2)
    return correlation_cal


def plot_cal(
    dataset1: pd.Series, dataset2: pd.Series, dataset3: pd.Series
) -> plt.subplot:
    """ Creates one figure with three subplots.
    Args:
        dataset1: First dataset to plot.
        dataset2: Second dataset to plot.
        dataset3: Third dataset to plot.
    Returns: One figure with three subplots.
    """
    plt.style.use("seaborn")
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True)

    title_font = {"family": "arial", "weight": "bold", "color": "black", "size": 15}
    label_font = {"family": "arial", "weight": "bold", "color": "black", "size": 10}

    ax1.set_title("Mean", fontdict=title_font)
    ax2.set_title("Standard deviation", fontdict=title_font)
    ax3.set_title("Variance", fontdict=title_font)

    # Plot 1 settings
    ax1.set_ylabel("Value", fontdict=label_font)
    (line1,) = ax1.plot(dataset1, color="r", marker="o", label="Mean",)
    ax1.legend(loc=0)

    # Plot 2 settings
    ax2.set_ylabel("Value", fontdict=label_font)
    (line1,) = ax2.plot(dataset2, color="b", marker="o", label="Standard deviation",)
    ax2.legend(loc=0)

    # Plot 3 settings
    ax3.set_ylabel("Value", fontdict=label_font)
    (line1,) = ax3.plot(dataset3, color="g", marker="o", label="Variance",)
    ax3.legend(loc=0)

    plt.tight_layout()
    plt.show()
    return fig


def plot_pearson(dataset1: pd.DataFrame, dataset2: pd.DataFrame) -> plt.subplot:
    """ Creates one figure with twp subplots.
    Args:
        dataset1: First dataset to plot.
        dataset2: Second dataset to plot.
    Returns: One figure with three subplots.
    """
    plt.style.use("seaborn")
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)

    title_font = {"family": "arial", "weight": "bold", "color": "black", "size": 15}
    label_font = {"family": "arial", "weight": "bold", "color": "black", "size": 10}

    ax1.set_title("Pearson x correlation coefficient", fontdict=title_font)
    ax1.set_ylabel("Value", fontdict=label_font)

    ax2.set_title("Pearson x4 correlation coefficient", fontdict=title_font)
    ax2.set_ylabel("Value", fontdict=label_font)
    ax2.set_xlabel("y dataset", fontdict=label_font)

# Plot 1 settings
    (line1,) = ax1.plot(
        dataset1["y1"],
        color="r",
        marker="o",
        label="Pearson correlation coefficient for y1",
    )
    ax1.legend(loc=10)

    (line2,) = ax1.plot(
        dataset1["y2"],
        color="g",
        marker="o",
        label="Pearson correlation coefficient for y2",
    )
    ax1.legend(loc=10)

    (line3,) = ax1.plot(
        dataset1["y3"],
        color="b",
        marker="o",
        label="Pearson correlation coefficient for y3",
    )
    ax1.legend(loc=10)

    (line4,) = ax1.plot(
        dataset1["y4"],
        color="m",
        marker="o",
        label="Pearson correlation coefficient for y4",
    )
    ax1.legend(loc=10)

# Plot 2 settings
    (line1,) = ax2.plot(
        dataset2["y1"],
        color="r",
        marker="o",
        label="Pearson correlation coefficient for y1",
    )
    ax2.legend(loc=10)

    (line2,) = ax2.plot(
        dataset2["y2"],
        color="g",
        marker="o",
        label="Pearson correlation coefficient for y2",
    )
    ax2.legend(loc=10)

    (line3,) = ax2.plot(
        dataset2["y3"],
        color="b",
        marker="o",
        label="Pearson correlation coefficient for y3",
    )
    ax2.legend(loc=10)
    (line4,) = ax2.plot(
        dataset2["y4"],
        color="m",
        marker="o",
        label="Pearson correlation coefficient for y4",
    )
    ax2.legend(loc=10)

    plt.tight_layout()
    plt.show()
    return fig

# Main definition
def main():
    """ Main function
    Returns: All required in exercise data and plots.
    """

    mean = mean_cal(dataframe_ds)
    standard_deviation = std_cal(dataframe_ds)
    variance = variance_cal(dataframe_ds)
    x_correlation = correlation_cal(dataframe_x)
    x4_correlation = correlation_cal(dataframe_x4)

    print(
        f"Mean value is:\n"
        f"{mean}\n"
        f"Standard deviation is:\n"
        f"{standard_deviation}\n"
        f"Variance is:\n"
        f"{variance}\n"
        f"Pearson correlation coefficient for x is:\n"
        f"{x_correlation}\n"
        f"Pearson correlation coefficient for x4 is:\n"
        f"{x4_correlation}"
    )

# Directory for results
    file_dir = os.path.dirname(__file__)
    result_dir = os.path.join(file_dir, "Result\\")

    """Checking is current directory already exists:
        If no, creating it and saving figures
        If yes, just saving figures
    """
    if not os.path.isdir(result_dir):
        os.makedirs(result_dir)
    fig1 = plot_cal(mean, standard_deviation, variance).savefig(
        result_dir + "fig1"
    )
    fig2 = plot_pearson(x_correlation, x4_correlation).savefig(
        result_dir + "fig2"
    )

    file = open(result_dir + "calculation.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow([mean, mean])
    writer.writerow([standard_deviation, standard_deviation])
    writer.writerow([variance, variance])
    writer.writerow([x_correlation, x_correlation])
    writer.writerow([x4_correlation, x4_correlation])

    file.close()


if __name__ == "__main__":
    main()
