#!/usr/bin/python
import wx
class Example(wx.Frame):
	def __init__(self, parent, title):
		super(Example, self).__init__(parent, title=title, size=(260,180))
		self.InitUI()
		self.Centre()
		self.Show()

	def InitUI(self):
		panel = wx.Panel(self,pos=(0, 30), size=(20,20))
		#panel.SetBackGroundColour('#4f5049')
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		midPan = wx.Panel(self, pos=(30, 70), size=(20,20))

		#midPan.SetBackGroundColour('red')

		vbox.Add(midPan, 1, wx.EXPAND | wx.LEFT, 20)
		panel.SetSizer(vbox)

if __name__ == '__main__':
	app = wx.App()
	Example(None, title='Border')
	app.MainLoop()
