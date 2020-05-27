// Author: Jimi Bourgeois
// Date: 27-02-2020

// Initialize and add the map
function initMap(lat, lng) {
	map = new google.maps.Map(document.getElementById("map"), {
		center: new google.maps.LatLng(lat, lng),
		zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
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
	var icon = {
        url: '../static/img/gmap_marker.png', // url
        scaledSize: new google.maps.Size(70, 70), // size
    };
	var marker = new google.maps.Marker({
		position: {lat: lat, lng: lng},
		map: map,
		title: "Coucou je suis là où vous me l'avez demandé !!!",
		icon: icon
	});
}
window.onload = function(){
	// Fonction d'initialisation qui s'exécute lorsque le DOM est chargé
	initMap();
};

// AJAX request to retrieve the user choice to process it with flask
$(document).ready(function() {
	$('form').on('submit', function(event) {
	    var researchInput = $('#nameInput').val();
	    $('#response-none').fadeOut()
	    $('#main-title').fadeOut();
	    $('#spinner').fadeIn(2000).delay(4000).fadeOut();
			$.ajax({
				data: {
					name: researchInput,
				},
				type: 'POST',
				url: '/ajax'
			})
				.done(function(response) {
				    // log
				    console.log(response);
				    // log
				    if (response.error) {
					    $('#response-none').delay(5000).fadeIn(2000);
					    $('#response-research').delay(5000).fadeOut();
					    $('#wiki-article').delay(5000).fadeOut();
					}
					else {
					    var lat = response.coords[0];
					    var lng = response.coords[1];
					    // log
					    console.log(lat);
					    console.log(lng);
					    // log
					    initMap(lat, lng);
					    $('#response-research').delay(5000).fadeIn(2000);
					    $('#wiki-article').text(response.content).delay(5000).fadeIn(2000);
					}
				});
			event.preventDefault();
	});
});