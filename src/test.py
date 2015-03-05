#!/usr/bin/env python

import os
import argparse
from sys import version_info as py_version
from files import PlainTextFileHandler as FHandler

fd = FHandler(r"C:\Users\informatic_26\Documents\GitHub\cottp\data\raw_twitter\rg1cat")

#http://www.dotnetperls.com/split-python examples for parsing estrings

def checkPyVersion(major,minor):
    if (major > py_version.major
        or (major == py_version.major and minor > py_version.minor)):
        print("The script must run with python version {}.{} or later".format(major,minor))
        input("Pres enter to close...")
        exit(1)
    return true
        
def parseTweet(entry):
    [t_id,separator,entry] = entry.partition(" ")
    [date,separator,entry] = entry.partition("<")
    [name,separator,msg] = entry.partition(">")
    print(t_id)
    print(date[2:])
    print(name)
    print(msg.strip()[:-1])
    return (int(t_id.strip()),date[2:].strip(),name.strip(),msg.strip()[:-1])

def processRawFolder(folder_path):
    path = r"%s" % directory

    for file in os.listdir(path):
        current_file = os.path.join(path, file)
        with open(current_file, "rb") as fd:
            print("=========")
            print(current_file)
            print(parseTweet(fd.readline()))
            print("=========")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "process a folder with files of raw twitter accouns msg extraction

    
