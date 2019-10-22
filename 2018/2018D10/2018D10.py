
#!/usr/bin/python

filepath = 'input.txt'
import re
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from datetime import datetime
startTime = datetime.now()

def main():
    pos , speed = [], []
    time = 0
    with open(filepath) as f:
        for line in f.readlines():
            read = [int(i) for i in re.findall(r'-?\d+\.?\d*', line)]
            pos.append([read[0], read[1]*-1])
            speed.append([read[2], read[3]*-1])
        f.close()

    app = QtGui.QApplication([])
    win = pg.GraphicsWindow()
    p1 = win.addPlot(title="plot1")

    while(True):
        time+=1
        for index in range(len(pos)):
            pos[index][0] = pos[index][0] + speed[index][0]
            pos[index][1] = pos[index][1] + speed[index][1]

        data = list(zip(*pos))
        if (max(data[1]) - min(data[1])) < 10:
            p1 = pg.plot(data[0], data[1], pen=None, symbol='o')
            break

    return time

if __name__ == '__main__':
    print(main(), str(datetime.now() - startTime)[:-3])
    input()