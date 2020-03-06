// Author: Jimi Bourgeois
// Date: 27-02-2020

// Initialize and add the map
function initMap() {
var myresult = {'lat': 48.856614, 'lng': 2.3522219};
var map = new google.maps.Map(
    document.getElementById('map'), {zoom: 11, center: myresult});
    var marker = new google.maps.Marker({position: myresult, map: map});
}

$(document).ready(function(){
    $("button").click(function(){
        $('p[class="dialogue"]:last').append('<img src="https://cdn.dribbble.com/users/63485/screenshots/4388983/liquid-preloader_dribbble_v2.gif" class="chargement">');
        $.ajax({
            url : '/ajax',
            type : 'POST',
            data : {name : $('#nameInput').val()},
            success : function(resp){
                $('img[class="chargement"]').remove();
                if (resp['histoire'] != 'vide') {
                    $('p[class="dialogue"]:last').append('<p class="dialogue">' + resp['histoire'] + '</p>');
                }
                else {
                    $('p[class="dialogue"]:last').append('<p class="dialogue">Ma mémoire doit me jouer des tours, attends...</p>');
                }
                if (resp['adresse'] != 'vide') {
                    $('p[class="dialogue"]:last').append('<p class="dialogue">Ce lieu est situé ' + resp['adresse'] + '</p>');
                    $('p[class="dialogue"]:last').append('<p class="dialogue"><iframe src=' + resp['url_carte'] + '></iframe></p>');
                }
                else {
                    $('p[class="dialogue"]:last').append('<p class="dialogue">J\'ai beau réfléchir...</p>');
                }

                $('p[class="dialogue"]:last').append('<p class="dialogue">Une autre question mon enfant ?</p>');
                $('p[class="dialogue"]:last').append('<br />');
            }

        });

    });

});