document.addEventListener('DOMContentLoaded', function () {

    mymap = L.map('mapid', {
        center: [57.70579538475589, 11.967961279294064],
        zoom: 12,
    });
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 20,
        id: 'mapbox/streets-v11',
        name: "picture_location",
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoiYXRoZW5hYXphciIsImEiOiJja3hmOGszb2g1YWlhMndsYXAxM3VzanMwIn0.TNTYhUG1sUDejMGylvzhgw'
    }).addTo(mymap)

    mymap.on('click', function (args) {
        selectLocationOnMap(args.latlng)


    })
});

function selectLocationOnMap(latlng) {

    mymap.eachLayer(function (layer) {
        if (layer.options.layer_type === "picture_marker_layer") {
            mymap.removeLayer(layer);
        }
    });

    addMarker(latlng)

    let latitude_holder_input = document.getElementById("pic_location_latitude")
    latitude_holder_input.value = latlng.lat
    let longitude_holder_input = document.getElementById("pic_location_longitude")
    longitude_holder_input.value = latlng.lng


}

function addMarker(latlng) {
    // Add marker to map at click location; add popup window
    var newMarker = new L.marker(latlng, {layer_type: "picture_marker_layer"}).addTo(mymap);
}


function pictureUpload() {
    let picture_upload_status = document.getElementById('noPicSpan');
    picture_upload_status.innerHTML = "uploaded";
    picture_upload_status.style.color = "green";
}


function addNewPictureSubmit(e) {
    e.preventDefault();
    let result1 = check_selected_picture()
    let result2 = check_selected_location()
    let result3 = check_selected_category()
    let result4 = check_picture_title()
    if (result1 && result2 && result3 && result4) {
        $('#addNewPictureFormId').submit();
    }
}


function check_selected_picture() {
    let image_input = document.getElementById("select_picture");
    if (image_input.value === "") {
        (function () {
            $(image_input).parent().parent().find('span').last().html("no picture selected!");
        })();
        return false
    } else if ((image_input.files[0].size) / 1024 > 10 * 1024) {
        (function () {
            $(image_input).parent().parent().find('span').last().html("maximum picture size is 10 mb .")
        })();
        return false;
    } else {
        (function () {
            $(image_input).parent().parent().find('span').last().html("")
        })();
        return true;
    }
}

function check_selected_location() {
    let latitude_input = document.getElementById("pic_location_latitude")
    let longitude_input = document.getElementById("pic_location_longitude")
    let location_err_span = document.getElementById("select_location_err")
    if (latitude_input.value === "" || longitude_input.value === "") {
        location_err_span.innerHTML = "select location of picture."
        return false
    } else {
        location_err_span.innerHTML = ""
        return true
    }
}


function check_selected_category() {
    let j = true;
    let category_selection_element = document.getElementById("category_selection");
    if (category_selection_element.value === "") {
        (function () {
            $(category_selection_element).next("span").html("choose a category.")
        })();
        j = false;
    } else {
        (function () {
            $(category_selection_element).next("span").html("")
        })();
    }
    return j;
}

function check_picture_title() {
    let element = document.getElementById("picture_title")
    let j = true;
    if (element.value === "") {
        (function () {
            $(element).next("span").html("enter picture title!")
        })();
        j = false;
    } else {
        (function () {
            $(element).next("span").html("")
        })();
        j = true;
    }
    return j;
}
