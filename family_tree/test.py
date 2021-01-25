# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:54:00 2020

@author: Administrador
"""

import json
from json import JSONEncoder
from person import Person


p1 = Person("David")
p1.addParent("Juan")
p1.addChild("Michael")
p2 = Person("Laura")
p2.addParent("Ami")



d = {"David" : p1, "Laura" : p2}

print(json.dumps(d, cls=EmployeeEncoder))