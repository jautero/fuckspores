#!/usr/bin/env python
# encoding: utf-8
"""
feed_fetcher.py

Created by Juha Autero on 2010-06-16.
Copyright (c) 2010 Juha Autero. All rights reserved.
"""

import unittest
import feedparser, StringIO
from google.appengine.api import urlfetch


class FeedFetcher:
    def __init__(self,feed):
        self.feed=feed
    def parse_feed(self):
        feeddata=feedparser.parse()
        for item in feeddata.entries:
            id=self.get_id(item)
            if not self.get_item(id):
                self.add_item(id,item)
    def get_id(self,item):
        
    def get_item(self,id):
        raise NotImplementedError("Method not implemented")
    def get_feed_data(self):
        raise NotImplementedError("Method not implemented")
    def add_item(self):
        raise NotImplementedError("Method not implemented")
                
class FSporeFeedFetcher(FeedFetcher):
    def get_feed_data(self):
        StringIO.StringIO(urlfetch.fetch(self.feed).content)
        
    def get_item(self,id):


class FeedFetcherTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()