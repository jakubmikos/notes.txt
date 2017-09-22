from sys import argv
import subprocess
from os import listdir
import fnmatch

import argparse

def slugify(text):
    return text.replace(' ', '-')

def createNote(title):
    print('Adding note...')
    filename = '{}.txt'.format(slugify(title))
    header = '# {}'.format(title)
    newNote = open(filename, 'w')
    newNote.write(header)
    newNote.close()
    return filename

def edit(filename):
    subprocess.call(['vim', filename])
    print ('note edited and saved')

def listNotes():
    for index, file in enumerate(listdir('.')):
        if fnmatch.fnmatch(file, '*.txt'):
            print ('[{}] {}'.format(index, file))

def addNote(args):
    createdNote = createNote(args.note_title)
    edit(createdNote)

def listAll(args):
    listNotes()
    
parser = argparse.ArgumentParser(prog='Notes.txt', description='Notes.txt plaintext notes mamanger.')
subparsers = parser.add_subparsers()

parser_add = subparsers.add_parser('add', help='Add note')
parser_add.add_argument('note_title', help='Note title')
parser_add.set_defaults(func=addNote)

parser_list = subparsers.add_parser('ls', help='List all notes')
parser_list.set_defaults(func=listAll)

parsed = parser.parse_args()
parsed.func(parsed)

