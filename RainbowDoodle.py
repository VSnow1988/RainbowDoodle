from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from random import random


class RainbowDoodleWidget(Widget):

	
	def on_touch_down(self, touch):
		with self.canvas:
			randcolor = (random(),random(),random())
			Color(*randcolor)
			d = 20.
			Ellipse(segments=180,pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=d/2)
			
	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]

class RainbowDoodleApp(App):

	def build(self):
		parent = Widget()
		self.painter = RainbowDoodleWidget()
		clearbtn = Button(text='Clear Canvas', size=(100,50), pos=(0,0))
		clearbtn.bind(on_release=self.clear_canvas)
		parent.add_widget(self.painter)
		parent.add_widget(clearbtn)
		return parent
		
	def clear_canvas(self, obj):
		self.painter.canvas.clear()
	def setcolor_purple(self, obj):
		self.painter.color = (0.5,0,0.5)
	def setcolor_random(self, obj):
		self.painter.color = (random(),random(),random())
	def setcolor_random(self, obj):
		self.color
		

if __name__ == '__main__':
    RainbowDoodleApp().run()