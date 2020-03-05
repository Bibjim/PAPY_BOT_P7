// Author: Jimi Bourgeois
// Date: 27-02-2020

// AJAX request to retrieve the user choice to process it with flask
$(document).ready(function() {
    $('form').on('submit', function(event) {
		$.ajax({
			data : {name : $('#nameInput').val()},
			type : 'POST',
			url : '/ajax'
		})
		event.preventDefault();
	});
})

// Google Maps init
var lat = 48.852969;
var lng = 2.349903;
var map = null;
// Card initialization function
function initMap() {
	map = new google.maps.Map(document.getElementById("map"), {
		center: new google.maps.LatLng(lat, lng),
		zoom: 11,
		mapTypeControl: true,
		scrollwheel: false,
		mapTypeControlOptions: {
			style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR
		},
		navigationControl: true,
		navigationControlOptions: {
			style: google.maps.NavigationControlStyle.ZOOM_PAN
		}
	});
	$.ajax({
	    data : results
	    type : 'GET'
		url : '/ajax',
	}).done(function(data){
			var marker = new google.maps.Marker({
				position: {lat: results.lat, lng: results.lng)},
				title: 'test',
				map: map
			});
		}
	});
}
