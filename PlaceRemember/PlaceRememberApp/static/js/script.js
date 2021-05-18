function updateCoordinates(lat, lng) {
    document.getElementById('id_lat').value = lat;
    document.getElementById('id_lng').value = lng;
}

initMap = function() {
    var map, marker;

    var myLatlng = {
      lat: 55.74,
      lng: 37.63
    };

    if (String(document.getElementById('id_lat').value).length == 0){
      document.getElementById('id_lat').value = myLatlng.lat;
      document.getElementById('id_lng').value = myLatlng.lng;
    }

    else{
      myLatlng.lat = parseFloat(String(document.getElementById('id_lat').value).replace(',','.'));
      myLatlng.lng = parseFloat(String(document.getElementById('id_lng').value).replace(',','.'));
    }

    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: myLatlng
    });

    google.maps.event.addListener(map, 'click', function(event) {
      placeMarker(event.latLng);
    });
  
    function placeMarker(location) {
        if(marker){
            marker.setPosition(location);
        }else{
            marker = new google.maps.Marker({
                position: location, 
                map: map,
                draggable: true
            });
        }
        document.getElementById('id_lat').value=location.lat();
        document.getElementById('id_lng').value=location.lng();
    }
  
    marker.addListener('dragend', function() {
      var position = marker.getPosition();
      updateCoordinates(position.lat(), position.lng())
    });
   
    map.panTo(myLatlng);
}