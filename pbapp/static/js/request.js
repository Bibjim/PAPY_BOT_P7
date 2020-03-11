// Author: Jimi Bourgeois
// Date: 27-02-2020

// Initialize and add the map
function initMap(lat, lng) {
    if (lat === undefined || lng === undefined) {
        lat = 0;
        lng = 0;

    } else {
        var myLatLng = {lat: lat, lng: lng};
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 11,
            center: myLatLng
        });

        var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        });
    }
}

// Display for return values research user
function displayResult(response) {
    var lat = response.coords[0];
    var lng = response.coords[1];
    console.log(lat);
    console.log(lng);

    var results = $('#results');
    results.attr("wiki-thumbnail", response.thumbnail);
    results.attr("gmaps-coords", `${lat} ${lng}`);

    $('#wiki-article').text(response.content);

    initMap(lat, lng);
}

// AJAX request to retrieve the user choice to process it with flask
$(document).ready(function(displayResult, initMap) {
	$('form').on('submit', function(event) {
	    var researchInput = $('#nameInput').val();
	    $('#spinner').fadeIn().delay(4000).fadeOut();
		$.ajax({
			data : {
				name : $('#nameInput').val(),
			},
			type : 'POST',
			url : '/ajax'
		})
		.done(function(data, response) {
			if (data.error) {
				$('#errorAlert').fadeIn();
				$('#map').hide();
				$('#results').hide();
				$('#wiki-article').text(response.content).hide()

			}
			else {
			    $('#map').show();
			    $('#wiki-article').text(response.content).show();
			    $('#results').show();
				$('#errorAlert').hide();
			}
		});
		event.preventDefault();
	});
});