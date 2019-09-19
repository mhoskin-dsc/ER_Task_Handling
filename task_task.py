#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:22:39 2019

@author: training2
"""

import itertools

task_store = {}

class task():
  newid = itertools.count()
  hintid = itertools.count()
  
  def __init__(self, active = False, complete = False, 
               prereqs = [], postreqs = [], desc = '', hints = {}):
    self.id = next(task.newid)
    self.active = active
    self.complete = complete
    self.prereqs = prereqs
    self.postreqs = postreqs
    self.desc = desc
    self.hints = hints
      
  
  def activate(self):
    self.active = True
  
  def complete(self):
    self.complete = True
    
  def get_hint(self):
    print(self.hints[min(next(task.hintid), 
                         len(self.hints) -1)])
  
  
def create_task(active = False, complete = False, prereqs = [],
                postreqs = [], desc = '', hints = {}):

  t = task(active = active, complete = complete, prereqs = prereqs, 
           postreqs = postreqs, desc = desc, hints = hints)
  task_store[t.id] = t
  


  
create_task(active = True, desc = 'open the box!', hints = {0:'is there a box',
                                                                  1:'does it open',
                                                                  2:'i think it does',
                                                                  3:'open the box!'})
    
    