#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty, ListProperty, NumericProperty

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
    color1 = ListProperty([1,1,1,1])
    color2 = ListProperty([0,1,0,1])
    fontsize1 = NumericProperty()


    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.fontsize1 = 50
        self.fontsize2 = 50
        self.text1 = 'Resetボタンを\n押してスタート'
        self.text2 = 'ここにはあなたが\n押した数が表示されます'
        self._answer = 0
        self.reset()
    
    def reset(self):
        self._reslist = []
        self._response = 0

    def buttonClicked11(self): #resetボタン
        self.fontsize1 = 140
        self.fontsize2 = 100
        self._answer = random.randint(3, 81)
        self.text1 = str(self._answer)
        self.reset()

    def buttonClicked0(self): #答え合わせボタン
        if len(self._reslist) == 0:
            pass
        elif self._reslist[0] == 1: #回答者が素数と答えた場合
            tmp = self.sosuHantei()
            if tmp == 1:
                self.text1 = '正解！'
            else:
                self.text1 = 'ぶっぶー！'
                self.reset()        
        else:                       #素数以外で答えた場合
            self._response = reduce(mul, self._reslist)
            if self._answer == self._response:
                self.text1 = '正解!'
            else:
                self.text1 = str(self._response) + ' ≠ ' + str(self._answer)
                self.reset()

    def sosuHantei(self):  #素数なら1を返す
        if (self._answer % 2) == 0:
            return 0        
        for i in range(3, int(self._answer/2), 2):
            if (self._answer % i == 0):
                return 0        
        return 1

    def buttonClicked1(self): #素数と答える
        self._reslist = []
        self._reslist.append(1)
        self.text2 = '素数' 

    def buttonClicked2(self):
        self._reslist.append(2)
        self.text2Hyouji()
        
    def buttonClicked3(self):
        self._reslist.append(3)
        self.text2Hyouji()

    def buttonClicked4(self):
        self._reslist.append(4)
        self.text2Hyouji()

    def buttonClicked5(self):
        self._reslist.append(5)
        self.text2Hyouji()

    def buttonClicked6(self):
        self._reslist.append(6)
        self.text2Hyouji()

    def buttonClicked7(self):
        self._reslist.append(7)
        self.text2Hyouji()

    def buttonClicked8(self):
        self._reslist.append(8)
        self.text2Hyouji()

    def buttonClicked9(self):
        self._reslist.append(9)
        self.text2Hyouji()       
    
    def text2Hyouji(self):
        temp1 = str(self._reslist[0])
        temp2 = ''
        for i in range(1, len(self._reslist)):
            temp2 += ( ' x ' + str(self._reslist[i]))
        self.text2 = temp1+temp2


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = '掛け算ゲーム'

if __name__ == '__main__':
    TestApp().run()
