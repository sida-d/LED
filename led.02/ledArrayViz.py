# Library support for 2D LED strip arrays
# By Brygg Ullmer, Sida Dai, and Mitali Bhosekar, Clemson University
# Begun 2022-04-13

from ledArray import *
import pygame as pyg

############## numpy|ulab 2D character array #############

class ledArrayViz: 
  ledArrayHandle   = None
  rectList         = None
  vertList         = None
  rectDim          = (2,2)
  basePos          = (50, 50)
  dx, dy           = 5, 5
  defaultRectColor = (50, 50, 50)
  vert2idx, idx2vert, idx2rect = [None]*3

  ############## constructor ##############

  def __init__(self, ledArray):
    self.ledArrayHandle = ledArray
    self.constructGridViz()

  ############## construct rects ##############

  def constructGridViz(self):
    print("ledArrayViz constructor called")

    rows, cols = self.ledArrayHandle.getShape()
    self.vertList = []; self.vert2idx = {}; self.idx2vert = {}

    cy = self.basePos[1]

    for i in range(rows):
      cx = self.basePos[0]
      for j in range(cols):
        vert = (cx, cy)
        self.vertList.append(vert)
        idx = (i, j)
        self.vert2idx[vert] = idx
        self.idx2vert[idx]  = vert
        cx += self.dx
      cy += self.dy

    self.constructRects()

  ############## construct rects ##############

  def constructRects(self):
    self.rectList = []
    #print("constructRects:", self.vertList)
    self.idx2rect = {}

    for vert in self.vertList:
      rect = pyg.Rect(vert, self.rectDim)
      idx  = self.vert2idx[vert]
      #print(idx, vert)
      self.idx2rect[idx] = rect

  ############## draw rects ##############

  def drawRects(self, screen):
    #print("drawRects:", self.vertList)
    for vert in self.vertList:
      idx  = self.vert2idx[vert]
      #print("dr1:", vert, idx)
      rect = self.idx2rect[idx]
      color = self.ledArrayHandle.getIdxColor(idx)
      #print("dr2:", idx, color)
      if color == (0, 0, 0) or color == None: 
        color = self.defaultRectColor

      screen.draw.filled_rect(rect, color)

  ############# pgzero draw #############

  def draw(self, screen):
    self.drawRects(screen)
    
### end ###