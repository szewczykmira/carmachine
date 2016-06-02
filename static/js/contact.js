/**
 * Created by mira on 6/2/16.
 */

function initMap(){
    var mapDiv = document.getElementById("g-map");
    var map = new google.maps.Map(mapDiv, {
      center: {lat: 51.1110443, lng:17.0509038},
      zoom: 15
    });

}