ACI Fault Analyzer (ALPHA)
==========================

Have you ever been troubleshooting a fault and been stuck wondering how it got there?
This tool is designed to make that process much easier. Gather some information from
your APIC, upload it to script, and the ACI Fault Analyzer will show you the relationship
between fabric faults and events. This makes it easier to see what events might have
caused which faults and can help you correct the issue faster.
 
Once you run the script, you're presented with a list of faults currently raised on your fabric.
Click on one of the faults and you're given a list of events that happened beforehand. You have
the option to set how far back from the fault you want to see, and we designed the script to sort
the event list based on relevance to the fault you're viewing.

<br>
##### Requires: #####

bottle 0.12.9 
(setup.py script coming soon)

audit logs and faults ( intructions on how to collect these below )
     
<br>  
##### Supports: #####

Cisco ACI - Only works for ACI
<br>   

#### Instructions: ####

on the CLI from one of your APIC's run the following two commands:

icurl "http://localhost:7777/api/class/faultInst.json" > faults.json

icurl "http://localhost:7777/api/class/aaaModLR.json" > events.json

using some type of file transfer grab both faults.json and events.json
and place them in the /static directory

The application  runs as a web based application and will run on TCP port
8082 and the loopback IP address  (127.0.0.1 or localhost) of the machine where it is running.
it can be excuted by type:

C:\Users\sheastma\PycharmProjects\test>python fault_bt_server.py 

and then going to the following address: http://127.0.0.1:8082/faults

*****THIS SCRIPT IS IN ALPHA AND WILL BE FULLY RELEASED SOON*********
