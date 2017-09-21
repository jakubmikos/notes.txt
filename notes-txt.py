from sys import argv
import subprocess
from os import listdir
import fnmatch

def slugify(text):
    return text.replace(' ', '-')

def addNote(title):
    filename = '%s.txt' % slugify(title)
    print (filename)
    newNote = open(filename, 'w')
    header = '# %s' % title
    print (header)
    newNote.write(header)
    newNote.close()
    return filename

def edit(filename):
    subprocess.call(['vim', filename])
    print ('note edited and saved')

def listNotes():
    for index, file in enumerate(listdir('.')):
        if fnmatch.fnmatch(file, '*.txt'):
            print ('[%d] %s' % (index, file))
    


print (argv)
if len(argv) > 1:
    command = argv[1]
    if command == 'add':
        print ('adding note...')
        filename = addNote(argv[2])
        edit(filename)
    elif command == 'ls':
        listNotes()
    elif command == 'open':


