#!/usr/bin/env python3
from hermes_python.hermes import Hermes
import hermes_python 
import requests
from xml.etree import ElementTree as ET

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 

a = datetime.now()
f = a.date()
defaultfecha = str(f)

def intent_received(hermes, intentMessage):

    if intentMessage.intent.intent_name == 'gemalb:GetNews':
        url = "http://www.ara.cat/rss/politica/"
        response = requests.get(url)
        xml = response.text
        root = ET.fromstring(xml)
        counter = 0
        for news in root.iter('item'):
            headline = news.find('title')
            if headline.text:
                counter=counter+1
                print("Titular {}.")dirv = headline.text
   
        sentence = 'Encontrados ' + counter + ' titulares'

    else:
        return
    
    hermes.publish_end_session(intentMessage.session_id, sentence)
    
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
