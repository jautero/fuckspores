#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Copyright 2008 Juha Autero
#
# Copyright 2010 Juha Autero <jautero@iki.fi>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

project="Fuckspores"
version="1.0"
author="Juha Autero <jautero@iki.fi>"
copyright="Copyright &copy; 2010 Juha Autero <jautero@iki.fi>"
application="fuckspores"
import random
greeting=random.choice(["Good morning, fuckspores","Good morning, fuckoids","Good morning, sexbuckets"])
import wsgiref.handlers
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp

import markdown

class MainPage(webapp.RequestHandler):

  def get(self):
    template_values=globals()
    path = os.path.join(os.path.dirname(__file__), 'index.md')
    
    self.response.out.write(markdown.markdown(template.render(path, template_values)))

class FucksporePage(webapp.RequestHandler):
    def get(self):
        template_values=globals()
        key=self.request.get("key",None)
        if not key:
          key=os.path.basename(self.request.path)
        mode=self.request.get("mode","view")
        if not key:
            mode="edit"
            template_values["url"]=""
            template_values["name"]=""
            template_values["image"]=""
            template_values["feeds"]=[]
        else:
            pass
        if mode=="edit":
            template_values["edit"]=True
        
            
def main():
  application = webapp.WSGIApplication([('/', MainPage),('/fuckspore',FucksporePage)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
