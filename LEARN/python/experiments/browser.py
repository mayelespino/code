#!/usr/bin/python
import sys
import wx
import wx.webkit        

theApp = wx.PySimpleApp(0)
theFrame = wx.Frame(None, -1, "", size=(640,480))
w = wx.webkit.WebKitCtrl(theFrame, -1)
w.LoadURL(sys.argv[1])
theFrame.Show()
theApp.MainLoop()
