#!/usr/bin/python3

import threading
import sys
import subprocess
import os

def search_file(name,directory):
    command = 'find{} -name "{}"'.format(directory,name)
    output= subprocess.check.output(command, shell=True,universal_newlines=True)
    locations=output.strip().split('\n')
    return locations

class SearchThread(threading.Thread):
    def __init__ (self, directory, name):
        threading.Thread.__init__(self)
        self.directory=directory
        self.name=name
        self.results=[]

def run(self):
    command = 'find{} -name "{}"'.format(self.directory,self.name)
    output=os.popen(command)
    for line in output:
        self.results.append


if __name__ == '__main__':
    if len(sys.argv)<3:
        sys.exit(1)
    directory=sys.argv[1]
    names=sys.argv[2:]
    threads=[]
    for name in names:
        thread = SearchThread(directory, name) ## se crea el hilo, pipe para cada nombre que se quiere buscar, es decir, un subhilo para cada uno
        thread.start()
        threads.append(thread) ## se agregan todos los nombres a la lista "threads"
    for threads in threads:
        thread.join() ## se espera a que todos los hilos finalicen su ejecución
        print("{} : {}".format(thread.name, thread.results))
