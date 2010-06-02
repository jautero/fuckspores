#!/usr/bin/env python
# encoding: utf-8
"""
fucksporemodel.py

Created by Juha Autero on 2010-05-15.
Copyright (c) 2010 Juha Autero. All rights reserved.
"""

from google.appengine.ext import db
class Fuckspore(db.Model):
	url=db.StringProperty()
	name=db.StringProperty()
	image=db.StringProperty()
