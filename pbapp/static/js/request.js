// Author: Jimi Bourgeois
// Date: 27-02-2020

$(document).ready(function() {


	// Initialize map
    function initMap(lat, lng) {
        let position  = {lat: lat, lng : lng};
        let map = $('.map').last().get(0);
        let goMap = new google.maps.Map(map, {scrollwheel: true, zoom: 12, center: position});
        let marker = new google.maps.Marker({position: position, map: goMap})

    }

    $("form").submit(function (event) {
        $('#spinner').fadeIn(2000).delay(4000).fadeOut();
        $('#response-research').delay(4000).fadeIn(2000);
        $('#response-research').append('<br>');
        $('#response-research').append('<div class="map" style="height: 400px;"></div>');
        $('#response-research').append('<br>');
        $('#response-research').append('<div class="wiki"></div>');
        $('#response-research').append('<br>');
        $('#response-research').append('<p class="lead">Voulez-vous faire une autre recherche ? </p>');
        var maps = $('.map').last();
        var wiki = $('.wiki').last();
        event.preventDefault();
        let query = $("input").val();
        $.ajax({
            data : {
                query : query
            },
            type : 'POST',
            url : '/ajax'
		}).done(function (response) {
		    maps.show();
		    initMap(parseFloat(response['lat']), parseFloat(response['lng']));
		    wiki.text(response['content']);

        })
    });
});