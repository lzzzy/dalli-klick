import os
import sys
import tkinter as tk

import random
from scipy.spatial import Voronoi
import numpy as np

from PIL import Image, ImageTk

class ImageController:
    valid_images = [".jpg",".gif",".png",".tga"]
    imageFiles = []
    imageFilesIndex = None
    tileId = None
    tiles = []

    def __init__(self, root, canvas, inputDirectory):
        self.root = root
        self.canvas = canvas

        if not os.path.exists(inputDirectory):
            sys.exit("inputDirectory not found")

        for f in os.listdir(inputDirectory):
            ext = os.path.splitext(f)[1]
            if ext.lower() not in self.valid_images:
                continue
            self.imageFiles.append(os.path.join(inputDirectory,f))        
        self.imageFilesIndex = 0

    
    def resize(self, img, max_width, max_height):
        width, height = img.size
        ratio = width / height 
        if max_height * ratio <= max_width:
            return img.resize((int(max_height*ratio), max_height), Image.ANTIALIAS)
        else:
            return img.resize((max_width, int(max_width/ratio)), Image.ANTIALIAS)

    def next_image(self):
        self.canvas.delete(self.tiles)
        self.tiles.clear()
        pil_img = Image.open(self.imageFiles[self.imageFilesIndex])
        self.imageFilesIndex += 1
        pil_img = self.resize(pil_img, self.root.winfo_screenwidth(), self.root.winfo_height())
        self.imgage = ImageTk.PhotoImage(pil_img)

        width = self.imgage.width()
        height = self.imgage.height()
        self.canvas.config(width=width, height=height)

        self.canvas.create_image((0, 0), anchor=tk.NW, image=self.imgage)
    
        # return

        points = [(random.randint(0,width),random.randint(0,height)) for i in range(9)]
        # add 4 distant dummy points
        points = np.append(points, [[width*99,height*99], [-width*99,height*99], [width*99,-height*99], [-width*99,-height*99]], axis = 0)
        vor = Voronoi(points)

        polygons = {}
        for id, region_index in enumerate(vor.point_region):
            points = []
            for vertex_index in vor.regions[region_index]:
                if vertex_index != -1:  # the library uses this for infinity
                    points.append(list(vor.vertices[vertex_index]))
            points.append(points[0])
            polygons[id]=points

        for id, poly in enumerate(polygons.values()):
            self.tiles.append(
                self.canvas.create_polygon(
                    *poly, 
                    fill="#"+("%06x"%random.randint(0,16777215)),
                    outline='black',
                    width=1
                )
            )
        # remove dummy polygons
        for i in range(4):
            self.tiles.pop()

    def next_tile(self):
        self.canvas.delete(self.tiles.pop())
            