// Author: Jimi Bourgeois
// Date: 27-02-2020

// Google Maps init
var lat = 48.852969;
var lng = 2.349903;
var map = null;
// Card initialization function
function initMap(lat, lng) {
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