function updateCoordinates(lat, lng) {
    document.getElementById('id_lat').value = lat;
    document.getElementById('id_lng').value = lng;
}

function initMap() {
    var map, marker, geocoder;
    var myLatlng = {
      lat: 55.74,
      lng: 37.63
    };
    document.getElementById('id_lat').value = myLatlng.lat;
    document.getElementById('id_lng').value = myLatlng.lng;

    geocoder = new google.maps.Geocoder();
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: myLatlng
    });
  
    marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      draggable: true
    });
  
    marker.addListener('dragend', function(e) {
      var position = marker.getPosition();
      updateCoordinates(position.lat(), position.lng())
    });
  
    map.addListener('click', function(e) {
      marker.setPosition(e.latLng);
      updateCoordinates(e.latLng.lat(), e.latLng.lng())
    });
  
    map.panTo(myLatlng);
}