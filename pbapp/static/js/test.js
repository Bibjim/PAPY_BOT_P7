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
    window.onload = function(){
	// Fonction d'initialisation qui s'exécute lorsque le DOM est chargé
	initMap();
    }

    $("form").submit(function (event) {
        $('#spinner').fadeIn(2000).delay(4000).fadeOut();
        $('#response-research').append('<div id="map"></div>');

        $('#response-research').append('<div id="wiki" class="lead"></div>').delay(6000).fadeIn();
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
