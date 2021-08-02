import numpy as np
import random

MAX_ELEVATION = 500
MIN_ELEVATION = -500

TERRAIN = 'terrain'

class World:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.layers =  {}

    self.generate_random_terrain()

  def generate_random_terrain(self):
    self.layers[TERRAIN] = np.zeros((self.width, self.height))

    for x in range(self.width):
      for y in range(self.height):
        self.get_layer(TERRAIN)[x, y] = random.uniform(MIN_ELEVATION, MAX_ELEVATION)

  def has_layer(self, layer_name):
    return layer_name in self.layers

  def get_layer(self, layer_name):
    return self.layers[layer_name]