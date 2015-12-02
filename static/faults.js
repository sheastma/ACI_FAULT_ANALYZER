$(document).ready(function(){

    $.getJSON('/static/faults.json', function (data) {

            
		var test = $('#table5').DataTable({
			columnDefs : [
				{ targets : [0],
					render : function(data) {
					data = data.split(",")
					alert(data[0]);
					return '<a href="/heuristic/'+data[0]+'/'+data[1]+'/'+data[2]+'">Click here</a>'
					} 
				},
				{ targets : [1],
					render : function(data) {
					return '<a href="http://mishield-bld.insieme.local/documentation/html/FAULT-'+data+'.html" target_blank>'+data+'</a>'
					} 
				}
			]
		});

            var tr;
            for (var i = 0; i < data["totalCount"]; i++) {
              test.row.add([
				  data['imdata'][i]['faultInst']["attributes"]["lastTransition"]+","+
				  data['imdata'][i]['faultInst']["attributes"]["created"]+","+
				  data['imdata'][i]['faultInst']["attributes"]["dn"],
                  data['imdata'][i]['faultInst']["attributes"]["code"],
                  data['imdata'][i]['faultInst']["attributes"]["cause"],
                  data['imdata'][i]['faultInst']["attributes"]["descr"],
                  data['imdata'][i]['faultInst']["attributes"]["created"],
                  data['imdata'][i]['faultInst']["attributes"]["changeSet"],
                  data['imdata'][i]['faultInst']["attributes"]["childAction"],
                  data['imdata'][i]['faultInst']["attributes"]["dn"],
                  data['imdata'][i]['faultInst']["attributes"]["domain"],
                  data['imdata'][i]['faultInst']["attributes"]["highestSeverity"],
                  data['imdata'][i]['faultInst']["attributes"]["lastTransition"],
                  data['imdata'][i]['faultInst']["attributes"]["lc"],
                  data['imdata'][i]['faultInst']["attributes"]["occur"],
                  data['imdata'][i]['faultInst']["attributes"]["origSeverity"],
                  data['imdata'][i]['faultInst']["attributes"]["prevSeverity"],
                  data['imdata'][i]['faultInst']["attributes"]["rule"],
                  data['imdata'][i]['faultInst']["attributes"]["severity"],
                  data['imdata'][i]['faultInst']["attributes"]["subject"],
                  data['imdata'][i]['faultInst']["attributes"]["type"],
                  data['imdata'][i]['faultInst']['attributes']["ack"]
      
   
              ])
            }

            test.draw();
        });
    });