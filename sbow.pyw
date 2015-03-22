#!/usr/bin/python
print("start")
import urllib
import os
import io
import wx

class ButtonFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'My Python App',size=(920, 400))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, "z.btbu.pw",(20,20))
        self.button.Size=wx.Size(200,100)
        self.button.SetDefault()
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        
        self.button2 = wx.Button(panel, -1, "jwgl",(220+20,20))
        self.button2.Size=wx.Size(200,100)
        self.button2.SetDefault()
        self.Bind(wx.EVT_BUTTON, self.OnClick2, self.button2)
        
        self.label=wx.StaticText (panel,-1,"message",(20,140))
        self.label.Size=wx.Size(920,100)

        try:
            image = wx.Image('out.jpg', wx.BITMAP_TYPE_JPEG)
            temp = image.ConvertToBitmap()
            size = temp.GetWidth(), temp.GetHeight()
            self.bmp = wx.StaticBitmap(panel,-1,temp,pos=(500, 20),size=size)
        except:
            print("error")
        

    def OnClick(self, event):
        print("start reading")
        conn = urllib.urlopen("http://z.btbu.pw")
        r=conn.read()
        r=r.decode("gbk")
        print("finished")
        print(r)
        print(type(r))
        self.label.SetLabel(r)

    def OnClick2(self, event):
        print("start reading")
        conn = urllib.urlopen("http://jwgl.btbu.edu.cn/verifycode.servlet")
        r=conn.read()
        f = output = open('out.jpg', 'wb')
        f.write(r)
        f.close()
        print("finished")
        image = wx.Image('out.jpg', wx.BITMAP_TYPE_JPEG)
        temp = image.ConvertToBitmap()
        self.bmp.SetBitmap(temp)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()
