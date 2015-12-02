__author__ = 'sheastma'
import bottle as bt
from bottle import route, run, template,static_file, response
import fault_analzer

@bt.route('/faults', method = 'GET')
def count_persons():
    f = open('test.html', 'r')
    return f.read()

@bt.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@bt.route('/heuristic/<time>/<time2>/<data:path>')
def heuristic(time,time2,data):
   events = fault_analzer.get_events()
   LTevents = fault_analzer.event_list(600,time, events)
   Cevents = fault_analzer.event_list(600,time2, events)
   all_events = LTevents+Cevents
   all_events = fault_analzer.heuristics(data, all_events)
   return template('events.tpl', all_events= all_events)

bt.run(host = 'localhost', port = 8080, debug = True)