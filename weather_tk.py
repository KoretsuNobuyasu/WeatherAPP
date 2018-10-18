#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#__author__ == nobu
#__date__ == 2018/10/16
#__version__ == 1.0.0

# import
import tkinter as tk
import json, requests, sys



# class
class Application(tk.Frame):
    """ウィンドウ内の情報"""

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there()
        self.osaka()
        self.quit()

    def osaka(self):
        self.osaka = tk.Button(self)
        self.osaka["text"] = "大阪"
        self.osaka["command"] = self.osaka_weather
        self.osaka.pack()

    def hi_there(self):
        self.hi_there = tk.Label(self)
        self.hi_there["text"] = "Please Choose A City Name\n都市名を選んでください"
        self.hi_there.pack(side="top")

    def quit(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.pack(side="bottom")

    def osaka_weather(self):
        self.location = "Osaka, JP"
        self.setting_location()

    def setting_location(self):
        # openweathermap.org 　JSON DATA Download from API
        self.url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&cnt=3&appid={}'.format(self.location, APPID)
        self.get_info()
        self.weather_data = self.loading()

    def get_info(self):
        self.response = requests.get(self.url)
        print(self.response)
        self.response.raise_for_status()

    def loading(self):
        # JSON Data to Python variable
        self.weather_data = json.loads(self.response.text)
        self.show()

    def show(self):
        w = self.weather_data['list']
        print('{}の現在の天気'.format(self.location))
        print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'], '\n')
        print('明日:')
        print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'], '\n')
        print('明後日:')
        print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])


root = tk.Tk()
root.geometry("500x500")
APPID='a584bd2a6688a2c48c50b3775c6d691b'
def main():

    app = Application(master=root)
    app.mainloop()
    return 0


if __name__ == '__main__':
    main()