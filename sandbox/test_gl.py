#!/usr/bin/python

import pyglet

config = pyglet.gl.Config(major_version=4, minor_version=0)

window = pyglet.window.Window(config=config)

print('GL version: ', window.context.get_info().get_version())

input()

window.close()
