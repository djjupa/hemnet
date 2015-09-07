#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2013 Hugo Lindström <hugolm84@gmail.com>
#
#
# local includes
#
#  from hemnet import hemnet

from flask import Blueprint, make_response, jsonify, request
from sys import argv
import os

#from parser import hemnet as parser
#from utils import cache

script, filename_input = argv

current_dir = os.getcwd();

print "Current directory: " + current_dir

filename = current_dir + "/data/booli.json" 
#filename = current_dir + "/data/" + filename_input


print "Opening the file..."
target = open(filename, 'w')

print "Writing to file..."
target.write("hello")