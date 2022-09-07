from pygame import mixer
mixer.init()
mixer.music.load('goldn-116392.mp3')
mixer.music.play()
input()
mixer.event.wait()