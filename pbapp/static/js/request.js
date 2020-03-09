// Author: Jimi Bourgeois
// Date: 27-02-2020

// Initialize and add the map
function initMap() {
var initCoord = {'lat': 48.856614, 'lng': 2.3522219};
var map = new google.maps.Map(
    document.getElementById('map'), {
        zoom: 4,
        center: initCoord
     });
    var marker = new google.maps.Marker({
        position: myresult,
        map: map
    });
}

// AJAX request to retrieve the user choice to process it with flask
$(document).ready(function() {
	$('form').on('submit', function(event) {
		$.ajax({
			data : {
				name : $('#nameInput').val(),
			},
			type : 'POST',
			url : '/ajax'
		})
		.done(function(data) {
			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();

			}
			else {
			    $('#spin').fadeIn(1000);
			    $('#spin').fadeout(1000);
			    $('#map').show();
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}
		});
		event.preventDefault();
	});
});