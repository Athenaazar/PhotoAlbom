function createMap(lat, lon) {
    mymap = L.map('mapid', {
        center: [parseFloat(lat), parseFloat(lon)],
        zoom: 12
    });
    var mymarker = L.marker([parseFloat(lat), parseFloat(lon)]).addTo(mymap);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoiYXRoZW5hYXphciIsImEiOiJja3hmOGszb2g1YWlhMndsYXAxM3VzanMwIn0.TNTYhUG1sUDejMGylvzhgw'
    }).addTo(mymap);

    mymap.setView([parseFloat(lat), parseFloat(lon)], 15);
}

function picture_location_btn(e) {
    let picture_uuid = $(e).data('picture_uuid')
    let csrf = $('input[name=csrfmiddlewaretoken]').val();
    $('#pictureLocationModalID .modal-dialog').html('');
    $.ajax({
        type: 'POST',
        url: '/picture/picture-details/',
        data: {
            'picture_uuid': picture_uuid,
            csrfmiddlewaretoken: csrf
        },
        success: function (data) {
            $('#pictureLocationModalID .modal-dialog').html($('#pictureLocationModalID .modal-dialog', data));
            $('#pictureLocationModalID').modal('show');

            const picture_lat = $('#pictureLat', data).val();
            const picture_lon = $('#pictureLon', data).val();

            setTimeout(() => {
                createMap(picture_lat, picture_lon)
            }, 1000)
        },
        error: function () {
            let message_text = "some error occurred!"
            showAlert(message_text, "error")
        },
    });
}

