import threading
import sys
import json

dicctionary= {}

class wordThread(threading.Thread):
   def __init__(self, _dictionary, _word):
          threading.Thread.__init__(self)
          self.dictionary = _dictionary
          self.word = _word
   def run(self):
          print ("processing " + self.word)
          # Get lock to synchronize threads
          threadLock.acquire()
          updateDictionary(self.dictionary, self.word)
          # Free lock to release next thread
          threadLock.release()

def updateDictionary(_dictionary, _word):
    if _word not in _dictionary:
        _dictionary[_word] = 1
    else:
        _dictionary[_word] += 1


threadLock = threading.Lock()
threads = []

print(sys.argv[0])
print(sys.argv[1])
if len(sys.argv) < 3:
    print("usage: file_name word .... word")
    sys.exit(1)

for word in sys.argv[2:] :
    thread = wordThread(dicctionary, word)
    thread.start()
    threads.append(thread)


# Wait for all threads to complete
for t in threads:
    t.join()

with open('{0}.json'.format(sys.argv[1]), 'w') as jsonFile:
    json.dump(dicctionary, jsonFile)

print ("Exiting Main Thread")