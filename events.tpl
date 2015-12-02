<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script type="text/javascript"></script>
<script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
<link rel="stylesheet" type="text/css" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
<script src="//cdn.datatables.net/1.10.10/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" type="text/css" href="//cdn.datatables.net/1.10.10/css/jquery.dataTables.min.css">
<body style = "background-color:#CCCCCA">
<table id="table6" class = "display" cellspacing="0" width="50%">
  <thead>
    <tr>
	  <th>match ratio</th>
	  <th>affected</th>
	  <th>cause</th>
      <th>changeSet</th>
	  <th>childAction</th>
      <th>code</th>
	  <th>created</th>
      <th>descr</th>
      <th>dn</th>
	  <th>id</th>
      <th>ind</th>
	  <th>modTs</th>
      <th>severity</th>
	  <th>status</th>
      <th>trig</th>
	  <th>txId</th>
      <th>user</th>
    </tr>
   </thead>
	<tfoot>
	<tr>
	  <th>match ratio</th>
	  <th>affected</th>
	  <th>cause</th>
      <th>changeSet</th>
	  <th>childAction</th>
      <th>code</th>
	  <th>created</th>
      <th>descr</th>
      <th>dn</th>
	  <th>id</th>
      <th>ind</th>
	  <th>modTs</th>
      <th>severity</th>
	  <th>status</th>
      <th>trig</th>
	  <th>txId</th>
      <th>user</th>
    </tr>
	</tfoot>
	<tbody>
%for event in all_events:
	<tr role="row"> 
	<td class="sorting_1">{{event["ratio"]}}</td>
	<td>{{event["affected"]}}</td>
	<td>{{event["cause"]}}</td>
	<td>{{event["changeSet"]}}</td>
	<td>{{event["childAction"]}}</td>
	<td>{{event["code"]}}</td>
	<td>{{event["created"]}}</td>
	<td>{{event["descr"]}}</td>
	<td>{{event["dn"]}}</td>
	<td>{{event["id"]}}</td>
	<td>{{event["ind"]}}</td>
	<td>{{event["modTs"]}}</td>
	<td>{{event["severity"]}}</td>
	<td>{{event["status"]}}</td>
	<td>{{event["trig"]}}</td>
	<td>{{event["txId"]}}</td>
	<td>{{event["user"]}}</td>
	</tr>
%end
</table>
<script src="/static/events.js"></script>
