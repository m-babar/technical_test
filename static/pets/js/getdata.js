$(document).ready(function() {
	// console.log('getdata is loaded');


	let geturl = $("#get_url_link").attr('data-get_url');

	$.getJSON(geturl, function(data){
	  // console.log(data[0].owner);

	  var item = []

 	var len = data.length
	for(i=0; i<len; i++) {
	   $("#details").prepend( 
       "<li>" + data[i].pet_type + "</li> <li>" + data[i].name +  "</li> <li>" + data[i].birthday +  "</li> <li>" + data[i].owner + "</li>"
    	)
		}
	});
});
	  

