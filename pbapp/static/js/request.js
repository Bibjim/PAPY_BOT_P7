// Author: Jimi Bourgeois
// Date: 27-02-2020
/*
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
		title: "Coucou j'ai trouvé votre recherche' !!!",
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
	    // spinner animation after the submit
	    $('#spinner').fadeIn(2000).delay(4000).fadeOut();
        // Mise en forme html
        //$('#show-resp').append('<div id="title-map" class="ombreouts">');
        //$('#title-map').append('<p class="lead">Hey !!! Votre recherche sur Google Maps ...</p>');
        $('#response-research').append('<div id="map"></div>').delay(5000).fadeIn();
        $('#response-research').append('<BR CLEAR="all">').delay(5000).fadeIn();
        //$('#show-resp').append('<div id="title-article">');
        //$('#title-article').append('<p class="lead">Et est-ce que vous saviez ? ...</p>');
        $('#response-research').append('<div id="wiki" class="lead"></div>').delay(5000).fadeIn();
        //$('#show-resp').append('<BR CLEAR="all">');

        var maps = $('.map').last();
        var wiki = $('.wiki').last();

	    var researchInput = $('#nameInput').val();
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
					    $('#wiki').delay(5000).fadeOut();
					}
					else {
					    var lat = response.coords[0];
					    var lng = response.coords[1];
					    // log
					    console.log(lat);
					    console.log(lng);
					    // log
					    initMap(lat, lng);
					    maps.show();
					    wiki.text(response.content);
					}
				});
			event.preventDefault();
	});
});
*/
$(document).ready(function() {



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
		title: "Coucou j'ai trouvé votre recherche' !!!",
		icon: icon
	    });
    }

    $("form").submit(function (event) {
        $('#spinner').fadeIn(2000).delay(4000).fadeOut();
        $('#response-research').append('<div id="map" class"container"></div>');
        $('#response-research').append('<div id="wiki" class="lead"></div>');
        var maps = $('.map').last();
        var wiki = $('.wiki').last();
        event.preventDefault();
        var researchInput = $('#nameInput').val();
        $.ajax({
				data: {
					name: researchInput,
				},
				type: 'POST',
				url: '/ajax'
		}).done(function (response) {
		    var lat = response.coords[0];
			var lng = response.coords[1];
			initMap(lat, lng);
            maps.show();
            wiki.text(response['content']);
        })
    });
});