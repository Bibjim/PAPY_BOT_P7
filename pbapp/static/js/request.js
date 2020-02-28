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