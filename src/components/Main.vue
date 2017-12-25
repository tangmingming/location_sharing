<template>
  <baidu-map style=""
             :center="center"
             :zoom="zoom"
             @ready="handler"
             :scroll-wheel-zoom="true"
  >

    <bm-scale anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-scale>
    <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
    <bm-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" @locationSuccess="location_success" :showAddressBar="true" :autoLocation="true"></bm-geolocation>
  </baidu-map>
</template>
<script>
  import Axios from "axios"
  export default {
    data () {
      return {
        center: {lng: 0, lat: 0},
        zoom: 3,
        BMap: null,
        map: null,
        point: null
      }
    },
    methods: {
      handler ({BMap, map}) {
        var self = this
        console.log(BMap, map)
        this.BMap = BMap
        this.map = map

        this.zoom = 10

        var geolocation = new BMap.Geolocation();
        geolocation.getCurrentPosition(function(r){
          if(this.getStatus() == BMAP_STATUS_SUCCESS){
            self.center.lng = r.point.lng
            self.center.lat = r.point.lat
          }
          else {
            alert('failed'+this.getStatus());
          }
        });
      },
      location_success(point, AddressComponent, marker){
        var geolocation = new BMap.Geolocation();
//        geolocation.getCurrentPosition(function(r){
//          if(this.getStatus() == BMAP_STATUS_SUCCESS){
//            var mk = new BMap.Marker(r.point);
//            map.addOverlay(mk);
//            map.panTo(r.point);
//          }
//          else {
//            alert('failed'+this.getStatus());
//          }
//        });
      },
      add_point(type, target, point, pixel, overlay){
        console.log("add_point")
        var point = new BMap.Point(106.53463501, 29.54460611);
        var label = new BMap.Label("我是文字\n标注哦",{offset:new BMap.Size(20,-10)});
        this.point.setLabel(label)
        this.point.setPosition(point)
      },
      update_postions(){
        let self = this
        console.log("update_postions")
        Axios.get("https://location.mingmingt.xyz/location", {timeout: 5000}).then(function (response) {
          self.map.clearOverlays()
          let locations = response["data"]["locations"]
          console.log(locations)
          for(let location of locations){
            let point = new self.BMap.Point(location["longitude"], location["latitude"])
            let label = new self.BMap.Label(location["spacing"]+"秒前|"+location["username"], {offset:new BMap.Size(-20,-20)})
            let marker = new BMap.Marker(point)
            marker.setLabel(label)
            self.map.addOverlay(marker)
          }
        })
      }
    },
    beforeMount(){
      setInterval(this.update_postions, 10000)
    }
  }
</script>

<style scoped="">
  .map{
    width: 100%;
    height: 100%;
  }
</style>
