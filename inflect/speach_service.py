# -*- coding: utf-8 -*-

import requests
import re
import time

def get_id(text = "atomelektrostacija"):
    r = ''
    url = 'http://runa.ailab.lv/AudioFileService/AudioFileService.asmx'
    data = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><CreateAudioRequest xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://tempuri.org/"><text>%s</text></CreateAudioRequest></s:Body></s:Envelope>'
    headers = {'soapaction': "http://tempuri.org/CreateAudioRequest", 'content-type': 'text/xml; charset=utf-8'}
    data = data % (text)

    r = requests.post(url, data.encode('utf-8'), headers=headers, timeout=10)
    if r == '':
        return None
    m = re.findall('<CreateAudioRequestResult>([^<]+)</CreateAudioRequestResult>', r.text)

    if(len(m)>0):
        return m[0]
    else:
        return None

def get_link(id):
    url = 'http://runa.ailab.lv/AudioFileService/AudioFileService.asmx'
    data = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body><CheckRequestStatus xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://tempuri.org/"><id>%s</id></CheckRequestStatus></s:Body></s:Envelope>'
    headers = {'soapaction': "http://tempuri.org/CheckRequestStatus", 'content-type': 'text/xml; charset=utf-8'}
    data = data % (id)

    r = requests.post(url, data.encode('utf-8'), headers=headers)
    m = re.findall('<CheckRequestStatusResult>([^<]+)</CheckRequestStatusResult>', r.text)

    if(len(m)>0):
        return m[0]
    else:
        return None

def return_link(link_id):
    a = 5
    while a > 0:
        audio=get_link(link_id)
        if(audio is not None):
            output = '<audio controls><source src="' + audio + '" type="audio/mpeg"></audio>'
            return output
        time.sleep(1)
        a = a - 1
    return "<p>Audio servis pašlaik nestrādā</p>"
