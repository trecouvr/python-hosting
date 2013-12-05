#!/usr/bin/env python

import sys
import os

DIR = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(DIR, '..'))
ROOT_TEMPLATES = os.path.join(ROOT, 'templates')
TMPL_PATH = os.path.join(ROOT_TEMPLATES, 'nginx.conf')
DEST_PATH = os.path.join(ROOT, 'nginx.conf')

def make_conf():
    tmpl = open(TMPL_PATH).read()
    r = tmpl.replace('<%root%>', ROOT)
    print r
    open(DEST_PATH, 'w').write(r)

if __name__ == '__main__':
    make_conf()
        
