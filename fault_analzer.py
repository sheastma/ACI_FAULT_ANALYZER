__author__ = 'sheastma'
import json
from difflib import SequenceMatcher

def get_events():
    with open('events.json') as data_file:
        data = json.load(data_file)
    events = []
    count = int(data["totalCount"])
        # self.log('Found ' + str(count) + ' total event records ...')
    for i in range(1, count, 1):
        temp = {"ratio": "","affected": "","cause":"","changeSet":"", "childAction":"","code":"","created":"","descr":"","dn":"","id":"","ind":"","modTs":"","severity":"","status":"","trig":"","txId":"","user":""}
        try:
            temp["ratio"] = ""
            temp["affected"] = data["imdata"][i]["aaaModLR"]["attributes"]["affected"]
            temp["cause"] = data["imdata"][i]["aaaModLR"]["attributes"]["cause"]
            temp["changeSet"] = data["imdata"][i]["aaaModLR"]["attributes"]["changeSet"]
            temp["childAction"] = data["imdata"][i]["aaaModLR"]["attributes"]["childAction"]
            temp["code"] = data["imdata"][i]["aaaModLR"]["attributes"]["code"]
            temp["created"] = data["imdata"][i]["aaaModLR"]["attributes"]["created"]
            temp["descr"] = data["imdata"][i]["aaaModLR"]["attributes"]["descr"]
            temp["dn"] = data["imdata"][i]["aaaModLR"]["attributes"]["dn"]
            temp["id"] = data["imdata"][i]["aaaModLR"]["attributes"]["id"]
            temp["ind"] = data["imdata"][i]["aaaModLR"]["attributes"]["ind"]
            temp["modTs"] = data["imdata"][i]["aaaModLR"]["attributes"]["modTs"]
            temp["severity"] = data["imdata"][i]["aaaModLR"]["attributes"]["severity"]
            temp["status"] = data["imdata"][i]["aaaModLR"]["attributes"]["status"]
            temp["trig"] = data["imdata"][i]["aaaModLR"]["attributes"]["trig"]
            temp["txId"] = data["imdata"][i]["aaaModLR"]["attributes"]["txId"]
            temp["user"] = data["imdata"][i]["aaaModLR"]["attributes"]["user"]
            #print temp
            events.append(temp)
        except:
            print 'The fault #'+str(i) +' failed. Please contact the authors of the script'
            continue
    return events

def event_list(history,time, events=[]):
    rev_events = []
    for event in events:
        ECyear = event["created"][0:4]
        ECmonth = event["created"][5:7]
        ECday = event["created"][8:10]
        EChour = event["created"][11:13]
        ECmin = event["created"][14:16]
        ECsecs = event["created"][17:19]
        #ETyear = event.lastTransition[0:4]
        #ETmonth = event.lastTransition[5:7]
        #ETday = event.lastTransition[8:10]
        #EThour = event.lastTransition[11:13]
        #ETmin = event.lastTransition[14:16]
        #ETsecs = event.lastTransition[17:19]
        syear = time[0:4]
        smonth = time[5:7]
        sday = time[8:10]
        shour = time[11:13]
        smin = time[14:16]
        #self.log(smin)
        ssecs = time[17:19]
        #self.log(ssecs)
        # Convert minutes to seconds for event and add leftover seconds
        Cevent_time = (int(ECmin) * 60) + int(ECsecs)
        #Tevent_time = (int(ETmin) * 60) + int(ETsecs)
        # Convert minutes to seconds for fault and add leftover seconds
        fault_time = (int(smin) * 60) + int(ssecs)

        # Assumes events fall within the previous hour?
        if ((ECyear == syear) and
            (ECmonth == smonth) and
            (ECday == sday) and
            (EChour == shour) and
            (Cevent_time <= fault_time) and
            (Cevent_time >= fault_time - int(history))):
                rev_events.append(event)


    return rev_events

def heuristics(dn, events=[]):
    for e in events:
        m = SequenceMatcher(None, e["affected"], dn)
        #m1 = SequenceMatcher(None, e.d, dn)
        e["ratio"] = m.ratio()
        #print e.affected + " " + dn
        #print e.ratio
        #print m
    return events

