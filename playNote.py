import pyglet

def main():
    effectA = pyglet.resource.media("Piano.ff.C4.aiff", streaming=False)
    while(1):
        effectA.play()
        pyglet.clock.schedule_once(lambda dt: pyglet.app.exit(), effectA.duration)
        pyglet.app.run()

if __name__ == "__main__":
    main()