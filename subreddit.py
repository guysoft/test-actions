import wx
import pkg_resources.py2_warn
import requests, json
import webbrowser
class AppWindow(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='/r/programming', size=(650, 400))
        self.panel = wx.Panel(self)
        self.Show()
if __name__ == '__main__':
    app = wx.App(False)
    window = AppWindow()
    app.MainLoop()
