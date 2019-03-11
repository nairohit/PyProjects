import wx #for dynamic gui
import wikipedia #search
import wolframalpha #search
from espeakng import ESpeakNG

#ESpeakNG.synth_wav("Welcome")
#espeak.synth("Welcome"

ESpeakNG.say("Hello")

class MyFrame(wx.Frame):  #GUI Building
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyAssistant")

        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am your Geanie. How may I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        #print("It worked")
        try:  # wolframalpha
            app_id = "<wolframalpha_app_ID>"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print(answer)
            #espeak.synth("The answer is "+answer)
            #ESpeakNG.synth_wav("The answer is "+answer)
            #esng.say(ESpeakNG, "The answer is"+answer)

        except:  # wikipedia
            '''input = input.split(' ')    #split input(WHO questions)
            input = " ".join(input[2:])'''
            #espeak.synth("Searched for"+input)
            #ESpeakNG.say("Searched for "+input)
            print(wikipedia.summary(input))

if __name__ == "__main__":
    app=wx.App(True)
    frame=MyFrame()
    app.MainLoop()
