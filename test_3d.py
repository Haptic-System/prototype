# -*- coding: utf-8 -*-



import communication_serie as cali_arduino
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl


app = pg.mkQApp("GLMeshItem Example")
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
w.setCameraPosition(distance=40)

g = gl.GLGridItem()
g.scale(2,2,1)
w.addItem(g)

import numpy as np


## Example 3:
## sphere

md = gl.MeshData.sphere(rows=10, cols=20)
#colors = np.random.random(size=(md.faceCount(), 4))
#colors[:,3] = 0.3
#colors[100:] = 0.0
"""
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m3 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')

m3.translate(5, -5, 0)
w.addItem(m3)
"""

###########

#colors = np.random.random(size=(md.faceCount(), 4))
#colors[:,3] = 0.3
#colors[100:] = 0.0
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m4 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')

m4.translate(0, 0, 0)
w.addItem(m4)

class Data:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

data = Data()

def measure_and_move_x(data,xmes):
    new_x = data.x
    if not xmes is None:
        data.x = xmes * 40 - 12
    # print("data.x: ", data.x)
    if not new_x is data.x:
        goto_x(data.x, new_x)

def measure_and_move_y(data,ymes):
    new_y = data.y
    if not ymes is None:
        data.y = -ymes * 40 + 15
    #print("data.y: ", data.y)
    if not new_y is data.y:
        goto_y(data.y, new_y)

def measure_and_move_z(data,zmes):
    new_z = data.z
    if not zmes is None:
        data.z = -zmes * 40 + 12.5
    #print("data.z: ", data.z)
    if not new_z is data.z:
        goto_z(data.z, new_z)


def measure_and_move_all(data):
    measure = cali_arduino.mesure()
    if not measure is None:
        # print("measure: ", measure)
        # print("measure[-1]: ", measure[-1])
        xmes = measure[-1][0]
        ymes = measure[-1][1]
        zmes = measure[-1][2]
    measure_and_move_x(data,xmes)
    measure_and_move_y(data,ymes)
    measure_and_move_z(data,zmes)


def goto_x(old_x, new_x):
    x_translation = old_x - new_x
    m4.translate(x_translation, 0 ,0)

def goto_y(old_y, new_y):
    y_translation = old_y - new_y
    m4.translate(0, y_translation ,0)

def goto_z(old_z, new_z):
    z_translation = old_z - new_z
    m4.translate(0, 0,z_translation)
###########################################

# def sphere_Xmovement(val, relative=True):
#     x = sphere.xcor()
#     if relative:
#         x += (val-.5)*width
#     else:
#         x = (val-.5)*width
#     print("x: ", x)
#     x = -x
#     sphere.setx(x)







if __name__ == '__main__':


    timer = QtCore.QTimer()
    timer.timeout.connect(lambda : measure_and_move_all(data))
    timer.start(10)
    pg.mkQApp().exec_()


    # while True:
    #     measure = cali_arduino.mesure()
    #     if not measure is None:
    #         val = measure
    #     print("val: ", val)
