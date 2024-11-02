from matplotlib import pyplot as plt
import numpy as np


def parseSimFile(filepath, inputs, outputs):
    fn: dict[int, list[tuple]] = {}
    inputs = ["A", "B", "C_in"]
    outputs = ["S", "C_out"]
    with open(filepath, "r") as f:
        for line in f:
            line = line.replace(":", "").replace("=", "")
            line = line.split()
            if line:
                print(line[1])
                if line[1] in inputs or line[1] in outputs:
                    if line[1] not in fn:
                        fn[line[1]] = []
                    fn[line[1]].append((line[0], line[2]))
    return fn


def waveform(simPath, inputs, outputs):
    data = parseSimFile(simPath, [], [])
    maxTime = 0
    # keysLen = int(len(list(data.keys)))
    fig, ax = plt.subplots(5, sharex=True, sharey=True)
    fig.set_layout_engine("constrained")
    fig.subplots_adjust(left=2, right=2, top=2, bottom=2)
    for i, key in enumerate(data.keys()):
        x_values, y_values = zip(*[(int(x), int(y)) for x, y in data[key]])
        maxTime = max(maxTime, max(x_values))
        x_values = list(x_values) + [maxTime, maxTime * 1.5]
        y_values = list(y_values) + [y_values[-1], y_values[-1]]
        ax[i].step(x_values, y_values, where="post")
        ax[i].text(
            -0.1,
            0.5,
            key,
            transform=ax[i].transAxes,
            fontsize=12,
            va="center",
            ha="right",
        )
    plt.yticks([0, 1])
    plt.xticks(np.arange(0, maxTime * 1.5, step=100))
    fig.set_size_inches(maxTime * 2 / 300, 10)
    plt.show()
