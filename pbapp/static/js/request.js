// Author: Jimi Bourgeois
// Date: 27-02-2020

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
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}
		});
		event.preventDefault();
	});
});