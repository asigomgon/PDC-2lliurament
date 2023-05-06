#!/usr/bin/python3

import os
import sys
import threading

class SearchThread (threading.Thread):
    def __init__(self,root_dir, filename):
        threading.Thread.__init__(self)
        self.root_dir=root_dir
        self.filename=filename
        self.locations= []


    def run(self):
        cmd= f"find {self.root_dir} -name '{self.filename}'"
        with os.popen(cmd) as pipe:
            for line in pipe:
                self.locations.append(line.strip())

    def __str__(self):
        return f"{self.filename}: {self.locations}"

if __name__=="__main__":
    root_dir=sys.argv[1]
    filenames=sys.argv[2:]

    threads = []
    for filename in filenames:
        t= SearchThread(root_dir, filename)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        print(t)

        
