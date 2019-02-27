#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty, ListProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

import random
from operator import mul
from functools import reduce

answer = 0
response = 0

# デフォルトに使用するフォントを変更する
resource_add_path('./fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class TextWidget(Widget):
    text1  = StringProperty()
    text2  = StringProperty()
    color = ListProperty([1,1,1,1])


    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text1 = 'Resetボタンを押してスタート'
        self.text2 = 'Response'
        self._answer = 0
        self._response = 0
        self._reslist = []

    def buttonClicked11(self):
        self._answer = random.randint(1, 81)
        self.text1 = str(self._answer)
        self._reslist = []
        self._response = 0

    def buttonClicked0(self):
        self._response = reduce(mul, self._reslist)
        if self._answer == self._response:
            self.text1 = '正解!'
        else:
            self._reslist=[]
            self._response=0
            if self._answer > self._response:
                self.text1 = 'ぶっぶー！\n正解はもっと大きいです'
            else:
                self.text1 = 'ぶっぶー！\nもっと小さいです'
        
    def buttonClicked1(self):
        self._reslist.append(1)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

    def buttonClicked2(self):
        self._reslist.append(2)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

    def buttonClicked3(self):
        self._reslist.append(3)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

    def buttonClicked4(self):
        self._reslist.append(4)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

    def buttonClicked5(self):
        self._reslist.append(5)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

    def buttonClicked6(self):
        self._reslist.append(6)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

    def buttonClicked7(self):
        self._reslist.append(7)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

    def buttonClicked8(self):
        self._reslist.append(8)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

    def buttonClicked9(self):
        self._reslist.append(9)
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = '九九探しゲーム'

if __name__ == '__main__':
    TestApp().run()
