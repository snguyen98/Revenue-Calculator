import matplotlib.pyplot as plt
import numpy as np

class SnaptoCursor(object):
    def __init__(self, ax, x, y, labels):
        self.ax = ax
        self.lx = ax.axhline(color='k')  # the horiz line
        self.ly = ax.axvline(color='k')  # the vert line
        self.x = x
        self.y = y
        self.labels = labels
        # text location in axes coords
        self.txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)

    def mouse_move(self, event):
        if not event.inaxes:
            return

        x, y = event.xdata, event.ydata
        indx = min(np.searchsorted(self.x, x), len(self.x) - 1)
        x = self.x[indx]
        y = self.y[indx]
        # update the line positions
        self.lx.set_ydata(y)
        self.ly.set_xdata(x)

        self.txt.set_text("[" + self.labels[x - 1] + "] - £" + str(y))
        self.ax.figure.canvas.draw()

def draw(rev, file, type):
    xmax = len(rev) + 1
    x = np.arange(1, xmax)
    y = list(rev.values())
    fig, ax = plt.subplots(figsize = (12,5))
    ax.set_title(file + " - " + type + "ly Revenue")
    ax.set_ylabel("Revenue")
    ax.get_xaxis().set_visible(False)
    margin = (max(y) - min(y)) / 4
    if (min(y) - margin < 0):
        lbound = 0
    else:
        lbound = min(y) - margin
    ax.set_ylim(lbound, max(y) + margin)
    ax.set_xlim(xmax - 0.9, 0.9)
    ax.plot(x,y)
    cursor = SnaptoCursor(ax, x, y, np.array(list(rev.keys())))
    fig.canvas.mpl_connect("motion_notify_event", cursor.mouse_move)
    plt.show()
