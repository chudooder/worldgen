import tkinter as tk
import world

def map_to_color(height):
  print(height)
  int_val = int(float(height - world.MIN_ELEVATION) / (world.MAX_ELEVATION - world.MIN_ELEVATION) * 256)
  return "#%02x%02x%02x" % (int_val, int_val, int_val)

class WorldView(tk.Frame):
  def __init__(self, master=None, world=None):
    super().__init__(master)
    self.master = master
    self.world = world

    self.pack()
    self.create_widgets()

  # Returns string to insert into a PhotoImage
  def render_world(self):
    terrain = self.world.get_layer(world.TERRAIN)
    pixels = ' '.join(('{' + ' '.join(map_to_color(terrain[x, y]) for x in range(self.world.width))) + '}' \
      for y in range(self.world.height))
    return pixels


  def create_widgets(self):
    self.photo_image = tk.PhotoImage(height=self.world.height, width=self.world.width)
    self.photo_image.put(self.render_world(), (0, 0, self.world.width - 1, self.world.height - 1))
    self.world_view = tk.Canvas(self, height=self.world.height, width=self.world.width)
    self.world_view.create_image(0, 0, anchor='nw', image=self.photo_image)
    self.world_view.pack()
