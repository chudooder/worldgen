import numpy as np
import tkinter as tk
from gui.application import WorldGenApp
from world import World


if __name__ == '__main__':

  world = World(200, 200)

  root = tk.Tk()
  app = WorldGenApp(master=root, world=world)
  app.mainloop()