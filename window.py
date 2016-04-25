# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import Tkinter
import os
from subprocess import Popen, PIPE
from tkMessageBox import showinfo, showwarning, showerror


class TkSpriderUI:
    """ A Scrapy Client Interface, developed by Tkinter library"""

    def __init__(self):
        self.process = None
        self.spiderstatus = 0

        # Tkinter Set
        # root window
        self.top = Tkinter.Tk()
        self.top.title('Wfrobot GUI')
        self.top.geometry('500x500')

        self.keywordvalue = Tkinter.StringVar(self.top)
        self.statevalue = Tkinter.StringVar(self.top)

        self.keywordframe = Tkinter.Frame(self.top)

        self.keywordbox = Tkinter.Entry(self.keywordframe, width=100, textvariable=self.keywordvalue)

        self.log = Tkinter.StringVar(self.top)
        self.log.set('GUI Start!')
        self.logwindow = Tkinter.Text(self.top, width=200, bg='white')
        self.buttonframe = Tkinter.Frame(self.top)
        self.submitbutton = Tkinter.Button(self.buttonframe, text='Start', command=self.startSpider)
        self.stopbutton = Tkinter.Button(self.buttonframe, text='Pause', command=self.stopSpider)

        self.logwindow.pack(fill=Tkinter.Y, expand=0)
        self.keywordframe.pack(fill=Tkinter.Y, expand=1)
        self.keywordbox.pack(fill=Tkinter.Y, expand=1)
        self.submitbutton.pack(side=Tkinter.LEFT)
        self.stopbutton.pack(side=Tkinter.LEFT)
        self.buttonframe.pack(fill=Tkinter.Y, expand=2)
        self.logwindow['state'] = 'disabled'


    def startSpider(self):
        if self.spiderstatus == 0 :
            keyword = self.keywordvalue.get()

            sprider = u'python D:\Python27\Lib\site-packages\scrapy\cmdline.py crawl wfrobot -a keyword=%s -s JOBDIR=crawls/wfrobot-1' % keyword
            # result = os.system(b1cmd)
            self.process = Popen(sprider, stdout=PIPE, stderr=PIPE)
            self.spiderstatus = 1
            self.submitbutton.configure(text="Pause")

            #while process.returncode is None:
            #    self.logwindow.insert(Tkinter.END, process.stdout.readline())
            returncode = self.process.poll()
            while returncode is None:
                msg = self.process.stderr.readline()
                returncode = self.process.poll()
                msg = msg.strip() + "\n"
                self.logwindow['state'] = 'normal'
                self.logwindow.insert(Tkinter.END, msg)
                self.logwindow['state'] = 'disabled'
            self.logwindow.insert(Tkinter.END, returncode)
            self.spiderstatus = 0
            self.submitbutton.configure(text='Start')
            return
        if self.spiderstatus == 1:
            self.process.terminate()
            self.spiderstatus = 0
            return
        if self.spiderstatus == 2:
            self.process.terminate()

    def stopSpider(self):
        # if self.
        self.process.terminate()
        self.spiderstatus = 0

        pass


def main():
    obj = TkSpriderUI()
    Tkinter.mainloop()


if __name__ == '__main__':
    main()
