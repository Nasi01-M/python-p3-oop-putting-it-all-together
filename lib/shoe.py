#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, model, size, color):
        self.brand = brand
        self.model = model
        self.size = size
        self.color = color

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color