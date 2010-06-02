#!/usr/bin/env python
# encoding: utf-8
"""
fuckoidmodel.py

Created by Juha Autero on 2010-05-15.
Copyright (c) 2010 Juha Autero. All rights reserved.
"""

from google.appengine.ext import db
from fucksporemodel import Fuckspore

class FuckoidFeed(db.Expando):
    URL=db.StringProperty()
    last_visited=db.DateProperty()
    polling_interval=db.IntegerProperty()
    fuckspore=db.ReferenceProprety(Fuckspore)
    
class Fuckoid(db.Expando):
	origin=db.ReferenceProprety(FuckoidFeed)
	timestamp=db.DateProperty()
    title=db.StringProperty()
    content=db.StringProperty(multiline=True)
    link=db.StringProperty()