/* Requete pour récupérer la donnée de localisation*/
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
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
/*
$(document).ready(function() {

        var myLatlng = new google.maps.LatLng(49.47143, 11.107489999999984);
        var mapOptions = {
            zoom: 8,
            center: myLatlng
        };
        var map = new google.maps.Map(document.getElementById('map'), mapOptions);
        var marker;

        $.ajax({
            type: 'GET',
            url: '/ajax',
            data: {
				lat : $('#lat').val(),
				lat : $('#lng').val(),
			},
            success: function(data) {
                    marker = new google.maps.Marker({
                    position: new google.maps.LatLng(data.lat, data.long),
                    map: map,
                    title: 'test'
                });
            }
        });
});*/