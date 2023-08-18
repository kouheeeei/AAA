function initMap() {
  var opts = {
      zoom: 15,
      center: new google.maps.LatLng(35.690921, 139.700258)
  };
var map = new google.maps.Map(document.getElementById("map"), opts);
}