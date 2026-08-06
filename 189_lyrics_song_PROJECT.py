import time 
import sys 
import io 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding= 'utf-8')

def print_lyrics():
    lyrics = [
        "I promise mai poori zindagi tumhari hard disk mai sirf aur sirf achhi memory store karunga",
        "512 GB RAM ki kasam tumhe kabhi bhi hang nahi hone dunga", 
        "pyaar to duniya karti hai mai to tumse pair karunga wo bhi Bluetooth ke sath",
        "aur tumhari zindagi mai koi bhi musibat aa jaye mere pyaar ke antivirus",
        "kya tum poori zindagi apna password banana chahti ho?"
      ]
    delays = [0.5, 0.9, 0.8, 0.7, 0.3] 
    print ("Will I send to her?....:\n") 
    time.sleep(1.4)
    for i, line in enumerate(lyrics):
          for char in line:
             sys.stdout.write(char)
             sys.stdout.flush()
             time.sleep(0.08)
          print()
          time.sleep(delays[i])
print_lyrics()