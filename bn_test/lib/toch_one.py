# -*- coding: utf-8 -*-
from airtest.core.api import touch,exists
class Touch_new(object):
    def toch_new(self,x):
        for i in range(3):
            self.x = x
            if exists(self.x):
                touch(self.x)
                break
    def toch_while(self, y):
        self.y =y
        while True:
            if exists(self.y):
                touch(self.y)
                break