import pyglet

# pick an animated gif file you have in the working directory
ag_file = "Final.gif"
animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)

win = pyglet.window.Window(width=sprite.width, height=sprite.height)

green = 0, 1, 0, 1
pyglet.gl.glClearColor(*green)

@win.event
def on_draw():
    win.clear()
    sprite.draw()

pyglet.app.run()