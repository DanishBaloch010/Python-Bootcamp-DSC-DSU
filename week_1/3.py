import time

song="""Birds flying high, you know how I feel
Sun in the sky, you know how I feel
Breeze driftin' on by, you know how I feel

Fish in the sea, you know how I feel
River running free, you know how I feel
Blossom on the tree, you know how I feel

Dragonfly out in the sun, you know what I mean, don't you know?
Butterflies all havin' fun, you know what I mean
Sleep in peace when day is done, that's what I mean
And this old world is a new world
And a bold world, for me

Stars when you shine, you know how I feel
Scent of the pine, you know how I feel
Oh, freedom is mine
And I know how I feel

I'm feeling good!"""

def printSong(str):
    for oneLine in str.splitlines():
        print(oneLine)
        time.sleep(1)

printSong(song)


