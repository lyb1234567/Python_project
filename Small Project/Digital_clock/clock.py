import tkinter as tk
from tkinter import PhotoImage
import datetime
import time
import  sys
global docount
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.hours=0
        self.secs=0
        self.mins=0
        self.time_disp=time.strftime("%H")
        self.create_widgets()
        self.grid(row=4,column=6)
        self.docount=True
        self.dis=True
        self.disp()
    def create_widgets(self):
        self.label = tk.Label(self.master, font=("Courier", 100, 'bold'), bg="blue", fg="white", bd=100,padx=300)
        self.label.grid(row=10, column=3,padx=80,columnspan=10)
        # self.disp()
        self.hour_label_text = tk.StringVar()
        self.hour_label_text.set("hour")
        self.hour_label = tk.Label(self.master, textvariable=self.hour_label_text, height=5)
        self.hour_label.grid(row=3, column=3)
        self.hour_enter_text = tk.StringVar(None)
        self.hour_enter = tk.Entry(self.master, textvariable=self.hour_enter_text, width=20)
        self.hour_enter.bind('<Return>',self.assign_time)
        self.hour_enter.grid(row=3, column=4)
        self.mins_label_text = tk.StringVar()
        self.mins_label_text.set("minute")
        self.mins_label = tk.Label(self.master, textvariable=self.mins_label_text, height=5)
        self.mins_label.grid(row=3, column=5)
        self.mins_enter_text = tk.StringVar(None)
        self.mins_enter = tk.Entry(self.master, textvariable=self.mins_enter_text, width=20)
        self.mins_enter.grid(row=3, column=6)
        self.mins_enter.bind('<Return>',self.assign_time)
        self.secs_label_text = tk.StringVar()
        self.secs_label_text.set("second")
        self.secs_label = tk.Label(self.master, textvariable=self.secs_label_text, height=5)
        self.secs_label.grid(row=3, column=7)
        self.secs_enter_text = tk.StringVar(None)
        self.secs_enter = tk.Entry(self.master, textvariable=self.secs_enter_text, width=20)
        self.secs_enter.bind('<Return>',self.assign_time)
        self.secs_enter.grid(row=3, column=8)
        self.disp_time = tk.Button(self,text="Time",command=self.time,padx=50)
        self.disp_time.grid(row=4,column=5)
        self.countdown = tk.Button(self, padx=30,text="Countdown", command=lambda :self.assign_time())
        self.countdown.grid(row=4, column=6)
        self.stop_button=tk.Button(self,padx=30,text="Stop",command=self.stop)
        self.stop_button.grid(row=4, column=7)
        self.start=tk.Button(self,padx=30,text="Start",command=self.start)
        self.start.grid(row=4,column=8)
        self.up=tk.Button(self,padx=30,text="Up",command=self.up_count)
        self.up.grid(row=4,column=9)
        self.down = tk.Button(self, padx=30, text="down", command=self.down_count)
        self.down.grid(row=4, column=10)

    # 启动倒计时
    def assign_time(self):
        self.hours=int(self.hour_enter.get()) if self.hour_enter.get() else self.hours
        self.mins=int(self.mins_enter.get()) if self.mins_enter.get() else self.mins
        self.secs=int(self.secs_enter.get()) if self.secs_enter.get() else self.secs
        self.count()
    # 显示正常时间
    def disp(self):
            if self.dis==True:
                if int(self.time_disp)<12:
                    text_input = time.strftime("%Y-%m-%d\n%H:%M:%S am")
                    self.label.config(text=text_input)
                    self.time_disp=time.strftime("%H")
                    self.after_id_time=self.after(1000, self.disp)
                else:
                    text_input = time.strftime("%Y-%m-%d\n%H:%M:%S pm")
                    self.label.config(text=text_input)
                    self.time_disp = time.strftime("%H")
                    self.after_id_time = self.after(1000, self.disp)
            else:
                return
    def time(self):
        self.after_cancel(self.after_id_count)
        self.dis=True
        self.disp()
    def stop(self):
        self.docount=False
    def start(self):
        self.docount=True
        self.count()

    def up_count(self):
        self.after_cancel(self.after_id_time)
        self.secs=self.secs+1
        if self.secs>=60:
            self.mins=self.mins+1
            self.secs=0
        if self.mins>=60:
            self.hours=self.hours+1
            self.mins=0
        timer = '{:02d}:{:02d}:{:02d}'.format(self.hours, self.mins, self.secs)
        self.label.config(text=timer)
    def down_count(self):
        self.after_cancel(self.after_id_time)
        if (self.mins==0 and self.hours==0 and self.secs==0):
            timer = '{:02d}:{:02d}:{:02d}'.format(self.hours, self.mins, self.secs)
            self.label.config(text=timer)
        if (self.hours==0 and self.mins==0 and self.secs>0):
            self.secs = self.secs - 1
            timer = '{:02d}:{:02d}:{:02d}'.format(self.hours, self.mins, self.secs)
            self.label.config(text=timer)

        if (self.hours==0 and self.mins>0 and self.secs>=0):
            self.secs = self.secs - 1
            if self.secs==0:
                self.mins=self.mins-1
                self.secs=59
            timer = '{:02d}:{:02d}:{:02d}'.format(self.hours, self.mins, self.secs)
            self.label.config(text=timer)

        if (self.hours>0 and self.mins>=0 and self.secs>=0):
            self.secs = self.secs - 1
            if self.secs==0:
                self.mins=self.mins-1
                self.secs=59
            if self.mins==0:
                self.hours=self.hours-1
                self.mins=59
            timer = '{:02d}:{:02d}:{:02d}'.format(self.hours, self.mins, self.secs)
            self.label.config(text=timer)
        timer = '{:02d}:{:02d}:{:02d}'.format(self.hours, self.mins, self.secs)
        self.label.config(text=timer)
    def confirm_count(self):
        self.docount=True
        self.count()
    def count(self,hours=None,mins=None,secs=None):
                self.after_cancel(self.after_id_time)
                if self.docount:
                    if (self.hours == 0 and self.secs == 0 and self.mins == 0):
                        self.docount = False
                        timer = '{:02d}:{:02d}:{:02d}'.format(self.hours, self.mins, self.secs)
                        self.label.config(text=timer)
                    self.secs = self.hours * 3600 + self.mins * 60 + self.secs
                    self.hours = self.secs // 3600
                    self.mins = (self.secs // 60) % 60
                    self.secs = self.secs % 60
                    timer = '{:02d}:{:02d}:{:02d}'.format(self.hours, self.mins, self.secs)
                    time.sleep(1)
                    self.secs = self.secs - 1
                    self.label.config(text=timer)
                    self.after_id_count=self.after(200,self.count)
                else:
                    return


    def play(self):
        pass

root = tk.Tk()
root.title("Digital Clock")
app = Application(master=root)
app.mainloop()
