import tkinter as tk
from gui.worldview import WorldView

class WorldGenApp(tk.Frame):
  def __init__(self, master=None, world=None):
    super().__init__(master)
    self.master = master
    self.world = world

    self.pack()
    self.create_widgets()

  def create_widgets(self):
    self.hi_there = tk.Button(self)
    self.hi_there['text'] = 'hello world!!'
    self.hi_there['command'] = self.say_hi
    self.hi_there.pack(side='top')

    self.world_view = WorldView(master=self, world=self.world)
    self.world_view.pack(side='right')

    self.quit = tk.Button(self, text='QUIT', fg='red', command=self.master.destroy)
    self.quit.pack(side='bottom')

  def say_hi(self):
    print('hi there')
