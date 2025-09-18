import os
import time
import matplotlib.pyplot as plt
import seaborn as sns
from .loader import load_fitness_data

def compare_formats(files):
    load_times = []
    file_sizes = []

    for f in files:
        start = time.time()
        df = load_fitness_data(f)
        end = time.time()
        load_times.append(end - start)
        file_sizes.append(os.path.getsize(f) / 1024)  # KB

    # Plot load times
    sns.barplot(x=files, y=load_times)
    plt.title("File Loading Time Comparison")
    plt.ylabel("Time (s)")
    plt.savefig("reports/load_time_comparison.png")
    plt.show()

    # Plot file sizes
    sns.barplot(x=files, y=file_sizes)
    plt.title("File Size Comparison")
    plt.ylabel("Size (KB)")
    plt.savefig("reports/file_size_comparison.png")
    plt.show()
