#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#__author__ == nobu
#__date__ == 2018/10/08
#__version__ == 1.0.0

# import
import json, requests, sys


EXIT_SUCCESS = 0
EXIT_FAILURE = 1
#openweathermap.org API key
APPID='a584bd2a6688a2c48c50b3775c6d691b'

def main():

    if len(sys.argv) < 2:
        print('Usage: weather.py location')
        print('場所を入力してください')
        sys.exit()
    location = ' '.join(sys.argv[1:])
    # openweathermap.org 　JSON DATA Download from API
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&cnt=3&appid={}'.format(location, APPID)
    data = loading(location, get_info(url))

    # it show weather info about select location
    w = data['list']
    print('{}の現在の天気'.format(location))
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('明日:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('明後日:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

    return  EXIT_SUCCESS


def get_info(url):
    response = requests.get(url)
    response.raise_for_status()
    return response

def loading(location, response):
    #JSON Data to Python variable
    weather_data = json.loads(response.text)
    return weather_data





if __name__ == '__main__':

    main()