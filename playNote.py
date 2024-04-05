import pyglet

def main():
    effectA = pyglet.resource.media("Piano.ff.C4.aiff",streaming=False)
    effectA.play()


if __name__ == "__main__":
    main()